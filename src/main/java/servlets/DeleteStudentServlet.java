package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/deleteStudent")
public class DeleteStudentServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        HttpSession session = request.getSession(false);
        if (session == null || !"true".equals(session.getAttribute("isAdmin"))) {
            response.sendRedirect("login.html");
            return;
        }
        
        String rollNo = request.getParameter("roll_no");
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            // Delete student (cascade will delete related records)
            String query = "DELETE FROM student WHERE roll_no=?";
            PreparedStatement pst = db.c.prepareStatement(query);
            pst.setString(1, rollNo);
            
            int result = pst.executeUpdate();
            
            pst.close();
            db.closeConnection();
            
            if (result > 0) {
                showMessage(out, "success", "Student deleted successfully!<br>Roll No: " + rollNo);
            } else {
                showMessage(out, "error", "No student found with Roll No: " + rollNo);
            }
            
        } catch (SQLException e) {
            showMessage(out, "error", "Error deleting student: " + e.getMessage());
        }
    }
    
    private void showMessage(PrintWriter out, String type, String message) {
        String bgColor = type.equals("success") ? "#27ae60" : "#e74c3c";
        String icon = type.equals("success") ? "✓" : "✗";
        
        out.println("<!DOCTYPE html><html><head>");
        out.println("<meta charset='UTF-8'><title>" + type + "</title>");
        out.println("<style>");
        out.println("body{font-family:Arial;display:flex;align-items:center;justify-content:center;");
        out.println("min-height:100vh;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);}");
        out.println(".box{background:white;padding:40px;border-radius:20px;text-align:center;max-width:500px;}");
        out.println("h2{color:" + bgColor + ";margin-bottom:20px;}");
        out.println(".btn{background:#667eea;color:white;padding:12px 30px;text-decoration:none;");
        out.println("border-radius:8px;display:inline-block;margin:5px;}");
        out.println("</style></head><body>");
        out.println("<div class='box'>");
        out.println("<h2>" + icon + " " + type.toUpperCase() + "</h2>");
        out.println("<p>" + message + "</p>");
        out.println("<a href='deleteStudent.html' class='btn'>Delete Another</a>");
        out.println("<a href='dashboard.jsp' class='btn'>Dashboard</a>");
        out.println("</div></body></html>");
    }
}
