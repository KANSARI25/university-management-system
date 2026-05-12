package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;
import java.sql.*;
import utils.conn;

/**
 * Login Servlet - Handles user authentication
 * 
 * @author Shabbir Ansari
 */
@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        System.out.println("=== LoginServlet: Processing login request ===");
        
        // Get form parameters
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        
        System.out.println("Username: " + username);
        System.out.println("Password: " + (password != null ? "******" : "null"));
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            // Connect to database
            conn db = new conn();
            
            if (db.c == null) {
                System.out.println("❌ Database connection failed");
                showError(out, "Database connection failed. Please try again later.");
                return;
            }
            
            System.out.println("✓ Database connected");
            
            // Query to check credentials
            String query = "SELECT * FROM account WHERE username=? AND password=?";
            PreparedStatement pst = db.c.prepareStatement(query);
            pst.setString(1, username);
            pst.setString(2, password);
            
            ResultSet rs = pst.executeQuery();
            
            if (rs.next()) {
                // Login successful
                System.out.println("✓ Login successful for: " + username);
                
                // Create session
                HttpSession session = request.getSession(true);
                session.setAttribute("username", username);
                session.setAttribute("name", rs.getString("name"));
                
                // Set role attributes
                String role = rs.getString("role");
                boolean isAdmin = "admin".equalsIgnoreCase(role);
                
                session.setAttribute("isAdmin", isAdmin ? "true" : "false");
                session.setAttribute("role", isAdmin ? "admin" : "user");
                
                // Set session timeout (30 minutes)
                session.setMaxInactiveInterval(30 * 60);
                
                System.out.println("Session created - ID: " + session.getId());
                System.out.println("User role: " + role);
                
                // Close resources
                rs.close();
                pst.close();
                db.closeConnection();
                
                // Redirect to dashboard
                response.sendRedirect("dashboard.jsp");
                
            } else {
                // Login failed
                System.out.println("❌ Login failed - Invalid credentials");
                
                rs.close();
                pst.close();
                db.closeConnection();
                
                showError(out, "Invalid username or password!");
            }
            
        } catch (SQLException e) {
            System.err.println("❌ SQL Error: " + e.getMessage());
            e.printStackTrace();
            showError(out, "An error occurred. Please try again.");
        }
    }
    
    /**
     * Display error message with styling
     */
    private void showError(PrintWriter out, String message) {
        out.println("<!DOCTYPE html>");
        out.println("<html lang='en'>");
        out.println("<head>");
        out.println("    <meta charset='UTF-8'>");
        out.println("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>");
        out.println("    <title>Login Error</title>");
        out.println("    <style>");
        out.println("        body {");
        out.println("            font-family: Arial, sans-serif;");
        out.println("            display: flex;");
        out.println("            align-items: center;");
        out.println("            justify-content: center;");
        out.println("            min-height: 100vh;");
        out.println("            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);");
        out.println("            margin: 0;");
        out.println("        }");
        out.println("        .error-box {");
        out.println("            background: white;");
        out.println("            padding: 40px;");
        out.println("            border-radius: 20px;");
        out.println("            box-shadow: 0 10px 40px rgba(0,0,0,0.2);");
        out.println("            text-align: center;");
        out.println("            max-width: 400px;");
        out.println("        }");
        out.println("        .error-box h2 {");
        out.println("            color: #e74c3c;");
        out.println("            margin-bottom: 20px;");
        out.println("        }");
        out.println("        .error-box p {");
        out.println("            color: #555;");
        out.println("            margin-bottom: 30px;");
        out.println("        }");
        out.println("        .btn {");
        out.println("            background: #667eea;");
        out.println("            color: white;");
        out.println("            padding: 12px 30px;");
        out.println("            text-decoration: none;");
        out.println("            border-radius: 8px;");
        out.println("            display: inline-block;");
        out.println("            transition: background 0.3s;");
        out.println("        }");
        out.println("        .btn:hover {");
        out.println("            background: #764ba2;");
        out.println("        }");
        out.println("    </style>");
        out.println("</head>");
        out.println("<body>");
        out.println("    <div class='error-box'>");
        out.println("        <h2>❌ Login Failed</h2>");
        out.println("        <p>" + message + "</p>");
        out.println("        <a href='login.html' class='btn'>Try Again</a>");
        out.println("    </div>");
        out.println("</body>");
        out.println("</html>");
    }
}
