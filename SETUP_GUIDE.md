# 🚀 SETUP GUIDE - University Management System

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software:
- ✅ **Java JDK 8 or higher** - [Download](https://www.oracle.com/java/technologies/downloads/)
- ✅ **MySQL 5.7 or higher** - [Download](https://dev.mysql.com/downloads/mysql/)
- ✅ **Apache Tomcat 9.0 or higher** - [Download](https://tomcat.apache.org/download-90.cgi)
- ✅ **Any IDE** (Eclipse, IntelliJ IDEA, NetBeans, or VS Code)

### Alternative (Cloud-Based):
- ✅ **Replit Account** - [Sign up](https://replit.com)
- ✅ **Clever Cloud Account** - [Sign up](https://www.clever-cloud.com)

---

## 🛠️ OPTION 1: Local Setup (Recommended for Development)

### Step 1: Install MySQL

1. Download and install MySQL
2. During installation, set a root password (remember this!)
3. Start MySQL service

**For Windows:**
```cmd
net start MySQL80
```

**For Mac:**
```bash
mysql.server start
```

**For Linux:**
```bash
sudo systemctl start mysql
```

### Step 2: Create Database

1. Open MySQL Command Line or MySQL Workbench
2. Login with root user:
```bash
mysql -u root -p
```

3. Run the schema script:
```sql
source /path/to/database/schema.sql
```

Or manually:
```sql
-- Copy and paste the content from database/schema.sql
```

4. Load sample data:
```sql
source /path/to/database/sample_data.sql
```

5. Verify database:
```sql
USE ums_db;
SHOW TABLES;
SELECT * FROM account;
```

### Step 3: Configure Database Connection

Edit `src/main/java/utils/conn.java`:

```java
// For Local MySQL
String host = "localhost";
String port = "3306";
String database = "ums_db";
String username = "root";
String password = "your-mysql-password"; // Your MySQL root password
```

### Step 4: Add MySQL Connector JAR

1. Download MySQL Connector/J: https://dev.mysql.com/downloads/connector/j/
2. Extract the ZIP file
3. Copy `mysql-connector-java-X.X.XX.jar` to:
   - **For Tomcat**: `<TOMCAT_HOME>/lib/`
   - **For IDE**: Add to project build path

### Step 5: Compile and Deploy

#### Using Eclipse:
1. Import project as "Dynamic Web Project"
2. Right-click project → Run As → Run on Server
3. Select Apache Tomcat
4. Access: `http://localhost:8080/ums/login.html`

#### Using IntelliJ IDEA:
1. File → Open → Select project folder
2. Configure Tomcat server
3. Run → Run 'Tomcat'
4. Access: `http://localhost:8080/login.html`

#### Manual Deployment:
1. Compile all Java files:
```bash
javac -d build/classes src/main/java/**/*.java
```

2. Create WAR file:
```bash
jar -cvf ums.war -C src/main/webapp .
```

3. Copy to Tomcat:
```bash
cp ums.war <TOMCAT_HOME>/webapps/
```

4. Start Tomcat:
```bash
cd <TOMCAT_HOME>/bin
./startup.sh  # Linux/Mac
startup.bat   # Windows
```

5. Access: `http://localhost:8080/ums/login.html`

---

## ☁️ OPTION 2: Cloud Setup (Replit + Clever Cloud)

### Step 1: Set Up Clever Cloud Database

1. Sign up at https://www.clever-cloud.com
2. Create new MySQL add-on:
   - Click "Create" → "Add-on"
   - Select "MySQL"
   - Choose plan (Free "DEV" plan available)
   - Note down the credentials

3. Access Adminer:
   - Go to Add-on dashboard
   - Click "Adminer" link
   - Login with provided credentials

4. Import Database:
   - In Adminer, click "Import"
   - Upload `database/schema.sql`
   - Upload `database/sample_data.sql`

### Step 2: Set Up Replit Project

1. Sign up/Login to https://replit.com
2. Click "+ Create Repl"
3. Select "Java (Swing)"
4. Name it "university-management-system"

5. Upload files:
   - Delete default files
   - Upload all files from this project
   - Or use Git import (if pushed to GitHub)

6. Configure database in `conn.java`:
```java
// Use Clever Cloud credentials
String host = "your-host.mysql.clever-cloud.com";
String port = "3306";
String database = "your-db-name";
String username = "your-username";
String password = "your-password";
```

7. Add dependencies in `.replit` file:
```
run = "javac -d build -cp .:mysql-connector-java.jar src/main/java/**/*.java && java -cp build:mysql-connector-java.jar Main"
```

8. Click "Run" button

---

## 🧪 Testing the Application

### 1. Test Database Connection

Run `conn.java` main method:
```bash
java -cp .:mysql-connector-java.jar utils.conn
```

Expected output:
```
✓ Database connected successfully!
✓ Total students in database: 5
```

### 2. Access Login Page

Open browser: `http://localhost:8080/ums/login.html`

### 3. Test Login

**Admin Login:**
- Username: `admin`
- Password: `admin123`

**User Login:**
- Username: `user`
- Password: `user123`

### 4. Navigate Dashboard

- Click "View Students" → Should show 5 sample students
- Click "View Attendance" → Should show attendance records
- Click "View Marks" → Should show marks records

---

## 📸 Taking Screenshots for Documentation

### Required Screenshots:

1. **Login Page** - `login.html`
2. **Admin Dashboard** - After admin login
3. **User Dashboard** - After user login
4. **Add Student Form** - `addStudent.html`
5. **View Students Table** - List of all students
6. **Update Student Form** - `updateStudent.html`
7. **Delete Student Form** - `deleteStudent.html`
8. **Search Student** - Search functionality
9. **Add Attendance** - Attendance marking form
10. **View Attendance Table** - Attendance records
11. **View Marks** - Marks display
12. **View Fees** - Fee records
13. **Database - Adminer** - Database interface

---

## 🐛 Common Issues & Solutions

### Issue 1: "ClassNotFoundException: com.mysql.cj.jdbc.Driver"
**Solution:** Add MySQL Connector JAR to classpath

### Issue 2: "Access denied for user"
**Solution:** Check MySQL username/password in `conn.java`

### Issue 3: "Database connection failed"
**Solution:** 
- Ensure MySQL service is running
- Check firewall settings
- Verify database name exists

### Issue 4: "404 Not Found"
**Solution:**
- Check Tomcat is running
- Verify deployment path
- Check web.xml configuration

### Issue 5: Session timeout immediately
**Solution:** Check browser cookies are enabled

---

## 📞 Need Help?

If you encounter any issues:

1. Check console logs in IDE
2. Check Tomcat logs: `<TOMCAT_HOME>/logs/catalina.out`
3. Verify all file paths are correct
4. Ensure all dependencies are included

---

## 🎯 Next Steps After Setup

Once you have the minor project running:

1. ✅ Take screenshots of all features
2. ✅ Test all CRUD operations
3. ✅ Document any bugs or improvements needed
4. ✅ Plan major project enhancements
5. ✅ Push code to GitHub repository

---

**🎓 Good luck with your project!**
