@echo off
echo ================================================
echo   UMS AI/ML Backend - Starting Flask Server
echo ================================================
echo.
echo Installing dependencies (first time only)...
pip install -r requirements.txt
echo.
echo Starting Flask API on http://localhost:5000
echo.
python app.py
pause
