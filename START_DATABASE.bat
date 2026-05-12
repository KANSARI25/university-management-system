@echo off
echo ================================================
echo   Starting MySQL Database Service
echo ================================================
echo.

echo Starting MySQL service...
net start MySQL80

if %errorlevel% == 0 (
    echo.
    echo ✓ MySQL started successfully!
    echo.
    echo To create database, run: SETUP_DATABASE.bat
    echo.
) else (
    echo.
    echo ✗ Failed to start MySQL
    echo Please check if MySQL is installed
    echo.
)

pause
