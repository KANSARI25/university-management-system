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
        
        System.out.println("=== AddTeacherServlet: Processing request ===");
        
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
            
            if (db.c == null) {
                showMessage(out, "error", "Database connection failed!");
                return;
            }
            
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
            
            System.out.println("✓ Teacher added successfully: " + empId);
            
            pst.close();
            db.closeConnection();
            
            showMessage(out, "success", "Teacher added successfully!<br>Emp ID: " + empId + "<br>Name: " + name);
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            showMessage(out, "error", "Error adding teacher: " + e.getMessage());
        }
    }
    
    private void showMessage(PrintWriter out, String type, String message) {
        String bgColor = type.equals("success") ? "#27ae60" : "#e74c3c";
        String icon = type.equals("success") ? "✓" : "✗";
        
        out.println("<!DOCTYPE html><html><head>");
        out.println("<meta charset='UTF-8'><title>" + type + "</title>");
        out.println("<style>");
        out.println("body{font-family:Arial;display:flex;align-items:center;justify-content:center;");
        out.println("min-height:100vh;background:linear-gradient(135deg,#667eea,#764ba2);}");
        out.println(".box{background:white;padding:40px;border-radius:20px;text-align:center;max-width:500px;}");
        out.println("h2{color:" + bgColor + ";margin-bottom:20px;}");
        out.println("p{color:#555;margin-bottom:30px;line-height:1.6;}");
        out.println(".btn{background:#667eea;color:white;padding:12px 30px;text-decoration:none;");
        out.println("border-radius:8px;display:inline-block;margin:5px;transition:background 0.3s;}");
        out.println(".btn:hover{background:#764ba2;}");
        out.println("</style></head><body>");
        out.println("<div class='box'>");
        out.println("<h2>" + icon + " " + type.toUpperCase() + "</h2>");
        out.println("<p>" + message + "</p>");
        out.println("<a href='addTeacher.html' class='btn'>Add Another Teacher</a>");
        out.println("<a href='viewTeachers' class='btn'>View All Teachers</a>");
        out.println("<a href='dashboard.jsp' class='btn'>Dashboard</a>");
        out.println("</div></body></html>");
    }
}
