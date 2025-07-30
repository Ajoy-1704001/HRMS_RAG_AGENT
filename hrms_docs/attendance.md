# Attendance Module Knowledge Base

> This document describes the Attendance feature set for HRMS, including step-by-step usage and frequently asked questions.

---

## Overview

The Attendance module lets Admins, Organization Admins, and Employees **view, upload, download, and manage attendance records** at both individual and bulk levels, handle manual requests, and process shift exchanges. Feature access depends on user role.

---

## Features & Steps

### 1. Daily Attendance Report (Admin/Org Admin)

1. **Login** to HRMS and go to the **Attendance** tab in the side navigation.
2. Go to the **Daily Attendance** tab.
3. Select the required **Date, Month, and Year**.
4. The page displays daily attendance for all employees, categorized as:
    - Total
    - Present
    - Late
    - Half Day
    - Absent
    - Leave
    - AFL / LFA
5. Click **Download Report** to export daily records.

---

### 2. Individual Attendance Report (Admin/Org Admin)

1. Go to **Individual Attendance** section.
2. Select the **Employee**.
3. View the attendance details.
4. Toggle the action button to mark as **absent** if needed.
5. Click **Download Report** for export.
6. Click **Upload Individual Attendance** to upload data for an employee.
7. Select **Start Date** and **End Date**, then upload by clicking **Upload**.

---

### 3. Monthly Attendance (Bulk, Admin/Org Admin)

1. Go to **Monthly Attendance** tab.
2. Select the **Month**.
3. Click **Upload Bulk Attendance**.
4. Use filters for employee, department, grade, or location.
5. Choose **Start Date** and **End Date**.
6. Upload the file with the **Upload** button.
7. Click **Download Report** for monthly export.

---

### 4. Manual Attendance Request (Admin/Org Admin)

1. Go to **Manual Attendance Request** tab.
2. View manual requests from employees.
3. Click **Request** to **Accept** or **Reject**.

---

### 5. Attendance Metrics Report

1. Go to **Attendance Metrics** tab.
2. Select **Date Range** and click **Apply**.
3. Select **Report Column**.
4. Click **Generate**.
5. Click **Export** to save the report.

---

### 6. Employee View

- **View Own Attendance:** Click **My Attendance** tab.
- **Request Attendance:** Click **Edit**, provide information, and **Confirm submit**.

#### Approval Flow for Attendance Requests

1. Line Manager
2. Dotted Manager 1 (if any)
3. Dotted Manager 2 (if any)
4. Admin (if configured by company)

---

### 7. Shift Exchange Requests & Approval

- **Send Request:**
    1. Go to **Shift Calendar** > **My Roster**.
    2. Click the **Shift Cell** to be changed.
    3. Select **New Shift** and employee to swap with.
    4. Click **Change** to send request.

- **Approval Process:**
    1. Sent request appears under **Shift Exchange Approval – My request**.
    2. Recipient can accept via **Exchange Request** tab.
    3. Final acceptance by line manager (**Subordinate Request** tab).
    4. Accepted requests update the Shift Calendar.

---

## FAQs

**Q1: Who can view and download attendance reports?**  
A: Only User Admins and Organization Admins can view, upload, or download attendance data for all employees. Employees can view and request their own attendance.

---

**Q2: How do attendance requests get approved?**  
A: Attendance requests follow this flow:  
Line Manager → Dotted Manager 1 (if any) → Dotted Manager 2 (if any) → Admin (if configured by company).

---

**Q3: Can an employee upload or change their own attendance?**  
A: Employees can request changes to their own attendance, but changes must be approved as per the approval flow.

---

**Q4: What happens if an employee’s attendance is incorrect?**  
A: Admins can toggle the attendance status (e.g., mark present as absent) and upload correct records as needed.

---

**Q5: Is there a way to upload attendance in bulk?**  
A: Yes, via the **Monthly Attendance** tab, admins can use **Upload Bulk Attendance** and advanced filters.

---

**Q6: Can I see attendance metrics for a custom period?**  
A: Yes, select your desired date range in the **Attendance Metrics** tab, generate the report, and export as needed. Obviously, you need to be in admin/organization admin/role based admin with attendance feature access.

---

**Q7: What does AFL and LFA stand for?**  
A: AFL stands for Applied for leave and LFA stands for Leave Fare Assistance.

---

## System Notes

- All report downloads are available from their respective attendance tabs.
- Filtering by department, grade, or location is supported for bulk uploads.
- Admin approval workflows can be customized in company configuration.

---
