package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

/**
 * Update Student Servlet - Handles updating student information
 * 
 * @author Shabbir Ansari
 */
@WebServlet("/updateStudent")
public class UpdateStudentServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        System.out.println("=== UpdateStudentServlet: Processing update request ===");
        
        HttpSession session = request.getSession(false);
        if (session == null || !"true".equals(session.getAttribute("isAdmin"))) {
            response.sendRedirect("login.html");
            return;
        }
        
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
        String status = request.getParameter("status");
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            if (db.c == null) {
                showMessage(out, "error", "Database connection failed!", "updateStudent.html");
                return;
            }
            
            String query = "UPDATE student SET name=?, father_name=?, dob=?, address=?, phone=?, " +
                          "email=?, aadhar=?, course=?, branch=?, semester=?, year=?, gender=?, " +
                          "category=?, status=? WHERE roll_no=?";
            
            PreparedStatement pst = db.c.prepareStatement(query);
            pst.setString(1, name);
            pst.setString(2, fatherName);
            pst.setString(3, dob);
            pst.setString(4, address);
            pst.setString(5, phone);
            pst.setString(6, email);
            pst.setString(7, aadhar);
            pst.setString(8, course);
            pst.setString(9, branch);
            pst.setInt(10, Integer.parseInt(semester));
            pst.setInt(11, Integer.parseInt(year));
            pst.setString(12, gender);
            pst.setString(13, category);
            pst.setString(14, status);
            pst.setString(15, rollNo);
            
            int result = pst.executeUpdate();
            
            pst.close();
            db.closeConnection();
            
            if (result > 0) {
                System.out.println("✓ Student updated successfully: " + rollNo);
                showMessage(out, "success", 
                    "Student updated successfully!<br>Roll No: " + rollNo + "<br>Name: " + name,
                    "updateStudent.html");
            } else {
                showMessage(out, "error", "No student found with Roll No: " + rollNo, "updateStudent.html");
            }
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            showMessage(out, "error", "Error updating student: " + e.getMessage(), "updateStudent.html");
        }
    }
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        String rollNo = request.getParameter("roll_no");
        
        if (rollNo == null || rollNo.trim().isEmpty()) {
            response.sendRedirect("updateStudent.html");
            return;
        }
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            String query = "SELECT * FROM student WHERE roll_no=?";
            PreparedStatement pst = db.c.prepareStatement(query);
            pst.setString(1, rollNo);
            ResultSet rs = pst.executeQuery();
            
            if (rs.next()) {
                // Return student data as JSON
                response.setContentType("application/json");
                out.println("{");
                out.println("\"success\": true,");
                out.println("\"roll_no\": \"" + rs.getString("roll_no") + "\",");
                out.println("\"name\": \"" + rs.getString("name") + "\",");
                out.println("\"father_name\": \"" + rs.getString("father_name") + "\",");
                out.println("\"dob\": \"" + rs.getString("dob") + "\",");
                out.println("\"address\": \"" + rs.getString("address") + "\",");
                out.println("\"phone\": \"" + rs.getString("phone") + "\",");
                out.println("\"email\": \"" + rs.getString("email") + "\",");
                out.println("\"aadhar\": \"" + rs.getString("aadhar") + "\",");
                out.println("\"course\": \"" + rs.getString("course") + "\",");
                out.println("\"branch\": \"" + rs.getString("branch") + "\",");
                out.println("\"semester\": " + rs.getInt("semester") + ",");
                out.println("\"year\": " + rs.getInt("year") + ",");
                out.println("\"gender\": \"" + rs.getString("gender") + "\",");
                out.println("\"category\": \"" + rs.getString("category") + "\",");
                out.println("\"status\": \"" + rs.getString("status") + "\"");
                out.println("}");
            } else {
                response.setContentType("application/json");
                out.println("{\"success\": false, \"message\": \"Student not found\"}");
            }
            
            rs.close();
            pst.close();
            db.closeConnection();
            
        } catch (SQLException e) {
            response.setContentType("application/json");
            out.println("{\"success\": false, \"message\": \"" + e.getMessage() + "\"}");
        }
    }
    
    private void showMessage(PrintWriter out, String type, String message, String backLink) {
        String bgColor = type.equals("success") ? "#27ae60" : "#e74c3c";
        String icon = type.equals("success") ? "✓" : "✗";
        
        out.println("<!DOCTYPE html><html><head>");
        out.println("<meta charset='UTF-8'><title>" + (type.equals("success") ? "Success" : "Error") + "</title>");
        out.println("<style>");
        out.println("body{font-family:Arial;display:flex;align-items:center;justify-content:center;");
        out.println("min-height:100vh;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);margin:0;}");
        out.println(".message-box{background:white;padding:40px;border-radius:20px;");
        out.println("box-shadow:0 10px 40px rgba(0,0,0,0.2);text-align:center;max-width:500px;}");
        out.println(".message-box h2{color:" + bgColor + ";margin-bottom:20px;}");
        out.println(".message-box p{color:#555;margin-bottom:30px;line-height:1.6;}");
        out.println(".btn{background:#667eea;color:white;padding:12px 30px;text-decoration:none;");
        out.println("border-radius:8px;display:inline-block;margin:5px;transition:background 0.3s;}");
        out.println(".btn:hover{background:#764ba2;}");
        out.println(".btn-secondary{background:#95a5a6;}.btn-secondary:hover{background:#7f8c8d;}");
        out.println("</style></head><body>");
        out.println("<div class='message-box'>");
        out.println("<h2>" + icon + " " + (type.equals("success") ? "Success" : "Error") + "</h2>");
        out.println("<p>" + message + "</p>");
        out.println("<a href='" + backLink + "' class='btn'>Update Another</a>");
        out.println("<a href='dashboard.jsp' class='btn btn-secondary'>Dashboard</a>");
        out.println("</div></body></html>");
    }
}
