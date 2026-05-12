# 🤖 UMS AI/ML Backend

Flask API providing AI/ML features for the University Management System.

## 📌 Features Implemented

1. **Student Performance Prediction** - Identify at-risk students
2. **Attendance Pattern Analysis** - Analyze attendance trends
3. **Fee Defaulter Prediction** - Predict potential defaulters
4. **Grade Prediction** - Predict final grades from internal marks

## 🚀 Quick Start

### Option 1: Using BAT file (Windows - EASIEST)
```cmd
Double-click START_ML_BACKEND.bat
```

### Option 2: Manual Start
```cmd
cd ml_backend
pip install -r requirements.txt
python app.py
```

## ⚙️ Configuration

Edit `app.py` and change MySQL password (Line 18):
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_MYSQL_PASSWORD',  # CHANGE THIS!
    'database': 'ums_db'
}
```

## 📡 API Endpoints

Once started, API will be available at `http://localhost:5000`

### 1. Performance Prediction
```
GET http://localhost:5000/api/predict/performance
```

### 2. Attendance Analysis
```
GET http://localhost:5000/api/analyze/attendance
```

### 3. Fee Defaulter Prediction
```
GET http://localhost:5000/api/predict/fee_defaulters
```

### 4. Grade Prediction
```
GET http://localhost:5000/api/predict/grades
```

## 🧪 Testing

Test in browser:
```
http://localhost:5000/
http://localhost:5000/api/predict/performance
```

## 📦 Dependencies

- Flask - Web framework
- flask-cors - Enable CORS for Java frontend
- mysql-connector-python - MySQL database connection
- pandas - Data manipulation
- numpy - Numerical operations

## 🔧 Troubleshooting

**Port already in use:**
Edit `app.py` line 240: Change `port=5000` to another port

**MySQL connection error:**
Check MySQL is running and password is correct in `DB_CONFIG`

**Module not found:**
Run: `pip install -r requirements.txt`
