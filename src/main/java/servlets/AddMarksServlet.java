package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/addMarks")
public class AddMarksServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        HttpSession session = request.getSession(false);
        if (session == null || !"true".equals(session.getAttribute("isAdmin"))) {
            response.sendRedirect("login.html");
            return;
        }
        
        String rollNo = request.getParameter("roll_no");
        String subjectCode = request.getParameter("subject_code");
        int semester = Integer.parseInt(request.getParameter("semester"));
        int internalMarks = Integer.parseInt(request.getParameter("internal_marks"));
        int externalMarks = Integer.parseInt(request.getParameter("external_marks"));
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            if (db.c == null) {
                showMessage(out, "error", "Database connection failed!");
                return;
            }
            
            // Check if marks record already exists
            String checkQuery = "SELECT * FROM marks WHERE roll_no=? AND subject_code=? AND semester=?";
            PreparedStatement checkPst = db.c.prepareStatement(checkQuery);
            checkPst.setString(1, rollNo);
            checkPst.setString(2, subjectCode);
            checkPst.setInt(3, semester);
            ResultSet rs = checkPst.executeQuery();
            
            String query;
            PreparedStatement pst;
            
            if (rs.next()) {
                // Update existing record
                query = "UPDATE marks SET internal_marks=?, external_marks=? " +
                       "WHERE roll_no=? AND subject_code=? AND semester=?";
                pst = db.c.prepareStatement(query);
                pst.setInt(1, internalMarks);
                pst.setInt(2, externalMarks);
                pst.setString(3, rollNo);
                pst.setString(4, subjectCode);
                pst.setInt(5, semester);
            } else {
                // Insert new record
                query = "INSERT INTO marks (roll_no, subject_code, semester, internal_marks, external_marks) " +
                       "VALUES (?, ?, ?, ?, ?)";
                pst = db.c.prepareStatement(query);
                pst.setString(1, rollNo);
                pst.setString(2, subjectCode);
                pst.setInt(3, semester);
                pst.setInt(4, internalMarks);
                pst.setInt(5, externalMarks);
            }
            
            pst.executeUpdate();
            
            int total = internalMarks + externalMarks;
            String grade = total >= 85 ? "A" : total >= 70 ? "B" : total >= 55 ? "C" : total >= 40 ? "D" : "F";
            
            rs.close();
            checkPst.close();
            pst.close();
            db.closeConnection();
            
            showMessage(out, "success", 
                String.format("Marks added successfully!<br>Roll No: %s<br>Subject: %s<br>" +
                             "Internal: %d | External: %d<br>Total: %d | Grade: %s",
                             rollNo, subjectCode, internalMarks, externalMarks, total, grade));
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            showMessage(out, "error", "Error adding marks: " + e.getMessage());
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
        out.println("border-radius:8px;display:inline-block;margin:5px;}");
        out.println("</style></head><body>");
        out.println("<div class='box'>");
        out.println("<h2>" + icon + " " + type.toUpperCase() + "</h2>");
        out.println("<p>" + message + "</p>");
        out.println("<a href='addMarks.html' class='btn'>Add More Marks</a>");
        out.println("<a href='viewMarks' class='btn'>View All Marks</a>");
        out.println("<a href='dashboard.jsp' class='btn'>Dashboard</a>");
        out.println("</div></body></html>");
    }
}
