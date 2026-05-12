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
            
            if (db.c == null) {
                out.println("<h3 style='color: #e74c3c;'>❌ Database connection failed!</h3>");
                out.println("</div></div></body></html>");
                return;
            }
            
            String query = "SELECT * FROM teacher ORDER BY emp_id";
            ResultSet rs = db.s.executeQuery(query);
            
            // Count total teachers
            String countQuery = "SELECT COUNT(*) as total FROM teacher";
            ResultSet countRs = db.c.createStatement().executeQuery(countQuery);
            int totalTeachers = 0;
            if (countRs.next()) {
                totalTeachers = countRs.getInt("total");
            }
            countRs.close();
            
            out.println("<h2>Total Teachers: " + totalTeachers + "</h2>");
            
            out.println("<table><thead><tr>");
            out.println("<th>Emp ID</th><th>Name</th><th>Qualification</th><th>Department</th>");
            out.println("<th>Designation</th><th>Phone</th><th>Email</th><th>Status</th>");
            out.println("</tr></thead><tbody>");
            
            while (rs.next()) {
                out.println("<tr>");
                out.println("<td><strong>" + rs.getString("emp_id") + "</strong></td>");
                out.println("<td>" + rs.getString("name") + "</td>");
                out.println("<td>" + rs.getString("qualification") + "</td>");
                out.println("<td>" + rs.getString("department") + "</td>");
                out.println("<td>" + rs.getString("designation") + "</td>");
                out.println("<td>" + rs.getString("phone") + "</td>");
                out.println("<td>" + rs.getString("email") + "</td>");
                
                String status = rs.getString("status");
                String statusClass = "Active".equals(status) ? "color:#27ae60;" : "color:#e74c3c;";
                out.println("<td style='" + statusClass + "font-weight:bold;'>" + status + "</td>");
                
                out.println("</tr>");
            }
            
            out.println("</tbody></table>");
            rs.close();
            db.closeConnection();
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            out.println("<h3 style='color:#e74c3c;'>❌ Error: " + e.getMessage() + "</h3>");
        }
        
        out.println("</div></div></body></html>");
    }
}
