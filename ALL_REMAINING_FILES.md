# 📂 ALL REMAINING FILES - COMPLETE CODE

This document contains ALL the code for remaining files. Create each file and copy the respective code.

---

## 🎓 STUDENT MANAGEMENT FILES

### File: `src/main/webapp/deleteStudent.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Delete Student - UMS</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; background: #f5f7fa; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;
                  padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .container { max-width: 600px; margin: 50px auto; padding: 0 20px; }
        .card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h2 { color: #e74c3c; margin-bottom: 30px; }
        label { display: block; margin-bottom: 8px; color: #333; font-weight: 500; }
        input { width: 100%; padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 14px; margin-bottom: 20px; }
        input:focus { outline: none; border-color: #e74c3c; }
        .btn { padding: 14px 30px; background: #e74c3c; color: white; border: none;
               border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: 600; }
        .btn:hover { background: #c0392b; }
        .warning { background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin-bottom: 20px;
                   border-radius: 8px; color: #856404; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🗑️ Delete Student</h1>
        <a href="dashboard.jsp" style="color: white; text-decoration: none;">← Back</a>
    </div>
    <div class="container">
        <div class="card">
            <h2>⚠️ Delete Student Record</h2>
            <div class="warning">
                <strong>Warning!</strong> This action cannot be undone. All related records (attendance, marks, fees) will be permanently deleted.
            </div>
            <form action="deleteStudent" method="POST" onsubmit="return confirm('Are you SURE you want to delete this student? This cannot be undone!');">
                <label>Roll Number:</label>
                <input type="text" name="roll_no" required placeholder="Enter Roll Number (e.g., 2301001)" pattern="[0-9]{7}">
                <button type="submit" class="btn">Delete Student</button>
            </form>
        </div>
    </div>
</body>
</html>
```

---

### File: `src/main/webapp/searchStudent.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Search Student - UMS</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; background: #f5f7fa; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;
                  padding: 20px 40px; }
        .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
        .card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .search-box { display: flex; gap: 10px; margin-bottom: 30px; }
        input { flex: 1; padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; }
        .btn { padding: 12px 30px; background: #667eea; color: white; border: none;
               border-radius: 8px; cursor: pointer; }
        .btn:hover { background: #764ba2; }
        .result { display: none; margin-top: 30px; }
        table { width: 100%; border-collapse: collapse; }
        th { background: #667eea; color: white; padding: 12px; text-align: left; }
        td { padding: 12px; border-bottom: 1px solid #e0e0e0; }
        .error { background: #ffe0e0; color: #c0392b; padding: 15px; border-radius: 8px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 Search Student</h1>
    </div>
    <div class="container">
        <div class="card">
            <div class="search-box">
                <input type="text" id="rollNo" placeholder="Enter Roll Number (e.g., 2301001)" pattern="[0-9]{7}">
                <button onclick="searchStudent()" class="btn">Search</button>
            </div>
            <div id="message"></div>
            <div id="result" class="result"></div>
        </div>
    </div>
    <script>
        function searchStudent() {
            const rollNo = document.getElementById('rollNo').value.trim();
            const messageDiv = document.getElementById('message');
            const resultDiv = document.getElementById('result');
            
            if (!rollNo) {
                messageDiv.innerHTML = '<div class="error">Please enter a roll number!</div>';
                return;
            }
            
            fetch('updateStudent?roll_no=' + rollNo)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        resultDiv.style.display = 'block';
                        resultDiv.innerHTML = `
                            <h3 style="color: #27ae60; margin-bottom: 20px;">✓ Student Found</h3>
                            <table>
                                <tr><th>Roll No</th><td>${data.roll_no}</td></tr>
                                <tr><th>Name</th><td>${data.name}</td></tr>
                                <tr><th>Father's Name</th><td>${data.father_name}</td></tr>
                                <tr><th>DOB</th><td>${data.dob}</td></tr>
                                <tr><th>Phone</th><td>${data.phone}</td></tr>
                                <tr><th>Email</th><td>${data.email}</td></tr>
                                <tr><th>Course</th><td>${data.course}</td></tr>
                                <tr><th>Branch</th><td>${data.branch}</td></tr>
                                <tr><th>Semester</th><td>${data.semester}</td></tr>
                                <tr><th>Status</th><td>${data.status}</td></tr>
                            </table>
                        `;
                        messageDiv.innerHTML = '';
                    } else {
                        messageDiv.innerHTML = '<div class="error">✗ Student not found!</div>';
                        resultDiv.style.display = 'none';
                    }
                })
                .catch(error => {
                    messageDiv.innerHTML = '<div class="error">Error: ' + error + '</div>';
                });
        }
    </script>
</body>
</html>
```

---

## 📋 ATTENDANCE MANAGEMENT FILES

### File: `src/main/java/servlets/AddStudentAttendanceServlet.java`

```java
package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/addStudentAttendance")
public class AddStudentAttendanceServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        HttpSession session = request.getSession(false);
        if (session == null || !"true".equals(session.getAttribute("isAdmin"))) {
            response.sendRedirect("login.html");
            return;
        }
        
        String rollNo = request.getParameter("roll_no");
        int semester = Integer.parseInt(request.getParameter("semester"));
        int totalClasses = Integer.parseInt(request.getParameter("total_classes"));
        int attendedClasses = Integer.parseInt(request.getParameter("attended_classes"));
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            // Check if attendance record exists
            String checkQuery = "SELECT * FROM attendance_student WHERE roll_no=? AND semester=?";
            PreparedStatement checkPst = db.c.prepareStatement(checkQuery);
            checkPst.setString(1, rollNo);
            checkPst.setInt(2, semester);
            ResultSet rs = checkPst.executeQuery();
            
            String query;
            PreparedStatement pst;
            
            if (rs.next()) {
                // Update existing record
                query = "UPDATE attendance_student SET total_classes=?, attended_classes=? WHERE roll_no=? AND semester=?";
                pst = db.c.prepareStatement(query);
                pst.setInt(1, totalClasses);
                pst.setInt(2, attendedClasses);
                pst.setString(3, rollNo);
                pst.setInt(4, semester);
            } else {
                // Insert new record
                query = "INSERT INTO attendance_student (roll_no, semester, total_classes, attended_classes) VALUES (?, ?, ?, ?)";
                pst = db.c.prepareStatement(query);
                pst.setString(1, rollNo);
                pst.setInt(2, semester);
                pst.setInt(3, totalClasses);
                pst.setInt(4, attendedClasses);
            }
            
            int result = pst.executeUpdate();
            double percentage = (totalClasses > 0) ? (attendedClasses * 100.0 / totalClasses) : 0;
            
            rs.close();
            checkPst.close();
            pst.close();
            db.closeConnection();
            
            if (result > 0) {
                showMessage(out, "success", String.format(
                    "Attendance recorded successfully!<br>" +
                    "Roll No: %s<br>Semester: %d<br>" +
                    "Attended: %d/%d<br>Percentage: %.2f%%",
                    rollNo, semester, attendedClasses, totalClasses, percentage
                ));
            }
            
        } catch (SQLException e) {
            showMessage(out, "error", "Error: " + e.getMessage());
        }
    }
    
    private void showMessage(PrintWriter out, String type, String message) {
        String bgColor = type.equals("success") ? "#27ae60" : "#e74c3c";
        out.println("<!DOCTYPE html><html><head><meta charset='UTF-8'><title>" + type + "</title>");
        out.println("<style>body{font-family:Arial;display:flex;align-items:center;justify-content:center;");
        out.println("min-height:100vh;background:linear-gradient(135deg,#667eea,#764ba2);}");
        out.println(".box{background:white;padding:40px;border-radius:20px;text-align:center;}");
        out.println("h2{color:" + bgColor + ";}");
        out.println(".btn{background:#667eea;color:white;padding:12px 30px;text-decoration:none;");
        out.println("border-radius:8px;display:inline-block;margin:5px;}</style></head><body>");
        out.println("<div class='box'><h2>" + type.toUpperCase() + "</h2><p>" + message + "</p>");
        out.println("<a href='addStudentAttendance.html' class='btn'>Mark Another</a>");
        out.println("<a href='dashboard.jsp' class='btn'>Dashboard</a></div></body></html>");
    }
}
```

---

### File: `src/main/webapp/addStudentAttendance.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mark Attendance - UMS</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; background: #f5f7fa; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;
                  padding: 20px 40px; }
        .container { max-width: 600px; margin: 50px auto; padding: 0 20px; }
        .card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h2 { color: #667eea; margin-bottom: 30px; }
        label { display: block; margin-bottom: 8px; color: #333; font-weight: 500; }
        input, select { width: 100%; padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px;
                        font-size: 14px; margin-bottom: 20px; }
        .btn { padding: 14px 30px; background: #667eea; color: white; border: none;
               border-radius: 8px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #764ba2; }
    </style>
</head>
<body>
    <div class="header"><h1>✅ Mark Student Attendance</h1></div>
    <div class="container">
        <div class="card">
            <h2>Record Attendance</h2>
            <form action="addStudentAttendance" method="POST">
                <label>Roll Number:</label>
                <input type="text" name="roll_no" required pattern="[0-9]{7}">
                
                <label>Semester:</label>
                <select name="semester" required>
                    <option value="1">1st Semester</option>
                    <option value="2">2nd Semester</option>
                    <option value="3">3rd Semester</option>
                    <option value="4">4th Semester</option>
                    <option value="5">5th Semester</option>
                    <option value="6">6th Semester</option>
                    <option value="7">7th Semester</option>
                    <option value="8">8th Semester</option>
                </select>
                
                <label>Total Classes:</label>
                <input type="number" name="total_classes" required min="1">
                
                <label>Classes Attended:</label>
                <input type="number" name="attended_classes" required min="0">
                
                <button type="submit" class="btn">Mark Attendance</button>
            </form>
        </div>
    </div>
</body>
</html>
```

---

## 👨‍🏫 TEACHER MANAGEMENT FILES

### File: `src/main/java/servlets/ViewTeachersServlet.java`

```java
package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/viewTeachers")
public class ViewTeachersServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("username") == null) {
            response.sendRedirect("login.html");
            return;
        }

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<!DOCTYPE html><html><head>");
        out.println("<meta charset='UTF-8'><title>View Teachers - UMS</title>");
        out.println("<style>");
        out.println("body{font-family:Arial;background:#f5f7fa;margin:0;}");
        out.println(".header{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;");
        out.println("padding:20px 40px;display:flex;justify-content:space-between;align-items:center;}");
        out.println(".container{max-width:1400px;margin:20px auto;padding:0 20px;}");
        out.println(".card{background:white;padding:30px;border-radius:15px;box-shadow:0 2px 10px rgba(0,0,0,0.1);}");
        out.println("table{width:100%;border-collapse:collapse;margin-top:20px;}");
        out.println("th{background:#667eea;color:white;padding:12px;text-align:left;}");
        out.println("td{padding:12px;border-bottom:1px solid #e0e0e0;}");
        out.println("tr:hover{background:#f8f9fa;}");
        out.println(".btn{padding:10px 20px;background:#667eea;color:white;text-decoration:none;");
        out.println("border-radius:8px;display:inline-block;}");
        out.println("</style></head><body>");

        out.println("<div class='header'>");
        out.println("<h1>👨‍🏫 View All Teachers</h1>");
        out.println("<a href='dashboard.jsp' class='btn'>← Back</a>");
        out.println("</div>");

        out.println("<div class='container'><div class='card'>");

        try {
            conn db = new conn();
            String query = "SELECT * FROM teacher ORDER BY emp_id";
            ResultSet rs = db.s.executeQuery(query);

            out.println("<h2>Teacher Records</h2>");
            out.println("<table><thead><tr>");
            out.println("<th>Emp ID</th><th>Name</th><th>Qualification</th><th>Department</th>");
            out.println("<th>Phone</th><th>Email</th><th>Status</th>");
            out.println("</tr></thead><tbody>");

            while (rs.next()) {
                out.println("<tr>");
                out.println("<td><strong>" + rs.getString("emp_id") + "</strong></td>");
                out.println("<td>" + rs.getString("name") + "</td>");
                out.println("<td>" + rs.getString("qualification") + "</td>");
                out.println("<td>" + rs.getString("department") + "</td>");
                out.println("<td>" + rs.getString("phone") + "</td>");
                out.println("<td>" + rs.getString("email") + "</td>");
                out.println("<td>" + rs.getString("status") + "</td>");
                out.println("</tr>");
            }

            out.println("</tbody></table>");
            rs.close();
            db.closeConnection();

        } catch (SQLException e) {
            out.println("<h3 style='color:#e74c3c;'>Error: " + e.getMessage() + "</h3>");
        }

        out.println("</div></div></body></html>");
    }
}
```

### File: `src/main/java/servlets/AddTeacherServlet.java`

```java
package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/addTeacher")
public class AddTeacherServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        HttpSession session = request.getSession(false);
        if (session == null || !"true".equals(session.getAttribute("isAdmin"))) {
            response.sendRedirect("login.html");
            return;
        }

        String empId = request.getParameter("emp_id");
        String name = request.getParameter("name");
        String fatherName = request.getParameter("father_name");
        String dob = request.getParameter("dob");
        String address = request.getParameter("address");
        String phone = request.getParameter("phone");
        String email = request.getParameter("email");
        String qualification = request.getParameter("qualification");
        String department = request.getParameter("department");
        String designation = request.getParameter("designation");
        String gender = request.getParameter("gender");

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        try {
            conn db = new conn();

            String query = "INSERT INTO teacher (emp_id, name, father_name, dob, address, phone, email, " +
                          "qualification, department, designation, gender, status) " +
                          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Active')";

            PreparedStatement pst = db.c.prepareStatement(query);
            pst.setString(1, empId);
            pst.setString(2, name);
            pst.setString(3, fatherName);
            pst.setString(4, dob);
            pst.setString(5, address);
            pst.setString(6, phone);
            pst.setString(7, email);
            pst.setString(8, qualification);
            pst.setString(9, department);
            pst.setString(10, designation);
            pst.setString(11, gender);

            pst.executeUpdate();
            pst.close();
            db.closeConnection();

            showMessage(out, "success", "Teacher added successfully!<br>Emp ID: " + empId);

        } catch (SQLException e) {
            showMessage(out, "error", "Error: " + e.getMessage());
        }
    }

    private void showMessage(PrintWriter out, String type, String message) {
        String bgColor = type.equals("success") ? "#27ae60" : "#e74c3c";
        out.println("<!DOCTYPE html><html><head><meta charset='UTF-8'><title>" + type + "</title>");
        out.println("<style>body{font-family:Arial;display:flex;align-items:center;justify-content:center;");
        out.println("min-height:100vh;background:linear-gradient(135deg,#667eea,#764ba2);}");
        out.println(".box{background:white;padding:40px;border-radius:20px;text-align:center;}");
        out.println("h2{color:" + bgColor + ";}.btn{background:#667eea;color:white;padding:12px 30px;");
        out.println("text-decoration:none;border-radius:8px;display:inline-block;margin:5px;}</style></head><body>");
        out.println("<div class='box'><h2>" + type.toUpperCase() + "</h2><p>" + message + "</p>");
        out.println("<a href='addTeacher.html' class='btn'>Add Another</a>");
        out.println("<a href='dashboard.jsp' class='btn'>Dashboard</a></div></body></html>");
    }
}
```

---

## 📊 MARKS MANAGEMENT FILES

### File: `src/main/java/servlets/ViewMarksServlet.java`

```java
package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/viewMarks")
public class ViewMarksServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("username") == null) {
            response.sendRedirect("login.html");
            return;
        }

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<!DOCTYPE html><html><head>");
        out.println("<meta charset='UTF-8'><title>View Marks - UMS</title>");
        out.println("<style>");
        out.println("body{font-family:Arial;background:#f5f7fa;margin:0;}");
        out.println(".header{background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:20px 40px;}");
        out.println(".container{max-width:1400px;margin:20px auto;padding:0 20px;}");
        out.println(".card{background:white;padding:30px;border-radius:15px;}");
        out.println("table{width:100%;border-collapse:collapse;margin-top:20px;}");
        out.println("th{background:#667eea;color:white;padding:12px;text-align:left;}");
        out.println("td{padding:12px;border-bottom:1px solid #e0e0e0;}");
        out.println("</style></head><body>");

        out.println("<div class='header'><h1>📊 View Marks</h1></div>");
        out.println("<div class='container'><div class='card'>");

        try {
            conn db = new conn();
            String query = "SELECT m.*, s.name FROM marks m JOIN student s ON m.roll_no = s.roll_no ORDER BY m.roll_no";
            ResultSet rs = db.s.executeQuery(query);

            out.println("<table><thead><tr>");
            out.println("<th>Roll No</th><th>Name</th><th>Subject</th><th>Semester</th>");
            out.println("<th>Internal</th><th>External</th><th>Total</th><th>Grade</th>");
            out.println("</tr></thead><tbody>");

            while (rs.next()) {
                int total = rs.getInt("internal_marks") + rs.getInt("external_marks");
                String grade = total >= 85 ? "A" : total >= 70 ? "B" : total >= 55 ? "C" : total >= 40 ? "D" : "F";

                out.println("<tr>");
                out.println("<td>" + rs.getString("roll_no") + "</td>");
                out.println("<td>" + rs.getString("name") + "</td>");
                out.println("<td>" + rs.getString("subject_code") + "</td>");
                out.println("<td>" + rs.getInt("semester") + "</td>");
                out.println("<td>" + rs.getInt("internal_marks") + "</td>");
                out.println("<td>" + rs.getInt("external_marks") + "</td>");
                out.println("<td><strong>" + total + "</strong></td>");
                out.println("<td><strong>" + grade + "</strong></td>");
                out.println("</tr>");
            }

            out.println("</tbody></table>");
            rs.close();
            db.closeConnection();

        } catch (SQLException e) {
            out.println("<h3 style='color:#e74c3c;'>Error: " + e.getMessage() + "</h3>");
        }

        out.println("</div></div></body></html>");
    }
}
```

---

**(Continue to next page for Fee Management, Subject Management, and AI/ML Backend)**
