@echo off
echo ================================================
echo   UMS Database Setup
echo ================================================
echo.
echo This will create the database and load sample data.
echo.
echo IMPORTANT: Make sure MySQL is running first!
echo (Run START_DATABASE.bat if not already running)
echo.
pause
echo.

cd database

echo Creating database and tables...
mysql -u root -p < schema.sql

if %errorlevel% == 0 (
    echo ✓ Database and tables created successfully!
    echo.
    echo Loading sample data...
    mysql -u root -p < sample_data.sql
    
    if %errorlevel% == 0 (
        echo ✓ Sample data loaded successfully!
        echo.
        echo Database setup complete! ✓
        echo.
        echo Next step: Update passwords in code files
        echo - src/main/java/utils/conn.java
        echo - ml_backend/app.py
        echo.
    )
)

cd ..
pause
