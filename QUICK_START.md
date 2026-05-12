# 🚀 QUICK START GUIDE - University Management System

## ⚡ Get Your UMS Running in 10 Minutes!

---

## 📋 Step 1: Install Prerequisites (5 minutes)

### 1.1 Install Java JDK 8+
**Windows:**
- Download: https://www.oracle.com/java/technologies/downloads/
- Install and set JAVA_HOME environment variable
- Verify: Open CMD and run `java -version`

**Check if already installed:**
```cmd
java -version
```

### 1.2 Install MySQL
**Windows:**
- Download: https://dev.mysql.com/downloads/installer/
- Choose "MySQL Installer Community"
- During installation, set root password (remember this!)
- Install MySQL Server + MySQL Workbench

**Check if MySQL is running:**
```cmd
mysql --version
```

### 1.3 Download Apache Tomcat 9
- Download: https://tomcat.apache.org/download-90.cgi
- Choose "32-bit/64-bit Windows Service Installer" for Windows
- OR download ZIP and extract to `C:\apache-tomcat-9.0`

---

## 🗄️ Step 2: Set Up Database (2 minutes)

### 2.1 Start MySQL
**Windows:**
```cmd
net start MySQL80
```

### 2.2 Open MySQL Command Line
```cmd
mysql -u root -p
```
(Enter your root password)

### 2.3 Create Database & Tables
```sql
-- Copy ALL content from database/schema.sql and paste here
-- Then copy ALL content from database/sample_data.sql and paste

-- OR run files directly:
source C:/path/to/your/project/database/schema.sql;
source C:/path/to/your/project/database/sample_data.sql;
```

### 2.4 Verify Database
```sql
USE ums_db;
SHOW TABLES;
SELECT * FROM account;
SELECT * FROM student;
```

You should see:
- 2 accounts (admin, user)
- 5 sample students

---

## ⚙️ Step 3: Configure Database Connection (1 minute)

### 3.1 Edit Connection File
Open: `src/main/java/utils/conn.java`

Find these lines (around line 27-32):
```java
// For Local MySQL (Uncomment below)
String host = "localhost";
String port = "3306";
String database = "ums_db";
String username = "root";
String password = "YOUR_MYSQL_PASSWORD";  // ← CHANGE THIS!
```

**Change the password to your MySQL root password!**

---

## 📦 Step 4: Add MySQL Connector JAR (1 minute)

### 4.1 Download MySQL Connector
- Download: https://dev.mysql.com/downloads/connector/j/
- Click "Platform Independent" → Download ZIP
- Extract the ZIP file
- Find: `mysql-connector-java-8.0.XX.jar`

### 4.2 Add JAR to Project

**Option A: For Tomcat**
Copy `mysql-connector-java-8.0.XX.jar` to:
```
C:\apache-tomcat-9.0\lib\
```

**Option B: For Eclipse/IDE**
- Right-click project → Properties → Java Build Path
- Click "Add External JARs"
- Select `mysql-connector-java-8.0.XX.jar`

---

## 🚀 Step 5: Run the Project! (1 minute)

### Option A: Using Eclipse IDE

1. **Import Project**
   - File → Import → Existing Projects into Workspace
   - Select your project folder
   - Click Finish

2. **Configure Tomcat Server**
   - Window → Preferences → Server → Runtime Environments
   - Add → Apache Tomcat v9.0
   - Browse to Tomcat installation folder

3. **Run Project**
   - Right-click project → Run As → Run on Server
   - Select Tomcat
   - Click Finish

4. **Access Application**
   - Browser will open automatically
   - OR go to: `http://localhost:8080/ums/login.html`

### Option B: Using IntelliJ IDEA

1. **Open Project**
   - File → Open → Select project folder

2. **Configure Tomcat**
   - Run → Edit Configurations
   - Click + → Tomcat Server → Local
   - Configure Tomcat Home
   - In Deployment tab, add your WAR

3. **Run**
   - Click Run button
   - Access: `http://localhost:8080/login.html`

### Option C: Manual Deployment

1. **Create WAR file**
```cmd
cd your-project-folder
jar -cvf ums.war -C src/main/webapp .
```

2. **Copy to Tomcat**
```cmd
copy ums.war C:\apache-tomcat-9.0\webapps\
```

3. **Start Tomcat**
```cmd
cd C:\apache-tomcat-9.0\bin
startup.bat
```

4. **Access Application**
```
http://localhost:8080/ums/login.html
```

---

## 🔐 Step 6: Login & Test!

### Login Credentials:

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**User Account (Read-Only):**
- Username: `user`
- Password: `user123`

### Test These Features:

1. ✅ **View Students** → Should show 5 students
2. ✅ **Add Student** → Create new student (Admin only)
3. ✅ **View Attendance** → See attendance records
4. ✅ **View Marks** → See examination marks
5. ✅ **View Fees** → See fee records

---

## 🐛 Troubleshooting

### Issue: "Database connection failed"
**Solution:**
- Check MySQL is running: `net start MySQL80`
- Verify password in `conn.java`
- Check database exists: `SHOW DATABASES;`

### Issue: "ClassNotFoundException: com.mysql.cj.jdbc.Driver"
**Solution:**
- Add MySQL Connector JAR to Tomcat lib folder
- OR add to project build path

### Issue: "404 Not Found"
**Solution:**
- Check Tomcat is running
- Verify URL: `http://localhost:8080/ums/login.html`
- Check webapp folder structure

### Issue: "Can't compile servlets"
**Solution:**
- Ensure JDK is installed (not just JRE)
- Add servlet-api.jar to build path
- OR use IDE's built-in Tomcat library

---

## 📊 Next Steps

Once running successfully:

1. ✅ **Test all features**
2. ✅ **Take screenshots**
3. ✅ **Add your own student data**
4. ✅ **Push to GitHub**
5. ✅ **Start planning AI/ML enhancements**

---

## 📞 Need Help?

Check these logs:
- **Tomcat logs**: `C:\apache-tomcat-9.0\logs\catalina.out`
- **MySQL logs**: Check MySQL Workbench
- **IDE console**: Check for error messages

---

**🎉 Congratulations! Your UMS is running!**
