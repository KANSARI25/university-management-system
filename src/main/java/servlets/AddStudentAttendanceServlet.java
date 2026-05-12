package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

@WebServlet("/addStudentAttendance")
public class AddStudentAttendanceServlet extends HttpServlet {
    
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
        int totalClasses = Integer.parseInt(request.getParameter("total_classes"));
        int attendedClasses = Integer.parseInt(request.getParameter("attended_classes"));
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            conn db = new conn();
            
            if (db.c == null) {
                showMessage(out, "error", "Database connection failed!");
                return;
            }
            
            // Check if attendance record exists
            String checkQuery = "SELECT * FROM attendance_student WHERE roll_no=? AND semester=?";
            PreparedStatement checkPst = db.c.prepareStatement(checkQuery);
            checkPst.setString(1, rollNo);
            checkPst.setInt(2, semester);
            ResultSet rs = checkPst.executeQuery();
            
            String query;
            PreparedStatement pst;
            
            if (rs.next()) {
                // Update existing record
                query = "UPDATE attendance_student SET total_classes=?, attended_classes=? " +
                       "WHERE roll_no=? AND semester=?";
                pst = db.c.prepareStatement(query);
                pst.setInt(1, totalClasses);
                pst.setInt(2, attendedClasses);
                pst.setString(3, rollNo);
                pst.setInt(4, semester);
            } else {
                // Insert new record
                query = "INSERT INTO attendance_student (roll_no, semester, total_classes, attended_classes) " +
                       "VALUES (?, ?, ?, ?)";
                pst = db.c.prepareStatement(query);
                pst.setString(1, rollNo);
                pst.setInt(2, semester);
                pst.setInt(3, totalClasses);
                pst.setInt(4, attendedClasses);
            }
            
            pst.executeUpdate();
            
            double percentage = (totalClasses > 0) ? (attendedClasses * 100.0 / totalClasses) : 0;
            String status = percentage >= 75 ? "✓ Good" : percentage >= 60 ? "⚠️ Warning" : "❌ Critical";
            
            System.out.println("✓ Attendance marked: " + rollNo + " - " + percentage + "%");
            
            rs.close();
            checkPst.close();
            pst.close();
            db.closeConnection();
            
            showMessage(out, "success", String.format(
                "Attendance recorded successfully!<br><br>" +
                "<strong>Roll No:</strong> %s<br>" +
                "<strong>Semester:</strong> %d<br>" +
                "<strong>Attended:</strong> %d/%d classes<br>" +
                "<strong>Percentage:</strong> %.2f%%<br>" +
                "<strong>Status:</strong> %s",
                rollNo, semester, attendedClasses, totalClasses, percentage, status
            ));
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            showMessage(out, "error", "Error recording attendance: " + e.getMessage());
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
        out.println("<a href='addStudentAttendance.html' class='btn'>Mark Another</a>");
        out.println("<a href='dashboard.jsp' class='btn'>Dashboard</a>");
        out.println("</div></body></html>");
    }
}
