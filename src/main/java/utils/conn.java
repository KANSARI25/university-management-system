package utils;

import java.sql.*;

/**
 * Database Connection Utility Class
 * Handles MySQL database connectivity for University Management System
 * 
 * @author Shabbir Ansari
 * @version 1.0
 */
public class conn {
    
    public Connection c;
    public Statement s;
    
    /**
     * Constructor - Establishes database connection
     * Update the credentials below with your MySQL details
     */
    public conn() {
        try {
            // Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // ========================================
            // DATABASE CONFIGURATION
            // ========================================
            // For Clever Cloud (Update with your details)
            String host = "your-clever-cloud-host.mysql.clever-cloud.com";
            String port = "3306";
            String database = "ums_db";
            String username = "your-username";
            String password = "your-password";
            
            // For Local MySQL (Uncomment below and comment above if using local)
            /*
            String host = "localhost";
            String port = "3306";
            String database = "ums_db";
            String username = "root";
            String password = "your-mysql-password";
            */
            
            // Build connection URL
            String url = "jdbc:mysql://" + host + ":" + port + "/" + database;
            url += "?useSSL=true&allowPublicKeyRetrieval=true";
            url += "&serverTimezone=UTC&autoReconnect=true";
            
            // Establish connection
            c = DriverManager.getConnection(url, username, password);
            s = c.createStatement();
            
            System.out.println("✓ Database connected successfully!");
            
        } catch (ClassNotFoundException e) {
            System.err.println("❌ MySQL Driver not found!");
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
            
        } catch (SQLException e) {
            System.err.println("❌ Database connection failed!");
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Close database connection and statement
     */
    public void closeConnection() {
        try {
            if (s != null && !s.isClosed()) {
                s.close();
            }
            if (c != null && !c.isClosed()) {
                c.close();
            }
            System.out.println("✓ Database connection closed");
        } catch (SQLException e) {
            System.err.println("❌ Error closing connection: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Test the database connection
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Testing Database Connection...");
        System.out.println("================================");
        
        conn db = new conn();
        
        if (db.c != null) {
            System.out.println("✓ Connection successful!");
            
            // Test query
            try {
                ResultSet rs = db.s.executeQuery("SELECT COUNT(*) as count FROM student");
                if (rs.next()) {
                    System.out.println("✓ Total students in database: " + rs.getInt("count"));
                }
                rs.close();
            } catch (SQLException e) {
                System.err.println("❌ Error executing test query: " + e.getMessage());
            }
            
            db.closeConnection();
        } else {
            System.out.println("❌ Connection failed!");
        }
    }
}
