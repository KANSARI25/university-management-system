package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/addFees")
public class AddFeesServlet extends HttpServlet {
    
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
        int totalFee = Integer.parseInt(request.getParameter("total_fee"));
        int paidFee = Integer.parseInt(request.getParameter("paid_fee"));
        String dueDate = request.getParameter("due_date");
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            if (db.c == null) {
                showMessage(out, "error", "Database connection failed!");
                return;
            }
            
            // Check if fee record exists
            String checkQuery = "SELECT * FROM fee WHERE roll_no=? AND semester=?";
            PreparedStatement checkPst = db.c.prepareStatement(checkQuery);
            checkPst.setString(1, rollNo);
            checkPst.setInt(2, semester);
            ResultSet rs = checkPst.executeQuery();
            
            String query;
            PreparedStatement pst;
            
            if (rs.next()) {
                // Update existing record
                query = "UPDATE fee SET total_fee=?, paid_fee=?, due_date=? " +
                       "WHERE roll_no=? AND semester=?";
                pst = db.c.prepareStatement(query);
                pst.setInt(1, totalFee);
                pst.setInt(2, paidFee);
                pst.setString(3, dueDate);
                pst.setString(4, rollNo);
                pst.setInt(5, semester);
            } else {
                // Insert new record
                query = "INSERT INTO fee (roll_no, semester, total_fee, paid_fee, due_date) " +
                       "VALUES (?, ?, ?, ?, ?)";
                pst = db.c.prepareStatement(query);
                pst.setString(1, rollNo);
                pst.setInt(2, semester);
                pst.setInt(3, totalFee);
                pst.setInt(4, paidFee);
                pst.setString(5, dueDate);
            }
            
            pst.executeUpdate();
            
            int pending = totalFee - paidFee;
            String status = paidFee >= totalFee ? "✓ Paid" : paidFee > 0 ? "⚠️ Partial" : "❌ Pending";
            
            System.out.println("✓ Fee record added: " + rollNo + " - ₹" + paidFee + "/₹" + totalFee);
            
            rs.close();
            checkPst.close();
            pst.close();
            db.closeConnection();
            
            showMessage(out, "success", String.format(
                "Fee record added successfully!<br><br>" +
                "<strong>Roll No:</strong> %s<br>" +
                "<strong>Semester:</strong> %d<br>" +
                "<strong>Total Fee:</strong> ₹%,d<br>" +
                "<strong>Paid:</strong> ₹%,d<br>" +
                "<strong>Pending:</strong> ₹%,d<br>" +
                "<strong>Status:</strong> %s<br>" +
                "<strong>Due Date:</strong> %s",
                rollNo, semester, totalFee, paidFee, pending, status, dueDate
            ));
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            showMessage(out, "error", "Error adding fee record: " + e.getMessage());
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
        out.println("p{color:#555;margin-bottom:30px;line-height:1.8;}");
        out.println(".btn{background:#667eea;color:white;padding:12px 30px;text-decoration:none;");
        out.println("border-radius:8px;display:inline-block;margin:5px;}");
        out.println("</style></head><body>");
        out.println("<div class='box'>");
        out.println("<h2>" + icon + " " + type.toUpperCase() + "</h2>");
        out.println("<p>" + message + "</p>");
        out.println("<a href='addFees.html' class='btn'>Add More Fees</a>");
        out.println("<a href='viewFees' class='btn'>View All Fees</a>");
        out.println("<a href='dashboard.jsp' class='btn'>Dashboard</a>");
        out.println("</div></body></html>");
    }
}
