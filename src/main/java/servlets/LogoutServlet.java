package servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.IOException;

/**
 * Logout Servlet - Handles user logout
 * 
 * @author Shabbir Ansari
 */
@WebServlet("/logout")
public class LogoutServlet extends HttpServlet {
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        System.out.println("=== LogoutServlet: Processing logout request ===");
        
        // Get current session
        HttpSession session = request.getSession(false);
        
        if (session != null) {
            String username = (String) session.getAttribute("username");
            System.out.println("Logging out user: " + username);
            
            // Invalidate session
            session.invalidate();
            System.out.println("✓ Session invalidated");
        }
        
        // Redirect to login page
        response.sendRedirect("login.html");
    }
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}
