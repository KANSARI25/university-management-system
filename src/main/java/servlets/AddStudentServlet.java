package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

/**
 * Add Student Servlet - Handles adding new students
 * 
 * @author Shabbir Ansari
 */
@WebServlet("/addStudent")
public class AddStudentServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        System.out.println("=== AddStudentServlet: Processing add student request ===");
        
        // Check if user is admin
        HttpSession session = request.getSession(false);
        if (session == null || !"true".equals(session.getAttribute("isAdmin"))) {
            response.sendRedirect("login.html");
            return;
        }
        
        // Get form parameters
        String rollNo = request.getParameter("roll_no");
        String name = request.getParameter("name");
        String fatherName = request.getParameter("father_name");
        String dob = request.getParameter("dob");
        String address = request.getParameter("address");
        String phone = request.getParameter("phone");
        String email = request.getParameter("email");
        String aadhar = request.getParameter("aadhar");
        String course = request.getParameter("course");
        String branch = request.getParameter("branch");
        String semester = request.getParameter("semester");
        String year = request.getParameter("year");
        String gender = request.getParameter("gender");
        String category = request.getParameter("category");
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            if (db.c == null) {
                showMessage(out, "error", "Database connection failed!", "addStudent.html");
                return;
            }
            
            // Insert student
            String query = "INSERT INTO student (roll_no, name, father_name, dob, address, phone, email, " +
                          "aadhar, course, branch, semester, year, gender, category) " +
                          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
            
            PreparedStatement pst = db.c.prepareStatement(query);
            pst.setString(1, rollNo);
            pst.setString(2, name);
            pst.setString(3, fatherName);
            pst.setString(4, dob);
            pst.setString(5, address);
            pst.setString(6, phone);
            pst.setString(7, email);
            pst.setString(8, aadhar);
            pst.setString(9, course);
            pst.setString(10, branch);
            pst.setInt(11, Integer.parseInt(semester));
            pst.setInt(12, Integer.parseInt(year));
            pst.setString(13, gender);
            pst.setString(14, category);
            
            int result = pst.executeUpdate();
            
            pst.close();
            db.closeConnection();
            
            if (result > 0) {
                System.out.println("✓ Student added successfully: " + rollNo);
                showMessage(out, "success", 
                    "Student added successfully!<br>Roll No: " + rollNo + "<br>Name: " + name,
                    "addStudent.html");
            } else {
                showMessage(out, "error", "Failed to add student!", "addStudent.html");
            }
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            
            String errorMsg = "Error adding student!";
            if (e.getMessage().contains("Duplicate entry")) {
                if (e.getMessage().contains("PRIMARY")) {
                    errorMsg = "Roll Number already exists!";
                } else if (e.getMessage().contains("phone")) {
                    errorMsg = "Phone number already exists!";
                } else if (e.getMessage().contains("email")) {
                    errorMsg = "Email already exists!";
                } else if (e.getMessage().contains("aadhar")) {
                    errorMsg = "Aadhar number already exists!";
                }
            }
            showMessage(out, "error", errorMsg, "addStudent.html");
        }
    }
    
    private void showMessage(PrintWriter out, String type, String message, String backLink) {
        String bgColor = type.equals("success") ? "#27ae60" : "#e74c3c";
        String icon = type.equals("success") ? "✓" : "✗";
        
        out.println("<!DOCTYPE html>");
        out.println("<html><head>");
        out.println("<meta charset='UTF-8'>");
        out.println("<title>" + (type.equals("success") ? "Success" : "Error") + "</title>");
        out.println("<style>");
        out.println("body { font-family: Arial; display: flex; align-items: center; justify-content: center;");
        out.println("       min-height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); margin: 0; }");
        out.println(".message-box { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.2);");
        out.println("               text-align: center; max-width: 500px; }");
        out.println(".message-box h2 { color: " + bgColor + "; margin-bottom: 20px; }");
        out.println(".message-box p { color: #555; margin-bottom: 30px; line-height: 1.6; }");
        out.println(".btn { background: #667eea; color: white; padding: 12px 30px; text-decoration: none;");
        out.println("       border-radius: 8px; display: inline-block; margin: 5px; transition: background 0.3s; }");
        out.println(".btn:hover { background: #764ba2; }");
        out.println(".btn-secondary { background: #95a5a6; }");
        out.println(".btn-secondary:hover { background: #7f8c8d; }");
        out.println("</style>");
        out.println("</head><body>");
        out.println("<div class='message-box'>");
        out.println("<h2>" + icon + " " + (type.equals("success") ? "Success" : "Error") + "</h2>");
        out.println("<p>" + message + "</p>");
        out.println("<a href='" + backLink + "' class='btn'>Add Another Student</a>");
        out.println("<a href='dashboard.jsp' class='btn btn-secondary'>Back to Dashboard</a>");
        out.println("</div>");
        out.println("</body></html>");
    }
}
