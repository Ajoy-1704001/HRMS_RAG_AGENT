# 📘 Add New Employee – HRMS Comprehensive Guide

## 🔍 Overview

The **Add New Employee** module in HRMS enables administrators to create or rehire employee profiles by submitting structured data through a multi-tab form interface. The process is robust, supporting data validation, conditional fields, secure draft saving, and compliance-ready document handling.

This feature ensures seamless employee onboarding and data integrity by enforcing business rules and validations across different sections like personal information, employment details, compensation, and experience.

---

## 🧭 Navigation Path

1. Log in to the HRMS portal with valid admin credentials.
2. Navigate to: **Employees → All Employees**
3. Click on the **Add Employees** button.
4. Select the relevant **Company** from the dropdown.

---

## 📝 Step-by-Step Process

### 📂 Step 1: Company Details

This is the initial tab where company-related employee configuration is added.

**Mandatory Fields:**

- `Action`: Choose between **Add New Employee** or **Rehire**
- `Company`: Select from the list of configured companies
- `Employee ID`: Follows the format `EMP12345`
- `First Name`, `Last Name`
- `Employee Role`: Options include *User*, *Admin*, *Organization Admin*
- `Employment Type`: Options like *Management*, *Worker*, *Staff*
- `Location`, `Department`, `Designation`
- `Employment Status`: *Trainee*, *Contractual*, *Probation*, *Permanent*
- `Date of Joining`
- `Line Manager`, `Attendance Roster`
- `Leave Policy`, `Leave Type`, `Holiday Policy`

**Optional Fields:**

- `Official Email`, `Phone`
- `Can Be`: *Line Manager*, *Team Leader*, *HOD*
- `Team Leader`, `Head of Department`

✅ Click **Continue** to proceed.

---

### 👤 Step 2: Personal Details

Capture personal and demographic information of the employee.

**Mandatory Fields:**

- `Gender`
- `Date of Birth (Certificate)`
- `Marital Status`

**Optional Fields:**

- `Father Name`, `Mother Name`, `Blood Group`
- `Original Date of Birth`
- `Personal Email`, `Nationality`
- `National ID (NID)`, `Tax ID (TIN)`, `Religion`

**Address Details:**

- **Present Address**: Line 1, Line 2, Line 3, City, State, Country
- **Permanent Address**: Same structure, with an option to copy from present address

✅ Click **Continue** to proceed.

---

### 💰 Step 3: Compensation & Benefits

Defines the employee’s financial and benefits-related setup.

**Mandatory Fields:**

- `Bank Name`, `Branch Name`, `Account Number`
- `Joining Salary (Total)`
- `Bank Amount`

**Optional Fields:**

- `Cash Amount`
- **Benefits (multi-select):** 
  - Provident Fund
  - Gratuity
  - Transport
  - Dormitory
  - LFA (Leave Fare Assistance)
  - Insurance
  - Bonus

**Nominee Details:**

- Mandatory: `Name`, `Relation`, `Percentage`
- Optional: `Date of Birth`, `Mobile`, `Address`

> 💡 **Note**: `Joining Salary = Bank Amount + Cash Amount`

✅ Click **Continue** to proceed.

---

### ☎️ Step 4: Emergency Contact

Provide emergency contact details for use in urgent scenarios.

**Mandatory Fields:**

- `Name`, `Relation`, `Contact Number`

**Optional Fields:**

- `Email`, `Address` (can be copied from employee’s address)

✅ Click **Continue** to proceed.

---

### 🎓 Step 5: Education & Experience

Document educational background and work history.

**Education Section:**

- `Degree/Certification`, `Major/Group`, `Institute Name`
- Optional: `Result`, `Year`, `Duration`, `Upload Certificate`

**Experience Section:**

- `Company Name`, `Designation`, `Department`, `Industry`
- `Employment Type`: *Full-Time*, *Part-Time*, *Contract*, *Internship*
- Optional: Upload **Experience Certificate**

✅ Click **Continue** to proceed.

---

### 📎 Step 6: Document Upload

Handles submission of important identification and supporting documents.

**Required Documents:**

- National ID (NID)
- CV
- Appointment Letter
- Profile Picture

**Optional Uploads:**

- Custom document with:
  - `Document Name`
  - `File Upload`
  - `Description`

✅ Click **Continue** to proceed.

---

### ✅ Step 7: Final Review and Submission

At this stage:

- All previously entered data is shown for final verification.
- The user can:
  - Click **Submit** to finalize the entry.
  - Use **Save as Draft** to temporarily save and complete later.

---

## 🛡️ Business Policies and Rules

- **Draft Saving:** Incomplete forms can be saved and resumed from the *Drafted Employees* section.
- **Validation Rules:**
  - Mandatory fields must be filled before submission.
  - Format for `Employee ID` must follow `EMP` + 5-digit format (e.g., `EMP00045`).
- **Data Protection:** All submitted information is encrypted and stored according to GDPR compliance.

---

## ❓ FAQs

### 🔹 What is the correct format for Employee ID?
It should follow the format `EMP` followed by five digits. Example: `EMP12345`.

### 🔹 Can I save the form and complete it later?
Yes, click on **Save as Draft** at any point during the process.

### 🔹 What happens if I forget to fill a required field?
The system will display a validation message and prevent further progress until corrected.

### 🔹 How can I auto-fill the permanent address?
Use the checkbox **Same as Present Address** to copy the address fields.

### 🔹 Which documents are mandatory to upload?
You must upload:
- National ID (NID)
- CV
- Appointment Letter
- Profile Picture

### 🔹 What does the “Rehire” action do?
Selecting **Rehire** fetches previous employee data (if available), allowing updates before final submission.

---

## 📌 Best Practices

- Always double-check the **Employment Status** and **Department** mapping.
- Ensure bank account details are correctly entered to avoid salary disbursement issues.
- Upload clear, legible documents for verification purposes.
- Use unique Employee IDs to avoid duplicates.
