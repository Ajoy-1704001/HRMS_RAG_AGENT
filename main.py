import streamlit as st
import os
import chromadb
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain, ConversationalRetrievalChain
from langchain.schema import HumanMessage, AIMessage
from langchain.chains import StuffDocumentsChain
from dotenv import load_dotenv

load_dotenv()

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = None

# Function to load and process HRMS documents
def load_hrms_documents(directory="hrms_docs"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    loader = DirectoryLoader(directory, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    try:
        documents = loader.load()
    except Exception as e:
        st.error(f"Error loading markdown files from {directory}: {str(e)}")
        return []

    if not documents:
        st.error("No markdown files found in hrms_docs directory. Please add .md files (e.g., add_new_employee.md) to proceed.")
        return []

    for doc in documents:
        filename = os.path.basename(doc.metadata['source'])
        feature_name = filename.replace('.md', '')
        doc.metadata['feature'] = feature_name
        doc.page_content = f"### Feature: {feature_name}\n\n{doc.page_content}"

    return documents

# Function to create vector store
def create_vector_store(documents):
    if not documents:
        return None

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(path="./chroma_db")

    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory="./chroma_db",
        collection_name="hrms_collection",
        collection_metadata={"hnsw:space": "cosine"},
        client=client
    )

    return vectorstore

# Function to setup RAG chain
def setup_rag_chain(vectorstore):
    if vectorstore is None:
        st.error("Vector store could not be created. Please ensure markdown files are present in hrms_docs.")
        return None

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7
    )

    # Prompt must use 'context', 'chat_history', and 'query' as variables
    prompt_template = """You are an expert Tafuri HRMS assistant. Use the documentation below to answer the user's query.

    The documentation may span multiple features. Do NOT copy-paste directly; instead, rephrase in your own words, elaborate clearly, and explain underlying logic or implications where relevant.

    Always aim to help the user understand, even if the exact answer is not in the context.

    Answer using a professional and approachable tone. Repharse the answer. Don't copy paste.

    Context:
    {context}

    Chat History:
    {chat_history}

    Question:
    {question}

    Please provide a **detailed, complete, step-by-step** explanation without stopping prematurely.

    Answer:"""


    prompt = PromptTemplate(
        input_variables=["context", "chat_history", "question"],
        template=prompt_template
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Chain that knows how to combine docs using that LLMChain
    combine_docs_chain = StuffDocumentsChain(
        llm_chain=llm_chain,
        document_variable_name="context"  # This must match your prompt
    )

    condense_prompt = PromptTemplate.from_template("""
        Given the following conversation and a follow-up question, rephrase the follow-up to be a standalone question.

        Chat History:
        {chat_history}
        Follow Up Input: {question}
        Standalone question:
        """)

    question_generator = LLMChain(llm=llm, prompt=condense_prompt)

    # Build the QA chain
    qa_chain = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 6, "fetch_k": 10}),
        combine_docs_chain=combine_docs_chain,
        question_generator=question_generator
    )

    return qa_chain

# Streamlit UI
st.title("Tafuri HRMS Service Agent")
st.write("Ask questions about our Tafuri HRMS")

# Initialize vector store and QA chain
if st.session_state.vectorstore is None:
    if os.path.exists("./chroma_db") and os.path.isdir("./chroma_db") and os.listdir("./chroma_db"):
        # If DB already exists, load it directly
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        client = chromadb.PersistentClient(path="./chroma_db")
        st.session_state.vectorstore = Chroma(
            embedding_function=embeddings,
            persist_directory="./chroma_db",
            collection_name="hrms_collection",
            client=client
        )
        st.session_state.qa_chain = setup_rag_chain(st.session_state.vectorstore)
    else:
        with st.spinner("Loading HRMS documentation..."):
            documents = load_hrms_documents()
            st.session_state.vectorstore = create_vector_store(documents)
            st.session_state.qa_chain = setup_rag_chain(st.session_state.vectorstore)

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know about HRMS?"):
    if st.session_state.qa_chain is None:
        st.error("QA chain not initialized. Please check if markdown files are loaded correctly.")
    else:
        # Add user message to chat history (only string content)
        st.session_state.chat_history.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.write(prompt)

        chat_history = []
        for m in st.session_state.chat_history:
            if m["role"] == "user":
                chat_history.append(HumanMessage(content=m["content"]))
            elif m["role"] == "assistant":
                chat_history.append(AIMessage(content=m["content"]))

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.qa_chain.invoke({
                    "question": prompt,
                    "chat_history": chat_history
                })

                # response may be a dict or string; extract answer string properly
                if isinstance(response, dict):
                    # ConversationalRetrievalChain usually returns {'answer': '...'}
                    answer_text = response.get("answer", str(response))
                else:
                    answer_text = response

                st.markdown(answer_text, unsafe_allow_html=True)
                # Append only the answer string to chat history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": answer_text
                })
                
                incomplete_endings = ["...", "to be continued", "next step", "continued", "step "]

                last_answer = answer_text.lower().strip()
                st.session_state.last_answer_incomplete = any(last_answer.endswith(e) for e in incomplete_endings)



if st.session_state.get("last_answer_incomplete", False):
    if st.button("Continue"):
        # Append user message "Please continue" to chat history
        st.session_state.chat_history.append({
            "role": "user",
            "content": "Please continue"
        })

        # Build chat_history messages for chain input
        chat_history = []
        for m in st.session_state.chat_history:
            if m["role"] == "user":
                chat_history.append(HumanMessage(content=m["content"]))
            elif m["role"] == "assistant":
                chat_history.append(AIMessage(content=m["content"]))

        with st.chat_message("user"):
            st.write("Please continue")

        with st.chat_message("assistant"):
            with st.spinner("Continuing..."):
                response = st.session_state.qa_chain.invoke({
                    "question": "Please continue",
                    "chat_history": chat_history
                })

                if isinstance(response, dict):
                    continuation = response.get("answer", str(response))
                else:
                    continuation = response

                st.markdown(continuation, unsafe_allow_html=True)

                # Append the continuation to chat history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": continuation
                })

                # Update incomplete flag for further continuation if needed
                last_answer = continuation.lower().strip()
                st.session_state.last_answer_incomplete = any(last_answer.endswith(e) for e in incomplete_endings)


# Clear chat history button
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.experimental_rerun()
