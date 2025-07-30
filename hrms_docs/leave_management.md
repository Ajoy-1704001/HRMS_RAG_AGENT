# Leave Feature

## Overview

The **Leave Feature** allows employees to manage and track their leave requests within the organization’s HRMS. This module streamlines the leave application process, making it transparent for both employees and administrators. Employees can view their leave balances, apply for leave, check application status, and access leave history. Admins or managers can review, approve, or reject leave requests and monitor overall leave records for compliance and planning.

---

## Leave Request Approval Flow

When an employee submits a leave request, the approval process follows this sequence:

1. **Line Manager**  
   The primary (direct) manager reviews the leave request first.

2. **Dotted Manager 1 (if any)**  
   If a dotted-line manager is configured, they review the request after the line manager.

3. **Dotted Manager 2 (if any)**  
   If a second dotted-line manager is configured, they review after Dotted Manager 1.

4. **Admin (if configured from company configuration)**  
   Finally, if the company settings require admin approval, the request goes to the admin for the final decision.

*The leave will only be fully approved after it passes through all configured approvers in this sequence.*

---

## Leave Management Steps

### For Employees

1. **Access the Leave Section**
   - Log in to the HRMS.
   - Navigate to the **Leave** section from the main dashboard or side navigation bar.

2. **View Leave Balance**
   - The leave dashboard displays your current leave balances for different leave types (e.g., annual, sick, casual).

3. **Apply for Leave**
   - Click the **Apply Leave** button.
   - Fill in required details:
     - Leave Type (e.g., Annual, Sick)
     - From Date, To Date
     - Reason for Leave
     - Any supporting attachment (if required)
   - Submit the leave application.

4. **Check Leave Status**
   - After applying, you can track the status (Pending, Approved, Rejected) of your request in the **Leave History** or **Leave Status** section.

### For Admins/Managers

1. **Review Leave Applications**
   - Access the **Leave Applications** dashboard.
   - View pending leave requests, including details like employee name, leave type, and requested dates.

2. **Approve or Reject Requests**
   - Click on a leave application to review its details.
   - Approve or reject the request with optional remarks.
   - The next approver (if any) will be notified, or the process is completed if it's the final step.

3. **Monitor Leave Records**
   - Generate reports or view logs for all leave requests for compliance, planning, or payroll purposes.

4. **View Monthly Leave Report**
   - Login to the HRMS. Go to the Leave Info tab from the navigation drawer at the left of the screen.
   - Go to the Leave Report Section. This page will show the monthly leave report of all employees.

5. **View and Download Individual Employee Leave Report**
   - Go to the Individual Leave Report Section.
   - Select the Employee.
   - Employee’s leave balance and calendar will be shown here.
   - Click the Download Report button to download individual employee’s leave report(pdf).

6. **Update Annual Leave Count**
   - Click the Update Annual Leave Count Button
   - Update the Total Expected Earned Leave and Total Carry Forward and click the Update button.
   - (note: Selected employee must have annual leave in his/her leave policy)

7. **View Bradford Score**
   - Go to the Bradford factor tab. This page will show all employee’s Bradford scores.
   - Optionally You can Click on the Employee’s name to see the employee's yearly leave report.

---

## FAQs

### Q1: **How do I apply for leave?**
- Go to the Leave section, click “Apply Leave,” fill in the required details, and submit.

### Q2: **Can I view my remaining leave balance?**
- Yes, your current leave balances for all types are shown on the leave dashboard.

### Q3: **Who approves my leave request?**
- Your leave request is routed through:  
  **Line Manager → Dotted Manager 1 (if any) → Dotted Manager 2 (if any) → Admin (if configured)**.  
  Each approver in this sequence must approve the request for it to be finalized.

### Q4: **How will I know if my leave is approved or rejected?**
- You will receive a system notification and can check the updated status in your Leave History.

### Q5: **Can I attach documents to my leave request?**
- Yes, supporting documents (such as medical certificates) can be uploaded when applying. But it depends on the leave policy. In leave policy, each leave type have these settings configured whether attachment is needed or not.

### Q6: **Can I edit/delete my leave request?**
- Yes, if your request status is still pending and not approved by any of the managers or admin, then you can see an edit/delete button along with your leave request in my leave request section.

---

## System Notes

- **Approval Sequence:** Leave requests are processed in the configured order of Line Manager → Dotted Managers → Admin, with each needing to approve before final approval.
- **Access Control:** Only authorized users (employees, managers, admins) can perform actions relevant to their roles.
- **Notifications:** System sends notifications and email for leave status changes (approved, rejected).
- **Compliance:** Leave entitlements and balances are calculated based on organizational policy.
- **Attachment Handling:** System supports attachment uploads with each leave application for supporting evidence.
- **Data Security:** All personal and leave data is stored securely, accessible only to authorized personnel.

---

