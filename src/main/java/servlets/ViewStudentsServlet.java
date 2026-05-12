package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

/**
 * View Students Servlet - Displays all students
 * 
 * @author Shabbir Ansari
 */
@WebServlet("/viewStudents")
public class ViewStudentsServlet extends HttpServlet {
    
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
        
        out.println("<!DOCTYPE html>");
        out.println("<html><head>");
        out.println("<meta charset='UTF-8'>");
        out.println("<meta name='viewport' content='width=device-width, initial-scale=1.0'>");
        out.println("<title>View Students - UMS</title>");
        out.println("<link rel='stylesheet' href='css/style.css'>");
        out.println("<style>");
        out.println("body { font-family: Arial; background: #f5f7fa; margin: 0; }");
        out.println(".header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;");
        out.println("          padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }");
        out.println(".container { max-width: 1400px; margin: 20px auto; padding: 0 20px; }");
        out.println(".card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }");
        out.println("table { width: 100%; border-collapse: collapse; margin-top: 20px; }");
        out.println("th { background: #667eea; color: white; padding: 12px; text-align: left; }");
        out.println("td { padding: 12px; border-bottom: 1px solid #e0e0e0; }");
        out.println("tr:hover { background: #f8f9fa; }");
        out.println(".btn { padding: 10px 20px; background: #667eea; color: white; text-decoration: none;");
        out.println("       border-radius: 8px; display: inline-block; margin: 5px; }");
        out.println(".btn:hover { background: #764ba2; }");
        out.println(".status-active { color: #27ae60; font-weight: bold; }");
        out.println(".status-inactive { color: #e74c3c; font-weight: bold; }");
        out.println("</style>");
        out.println("</head><body>");
        
        out.println("<div class='header'>");
        out.println("<h1>📚 View All Students</h1>");
        out.println("<a href='dashboard.jsp' class='btn'>← Back to Dashboard</a>");
        out.println("</div>");
        
        out.println("<div class='container'>");
        out.println("<div class='card'>");
        
        try {
            conn db = new conn();
            
            if (db.c == null) {
                out.println("<h3 style='color: #e74c3c;'>❌ Database connection failed!</h3>");
                out.println("</div></div></body></html>");
                return;
            }
            
            String query = "SELECT * FROM student ORDER BY roll_no";
            ResultSet rs = db.s.executeQuery(query);
            
            // Count total students
            String countQuery = "SELECT COUNT(*) as total FROM student";
            ResultSet countRs = db.c.createStatement().executeQuery(countQuery);
            int totalStudents = 0;
            if (countRs.next()) {
                totalStudents = countRs.getInt("total");
            }
            countRs.close();
            
            out.println("<h2>Total Students: " + totalStudents + "</h2>");
            
            if (totalStudents == 0) {
                out.println("<p style='text-align: center; color: #666; padding: 40px;'>");
                out.println("No students found. <a href='addStudent.html'>Add your first student</a></p>");
            } else {
                out.println("<div style='overflow-x: auto;'>");
                out.println("<table>");
                out.println("<thead><tr>");
                out.println("<th>Roll No</th><th>Name</th><th>Father's Name</th><th>Course</th>");
                out.println("<th>Branch</th><th>Semester</th><th>Phone</th><th>Email</th><th>Status</th>");
                out.println("</tr></thead>");
                out.println("<tbody>");
                
                while (rs.next()) {
                    out.println("<tr>");
                    out.println("<td><strong>" + rs.getString("roll_no") + "</strong></td>");
                    out.println("<td>" + rs.getString("name") + "</td>");
                    out.println("<td>" + rs.getString("father_name") + "</td>");
                    out.println("<td>" + rs.getString("course") + "</td>");
                    out.println("<td>" + rs.getString("branch") + "</td>");
                    out.println("<td>" + rs.getInt("semester") + "</td>");
                    out.println("<td>" + rs.getString("phone") + "</td>");
                    out.println("<td>" + rs.getString("email") + "</td>");
                    
                    String status = rs.getString("status");
                    String statusClass = "Active".equals(status) ? "status-active" : "status-inactive";
                    out.println("<td class='" + statusClass + "'>" + status + "</td>");
                    
                    out.println("</tr>");
                }
                
                out.println("</tbody>");
                out.println("</table>");
                out.println("</div>");
            }
            
            rs.close();
            db.closeConnection();
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            out.println("<h3 style='color: #e74c3c;'>❌ Error loading students: " + e.getMessage() + "</h3>");
        }
        
        out.println("</div></div>");
        out.println("</body></html>");
    }
}
