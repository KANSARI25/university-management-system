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
        out.println(".header{background:linear-gradient(135deg,#667eea,#764ba2);color:white;");
        out.println("padding:20px 40px;display:flex;justify-content:space-between;align-items:center;}");
        out.println(".container{max-width:1400px;margin:20px auto;padding:0 20px;}");
        out.println(".card{background:white;padding:30px;border-radius:15px;box-shadow:0 2px 10px rgba(0,0,0,0.1);}");
        out.println("table{width:100%;border-collapse:collapse;margin-top:20px;}");
        out.println("th{background:#667eea;color:white;padding:12px;text-align:left;}");
        out.println("td{padding:12px;border-bottom:1px solid #e0e0e0;}");
        out.println("tr:hover{background:#f8f9fa;}");
        out.println(".grade-A{background:#d4edda;color:#155724;padding:5px 10px;border-radius:5px;font-weight:bold;}");
        out.println(".grade-B{background:#cfe2ff;color:#084298;padding:5px 10px;border-radius:5px;font-weight:bold;}");
        out.println(".grade-C{background:#fff3cd;color:#664d03;padding:5px 10px;border-radius:5px;font-weight:bold;}");
        out.println(".grade-D{background:#f8d7da;color:#842029;padding:5px 10px;border-radius:5px;font-weight:bold;}");
        out.println(".grade-F{background:#f8d7da;color:#842029;padding:5px 10px;border-radius:5px;font-weight:bold;}");
        out.println(".btn{padding:10px 20px;background:#667eea;color:white;text-decoration:none;border-radius:8px;}");
        out.println("</style></head><body>");
        
        out.println("<div class='header'>");
        out.println("<h1>📊 View Marks</h1>");
        out.println("<a href='dashboard.jsp' class='btn'>← Back</a>");
        out.println("</div>");
        
        out.println("<div class='container'><div class='card'>");
        
        try {
            conn db = new conn();
            
            if (db.c == null) {
                out.println("<h3 style='color:#e74c3c;'>❌ Database connection failed!</h3>");
                out.println("</div></div></body></html>");
                return;
            }
            
            String query = "SELECT m.*, s.name FROM marks m " +
                          "JOIN student s ON m.roll_no = s.roll_no " +
                          "ORDER BY m.roll_no, m.semester, m.subject_code";
            ResultSet rs = db.s.executeQuery(query);
            
            // Count total marks records
            String countQuery = "SELECT COUNT(*) as total FROM marks";
            ResultSet countRs = db.c.createStatement().executeQuery(countQuery);
            int totalRecords = 0;
            if (countRs.next()) {
                totalRecords = countRs.getInt("total");
            }
            countRs.close();
            
            out.println("<h2>Total Marks Records: " + totalRecords + "</h2>");
            
            out.println("<div style='overflow-x:auto;'>");
            out.println("<table><thead><tr>");
            out.println("<th>Roll No</th><th>Name</th><th>Subject</th><th>Semester</th>");
            out.println("<th>Internal</th><th>External</th><th>Total</th><th>Grade</th>");
            out.println("</tr></thead><tbody>");
            
            while (rs.next()) {
                int internal = rs.getInt("internal_marks");
                int external = rs.getInt("external_marks");
                int total = internal + external;
                String grade;
                String gradeClass;
                
                if (total >= 85) {
                    grade = "A";
                    gradeClass = "grade-A";
                } else if (total >= 70) {
                    grade = "B";
                    gradeClass = "grade-B";
                } else if (total >= 55) {
                    grade = "C";
                    gradeClass = "grade-C";
                } else if (total >= 40) {
                    grade = "D";
                    gradeClass = "grade-D";
                } else {
                    grade = "F";
                    gradeClass = "grade-F";
                }
                
                out.println("<tr>");
                out.println("<td><strong>" + rs.getString("roll_no") + "</strong></td>");
                out.println("<td>" + rs.getString("name") + "</td>");
                out.println("<td>" + rs.getString("subject_code") + "</td>");
                out.println("<td>" + rs.getInt("semester") + "</td>");
                out.println("<td>" + internal + "</td>");
                out.println("<td>" + external + "</td>");
                out.println("<td><strong>" + total + "</strong></td>");
                out.println("<td><span class='" + gradeClass + "'>" + grade + "</span></td>");
                out.println("</tr>");
            }
            
            out.println("</tbody></table>");
            out.println("</div>");
            
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
