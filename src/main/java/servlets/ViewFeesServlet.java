package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/viewFees")
public class ViewFeesServlet extends HttpServlet {
    
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
        out.println("<meta charset='UTF-8'><title>View Fees - UMS</title>");
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
        out.println(".paid{color:#27ae60;font-weight:bold;}.pending{color:#e74c3c;font-weight:bold;}");
        out.println(".partial{color:#f39c12;font-weight:bold;}");
        out.println(".btn{padding:10px 20px;background:#667eea;color:white;text-decoration:none;border-radius:8px;}");
        out.println("</style></head><body>");
        
        out.println("<div class='header'>");
        out.println("<h1>💰 View Fee Records</h1>");
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
            
            String query = "SELECT f.*, s.name FROM fee f " +
                          "JOIN student s ON f.roll_no = s.roll_no " +
                          "ORDER BY f.roll_no, f.semester";
            ResultSet rs = db.s.executeQuery(query);
            
            // Count total fee records
            String countQuery = "SELECT COUNT(*) as total FROM fee";
            ResultSet countRs = db.c.createStatement().executeQuery(countQuery);
            int totalRecords = 0;
            if (countRs.next()) {
                totalRecords = countRs.getInt("total");
            }
            countRs.close();
            
            out.println("<h2>Total Fee Records: " + totalRecords + "</h2>");
            
            out.println("<div style='overflow-x:auto;'>");
            out.println("<table><thead><tr>");
            out.println("<th>Roll No</th><th>Name</th><th>Semester</th><th>Total Fee</th>");
            out.println("<th>Paid</th><th>Pending</th><th>Status</th><th>Due Date</th>");
            out.println("</tr></thead><tbody>");
            
            while (rs.next()) {
                int totalFee = rs.getInt("total_fee");
                int paidFee = rs.getInt("paid_fee");
                int pendingFee = totalFee - paidFee;
                
                String status;
                String statusClass;
                
                if (paidFee >= totalFee) {
                    status = "Paid";
                    statusClass = "paid";
                } else if (paidFee > 0) {
                    status = "Partial";
                    statusClass = "partial";
                } else {
                    status = "Pending";
                    statusClass = "pending";
                }
                
                out.println("<tr>");
                out.println("<td><strong>" + rs.getString("roll_no") + "</strong></td>");
                out.println("<td>" + rs.getString("name") + "</td>");
                out.println("<td>" + rs.getInt("semester") + "</td>");
                out.println("<td>₹" + totalFee + "</td>");
                out.println("<td>₹" + paidFee + "</td>");
                out.println("<td>₹" + pendingFee + "</td>");
                out.println("<td class='" + statusClass + "'>" + status + "</td>");
                out.println("<td>" + rs.getDate("due_date") + "</td>");
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
