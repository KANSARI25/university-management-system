@echo off
echo ================================================================
echo   UMS PROJECT - INSTALLATION VERIFICATION
echo ================================================================
echo.
echo Checking what you have installed...
echo.
echo ================================================================

echo 1. CHECKING JAVA...
echo ----------------------------------------------------------------
java -version 2>&1 | findstr "version" >nul
if %errorlevel% == 0 (
    echo [✓] Java is installed
    java -version 2>&1 | findstr "version"
) else (
    echo [✗] Java NOT found
    echo     Download from: https://www.oracle.com/java/technologies/downloads/
)
echo.

echo 2. CHECKING PYTHON...
echo ----------------------------------------------------------------
python --version 2>&1 | findstr "Python" >nul
if %errorlevel% == 0 (
    echo [✓] Python is installed
    python --version
) else (
    echo [✗] Python NOT found
    echo     You mentioned you have it - check PATH variable
)
echo.

echo 3. CHECKING MYSQL...
echo ----------------------------------------------------------------
mysql --version 2>&1 | findstr "mysql" >nul
if %errorlevel% == 0 (
    echo [✓] MySQL client is installed
    mysql --version
) else (
    echo [✗] MySQL NOT found
    echo     Download from: https://dev.mysql.com/downloads/installer/
)
echo.

echo 4. CHECKING MYSQL SERVICE...
echo ----------------------------------------------------------------
sc query MySQL80 | findstr "RUNNING" >nul
if %errorlevel% == 0 (
    echo [✓] MySQL service is RUNNING
) else (
    sc query MySQL80 | findstr "STOPPED" >nul
    if %errorlevel% == 0 (
        echo [!] MySQL service is STOPPED
        echo     Run: START_DATABASE.bat to start it
    ) else (
        echo [✗] MySQL service NOT found
        echo     MySQL may not be installed or service name is different
    )
)
echo.

echo 5. CHECKING TOMCAT...
echo ----------------------------------------------------------------
if exist "C:\tomcat\bin\startup.bat" (
    echo [✓] Tomcat found at C:\tomcat
) else if exist "C:\apache-tomcat-9.0\bin\startup.bat" (
    echo [✓] Tomcat found at C:\apache-tomcat-9.0
) else if exist "C:\Program Files\Apache Software Foundation\Tomcat 9.0\bin\startup.bat" (
    echo [✓] Tomcat found in Program Files
) else (
    echo [✗] Tomcat NOT found
    echo     Download from: https://tomcat.apache.org/download-90.cgi
    echo     Extract to: C:\tomcat
)
echo.

echo 6. CHECKING PYTHON PACKAGES...
echo ----------------------------------------------------------------
pip show flask >nul 2>&1
if %errorlevel% == 0 (
    echo [✓] Flask is installed
) else (
    echo [✗] Flask NOT installed
    echo     Run: pip install flask
)

pip show flask-cors >nul 2>&1
if %errorlevel% == 0 (
    echo [✓] Flask-CORS is installed
) else (
    echo [✗] Flask-CORS NOT installed
    echo     Run: pip install flask-cors
)

pip show mysql-connector-python >nul 2>&1
if %errorlevel% == 0 (
    echo [✓] MySQL Connector for Python is installed
) else (
    echo [✗] MySQL Connector NOT installed
    echo     Run: pip install mysql-connector-python
)

pip show pandas >nul 2>&1
if %errorlevel% == 0 (
    echo [✓] Pandas is installed
) else (
    echo [✗] Pandas NOT installed
    echo     Run: pip install pandas
)

pip show numpy >nul 2>&1
if %errorlevel% == 0 (
    echo [✓] NumPy is installed
) else (
    echo [✗] NumPy NOT installed
    echo     Run: pip install numpy
)
echo.

echo 7. CHECKING PORT AVAILABILITY...
echo ----------------------------------------------------------------
netstat -ano | findstr ":8080" >nul
if %errorlevel% == 0 (
    echo [!] Port 8080 is IN USE (Tomcat might be running already)
) else (
    echo [✓] Port 8080 is FREE (good for Tomcat)
)

netstat -ano | findstr ":5000" >nul
if %errorlevel% == 0 (
    echo [!] Port 5000 is IN USE (Flask might be running already)
) else (
    echo [✓] Port 5000 is FREE (good for Flask)
)
echo.

echo ================================================================
echo   SUMMARY
echo ================================================================
echo.
echo If you see [✓] - you're good!
echo If you see [✗] - you need to install that component
echo If you see [!] - check the message
echo.
echo ================================================================
echo   WHAT TO INSTALL (if missing)
echo ================================================================
echo.
echo Missing components? Run these:
echo.
echo 1. Install Python packages:
echo    pip install flask flask-cors mysql-connector-python pandas numpy
echo.
echo 2. Check INSTALLATION_LINKS.txt for download links
echo.
echo ================================================================
pause
