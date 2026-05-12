<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    // Check if user is logged in
    String username = (String) session.getAttribute("username");
    String name = (String) session.getAttribute("name");
    String role = (String) session.getAttribute("role");
    String isAdminStr = (String) session.getAttribute("isAdmin");
    
    if (username == null) {
        response.sendRedirect("login.html");
        return;
    }
    
    boolean isAdmin = "true".equals(isAdminStr) || "admin".equals(role);
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - UMS</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f7fa;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .header h1 {
            font-size: 24px;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .user-info span {
            background: rgba(255,255,255,0.2);
            padding: 8px 15px;
            border-radius: 20px;
        }

        .btn-logout {
            background: #e74c3c;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            transition: background 0.3s;
        }

        .btn-logout:hover {
            background: #c0392b;
        }

        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }

        .welcome-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .welcome-card h2 {
            color: #667eea;
            margin-bottom: 10px;
        }

        .role-badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-left: 10px;
        }

        .role-admin {
            background: #27ae60;
            color: white;
        }

        .role-user {
            background: #3498db;
            color: white;
        }

        .section {
            margin-bottom: 40px;
        }

        .section-title {
            font-size: 20px;
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .menu-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            text-decoration: none;
            color: #333;
            transition: all 0.3s;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .menu-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        }

        .menu-card h3 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 18px;
        }

        .menu-card p {
            color: #666;
            font-size: 14px;
        }

        .icon {
            font-size: 40px;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎓 University Management System</h1>
        <div class="user-info">
            <span><%= name %></span>
            <span class="role-badge <%= isAdmin ? "role-admin" : "role-user" %>">
                <%= isAdmin ? "ADMIN" : "USER" %>
            </span>
            <a href="logout" class="btn-logout">Logout</a>
        </div>
    </div>

    <div class="container">
        <div class="welcome-card">
            <h2>Welcome back, <%= name %>! 👋</h2>
            <p>You are logged in as: <strong><%= isAdmin ? "Administrator" : "User" %></strong></p>
            <% if (!isAdmin) { %>
                <p style="margin-top:10px; color:#e74c3c;">
                    ⚠️ <strong>Note:</strong> You have read-only access. Contact admin for modifications.
                </p>
            <% } %>
        </div>

        <!-- View Records Section (Available to All) -->
        <div class="section">
            <h2 class="section-title">📊 View Records</h2>
            <div class="menu-grid">
                <a href="viewStudents" class="menu-card">
                    <div class="icon">👨‍🎓</div>
                    <h3>View Students</h3>
                    <p>View all student records</p>
                </a>
                <a href="viewTeachers" class="menu-card">
                    <div class="icon">👨‍🏫</div>
                    <h3>View Teachers</h3>
                    <p>View all teacher records</p>
                </a>
                <a href="viewStudentAttendance" class="menu-card">
                    <div class="icon">📋</div>
                    <h3>Student Attendance</h3>
                    <p>View attendance records</p>
                </a>
                <a href="viewMarks" class="menu-card">
                    <div class="icon">📝</div>
                    <h3>Examination Marks</h3>
                    <p>View marks and grades</p>
                </a>
                <a href="viewFees" class="menu-card">
                    <div class="icon">💰</div>
                    <h3>Fee Records</h3>
                    <p>View fee payment status</p>
                </a>
                <a href="analytics.jsp" class="menu-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
                    <div class="icon">🤖</div>
                    <h3>AI/ML Analytics</h3>
                    <p>Performance predictions & insights</p>
                </a>
            </div>
        </div>

        <% if (isAdmin) { %>
        <!-- Student Management Section (Admin Only) -->
        <div class="section">
            <h2 class="section-title">🎓 Student Management</h2>
            <div class="menu-grid">
                <a href="addStudent.html" class="menu-card">
                    <div class="icon">➕</div>
                    <h3>Add Student</h3>
                    <p>Register new student</p>
                </a>
                <a href="updateStudent.html" class="menu-card">
                    <div class="icon">✏️</div>
                    <h3>Update Student</h3>
                    <p>Modify student information</p>
                </a>
                <a href="deleteStudent.html" class="menu-card">
                    <div class="icon">🗑️</div>
                    <h3>Delete Student</h3>
                    <p>Remove student record</p>
                </a>
                <a href="searchStudent.html" class="menu-card">
                    <div class="icon">🔍</div>
                    <h3>Search Student</h3>
                    <p>Find student by Roll No</p>
                </a>
                <a href="addStudentAttendance.html" class="menu-card">
                    <div class="icon">✅</div>
                    <h3>Mark Attendance</h3>
                    <p>Record student attendance</p>
                </a>
            </div>
        </div>

        <!-- Teacher Management Section (Admin Only) -->
        <div class="section">
            <h2 class="section-title">👨‍🏫 Teacher Management</h2>
            <div class="menu-grid">
                <a href="addTeacher.html" class="menu-card">
                    <div class="icon">➕</div>
                    <h3>Add Teacher</h3>
                    <p>Register new teacher</p>
                </a>
            </div>
        </div>

        <!-- Marks Management Section (Admin Only) -->
        <div class="section">
            <h2 class="section-title">📊 Marks Management</h2>
            <div class="menu-grid">
                <a href="addMarks.html" class="menu-card">
                    <div class="icon">📝</div>
                    <h3>Add/Update Marks</h3>
                    <p>Enter student examination marks</p>
                </a>
            </div>
        </div>

        <!-- Fee Management Section (Admin Only) -->
        <div class="section">
            <h2 class="section-title">💰 Fee Management</h2>
            <div class="menu-grid">
                <a href="addFees.html" class="menu-card">
                    <div class="icon">💳</div>
                    <h3>Add/Update Fee Record</h3>
                    <p>Record fee payments</p>
                </a>
            </div>
        </div>
        <% } %>
    </div>
</body>
</html>
