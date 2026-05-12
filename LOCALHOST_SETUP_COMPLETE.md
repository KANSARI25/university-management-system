# 🚀 LOCALHOST SETUP - COMPLETE GUIDE (SIMPLEST METHOD)

## 🎯 **GOAL: Get Your UMS Running on Localhost in 15 Minutes**

---

## 📋 **WHAT YOU NEED TO INSTALL (One-Time Setup):**

### 1. Java JDK (If not installed)
- Download: https://www.oracle.com/java/technologies/downloads/#jdk17-windows
- Choose: Windows x64 Installer
- Install with default settings
- **Time: 5 minutes**

### 2. Apache Tomcat
- Download: https://tomcat.apache.org/download-90.cgi
- Scroll down to "Binary Distributions"
- Download: **64-bit Windows zip** (apache-tomcat-9.0.XX-windows-x64.zip)
- Extract to: `C:\tomcat` (simple path!)
- **Time: 2 minutes**

### 3. MySQL
- Download: https://dev.mysql.com/downloads/installer/
- Choose: **mysql-installer-community** (smaller web installer)
- Install: MySQL Server + MySQL Workbench
- Set root password: `root123` (remember this!)
- **Time: 5 minutes**

### 4. MySQL Connector JAR
- Download: https://dev.mysql.com/downloads/connector/j/
- Choose: **Platform Independent (ZIP)**
- Download and extract
- Find file: `mysql-connector-j-8.X.XX.jar`
- **Time: 2 minutes**

---

## 🗄️ **STEP 1: SETUP DATABASE (5 minutes)**

### 1.1 Start MySQL
```cmd
net start MySQL80
```
(Or search "Services" in Windows → Start MySQL80)

### 1.2 Open MySQL Command Line
```cmd
mysql -u root -p
```
Password: `root123` (or whatever you set)

### 1.3 Create Database
Copy and paste this in MySQL command line:

```sql
CREATE DATABASE ums_db;
USE ums_db;
```

### 1.4 Create Tables
Open file: `database/schema.sql` in Notepad
Copy ALL content
Paste in MySQL command line
Press Enter

### 1.5 Add Sample Data
Open file: `database/sample_data.sql` in Notepad  
Copy ALL content  
Paste in MySQL command line  
Press Enter

### 1.6 Verify
```sql
SHOW TABLES;
SELECT * FROM account;
```
You should see 8 tables! ✅

---

## 🔧 **STEP 2: CONFIGURE PROJECT (5 minutes)**

### 2.1 Update MySQL Password in Java
Open: `src/main/java/utils/conn.java`

Find line ~31:
```java
String password = "YOUR_MYSQL_PASSWORD";
```

Change to:
```java
String password = "root123";  // Your MySQL password
```

### 2.2 Update MySQL Password in Python
Open: `ml_backend/app.py`

Find line ~18:
```python
'password': 'YOUR_MYSQL_PASSWORD',
```

Change to:
```python
'password': 'root123',  # Your MySQL password
```

### 2.3 Copy MySQL Connector JAR
Copy the file: `mysql-connector-j-8.X.XX.jar`  
To: `C:\tomcat\lib\`

---

## 📦 **STEP 3: PREPARE WEB APPLICATION (3 minutes)**

### 3.1 Create Webapp Folder Structure
Create this structure in `C:\tomcat\webapps\ums\`:

```
C:\tomcat\webapps\ums\
├── WEB-INF\
│   ├── classes\
│   ├── lib\
│   └── web.xml
├── login.html
├── dashboard.jsp
├── addStudent.html
└── (all other HTML/JSP files)
```

### 3.2 Copy Files

**Copy ALL .html and .jsp files:**
From: `src/main/webapp/`  
To: `C:\tomcat\webapps\ums\`

**Copy web.xml:**
From: `src/main/webapp/WEB-INF/web.xml`  
To: `C:\tomcat\webapps\ums\WEB-INF\web.xml`

**Copy compiled Java classes:**
You need to compile the Java files first. See below.

---

## ⚙️ **STEP 4: COMPILE JAVA FILES (IMPORTANT!)**

### Option A: Use Eclipse/IntelliJ (If you have it)
1. Import project
2. Add MySQL connector JAR to build path
3. Build project (Ctrl+B)
4. Export as WAR file
5. Copy WAR to `C:\tomcat\webapps\` (it auto-deploys!)

### Option B: Manual Compilation (If no IDE)

Open Command Prompt in your project folder:

```cmd
cd src\main\java

javac -cp "C:\tomcat\lib\servlet-api.jar;path\to\mysql-connector-j-8.X.XX.jar" -d ..\..\..\..\tomcat\webapps\ums\WEB-INF\classes utils\conn.java servlets\*.java
```

Replace `path\to\` with actual path to MySQL connector JAR.

---

## 🚀 **STEP 5: START TOMCAT (1 minute)**

```cmd
cd C:\tomcat\bin
startup.bat
```

A window will open showing Tomcat logs.

Wait until you see: `Server startup in [XXXX] milliseconds`

**Tomcat is running!** ✅

---

## 🐍 **STEP 6: START PYTHON AI/ML BACKEND (2 minutes)**

Open **NEW** Command Prompt:

```cmd
cd "C:\Users\mansari\OneDrive - Ashley Furniture Industries, Inc\Desktop\Major_Project_Shabbir\ml_backend"

pip install flask flask-cors mysql-connector-python pandas numpy

python app.py
```

You should see:
```
🚀 UMS AI/ML Backend Starting...
📡 API will be available at: http://localhost:5000
```

**Flask is running!** ✅

---

## 🌐 **STEP 7: ACCESS YOUR APPLICATION**

Open browser:

### Main Application (Java):
```
http://localhost:8080/ums/login.html
```

### Login Credentials:
- **Username:** `admin`
- **Password:** `admin123`

### AI/ML Backend (Python):
```
http://localhost:5000
```

---

## ✅ **VERIFICATION CHECKLIST:**

- [ ] MySQL is running (check Services)
- [ ] Database `ums_db` exists with 8 tables
- [ ] Sample data loaded (5 students, 3 teachers)
- [ ] Password updated in `conn.java`
- [ ] Password updated in `app.py`
- [ ] MySQL connector JAR in `C:\tomcat\lib\`
- [ ] Files copied to `C:\tomcat\webapps\ums\`
- [ ] Java files compiled
- [ ] Tomcat started (port 8080)
- [ ] Flask started (port 5000)
- [ ] Browser shows login page

---

## 🎯 **QUICK TROUBLESHOOTING:**

### ❌ "This site can't be reached"
**Solution:** Tomcat not running. Start it:
```cmd
cd C:\tomcat\bin
startup.bat
```

### ❌ "404 Not Found"
**Solution:** Check files are in `C:\tomcat\webapps\ums\`

### ❌ "Database connection failed"
**Solution:** 
1. Check MySQL is running: `net start MySQL80`
2. Verify password in `conn.java` matches your MySQL password

### ❌ "ClassNotFoundException: com.mysql.cj.jdbc.Driver"
**Solution:** Copy `mysql-connector-j-8.X.XX.jar` to `C:\tomcat\lib\`

---

## 📸 **FOR YOUR DOCUMENTATION:**

### Screenshots to Take:
1. MySQL database tables (SHOW TABLES)
2. Sample data (SELECT * FROM student)
3. Tomcat startup console
4. Flask backend console
5. Login page
6. Dashboard after login
7. Add student form
8. Student list view
9. All other features
10. AI/ML analytics page

### What to Document:
1. Installation steps you followed
2. Configuration changes (passwords, paths)
3. How to start the application
4. Screenshots of all features
5. Database schema (ER diagram)
6. Code snippets (servlets, JSP)

---

## 💡 **EVEN SIMPLER: PRE-COMPILED VERSION**

Want me to create a **ready-to-run ZIP file** with:
- ✅ Pre-compiled Java classes
- ✅ All files in correct structure
- ✅ Batch scripts to auto-start everything
- ✅ Just extract and run?

Let me know! 🚀
