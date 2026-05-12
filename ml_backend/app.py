# University Management System - AI/ML Backend
# Flask API for AI/ML Features (BCA Major Project)
# Author: Shabbir Ansari

from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)  # Enable CORS for Java frontend

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_MYSQL_PASSWORD',  # CHANGE THIS!
    'database': 'ums_db'
}

def get_db_connection():
    """Get MySQL database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        return None


# ==================== FEATURE 1: STUDENT PERFORMANCE PREDICTION ====================

@app.route('/api/predict/performance', methods=['GET'])
def predict_performance():
    """
    Predict student at-risk status based on attendance and marks
    Algorithm: Simple threshold-based classification (BCA-level)
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        # Get student performance data
        query = """
            SELECT 
                s.roll_no,
                s.name,
                s.semester,
                COALESCE(AVG((a.attended_classes * 100.0 / a.total_classes)), 0) as attendance_percent,
                COALESCE(AVG(m.internal_marks + m.external_marks), 0) as avg_marks
            FROM student s
            LEFT JOIN attendance_student a ON s.roll_no = a.roll_no
            LEFT JOIN marks m ON s.roll_no = m.roll_no
            WHERE s.status = 'Active'
            GROUP BY s.roll_no, s.name, s.semester
        """
        
        cursor.execute(query)
        students = cursor.fetchall()
        
        predictions = []
        for student in students:
            attendance = float(student['attendance_percent'])
            marks = float(student['avg_marks'])
            
            # Simple rule-based prediction
            risk_score = 0
            risk_factors = []
            
            if attendance < 60:
                risk_score += 40
                risk_factors.append("Very Low Attendance")
            elif attendance < 75:
                risk_score += 20
                risk_factors.append("Low Attendance")
            
            if marks < 40:
                risk_score += 40
                risk_factors.append("Failing Marks")
            elif marks < 55:
                risk_score += 20
                risk_factors.append("Below Average Marks")
            
            # Determine risk level
            if risk_score >= 50:
                risk_level = "High Risk"
                color = "red"
            elif risk_score >= 25:
                risk_level = "Medium Risk"
                color = "orange"
            else:
                risk_level = "Low Risk"
                color = "green"
            
            predictions.append({
                'roll_no': student['roll_no'],
                'name': student['name'],
                'semester': student['semester'],
                'attendance': round(attendance, 2),
                'avg_marks': round(marks, 2),
                'risk_level': risk_level,
                'risk_score': risk_score,
                'risk_factors': risk_factors,
                'color': color
            })
        
        cursor.close()
        conn.close()
        
        return jsonify({
            'success': True,
            'total_students': len(predictions),
            'predictions': predictions
        })
        
    except Exception as e:
        print(f"❌ Error in performance prediction: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== FEATURE 2: ATTENDANCE PATTERN ANALYSIS ====================

@app.route('/api/analyze/attendance', methods=['GET'])
def analyze_attendance():
    """
    Analyze attendance patterns and trends
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        # Get attendance data
        query = """
            SELECT 
                s.roll_no,
                s.name,
                s.course,
                s.semester,
                a.total_classes,
                a.attended_classes,
                (a.attended_classes * 100.0 / a.total_classes) as attendance_percent
            FROM student s
            JOIN attendance_student a ON s.roll_no = a.roll_no
            WHERE s.status = 'Active' AND a.total_classes > 0
        """
        
        cursor.execute(query)
        records = cursor.fetchall()
        
        analysis = {
            'total_records': len(records),
            'excellent': 0,  # >= 90%
            'good': 0,       # 75-89%
            'satisfactory': 0,  # 60-74%
            'poor': 0,       # < 60%
            'students': []
        }
        
        for record in records:
            percent = float(record['attendance_percent'])
            
            if percent >= 90:
                analysis['excellent'] += 1
                category = "Excellent"
                color = "green"
            elif percent >= 75:
                analysis['good'] += 1
                category = "Good"
                color = "blue"
            elif percent >= 60:
                analysis['satisfactory'] += 1
                category = "Satisfactory"
                color = "orange"
            else:
                analysis['poor'] += 1
                category = "Poor"
                color = "red"
            
            analysis['students'].append({
                'roll_no': record['roll_no'],
                'name': record['name'],
                'course': record['course'],
                'semester': record['semester'],
                'total_classes': record['total_classes'],
                'attended': record['attended_classes'],
                'percentage': round(percent, 2),
                'category': category,
                'color': color
            })
        
        cursor.close()
        conn.close()
        
        return jsonify({
            'success': True,
            'analysis': analysis
        })
        
    except Exception as e:
        print(f"❌ Error in attendance analysis: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== FEATURE 3: FEE DEFAULTER PREDICTION ====================

@app.route('/api/predict/fee_defaulters', methods=['GET'])
def predict_fee_defaulters():
    """
    Predict potential fee defaulters based on payment history
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT 
                s.roll_no,
                s.name,
                s.phone,
                s.email,
                f.semester,
                f.total_fee,
                f.paid_fee,
                (f.total_fee - f.paid_fee) as pending_fee,
                f.due_date,
                DATEDIFF(f.due_date, CURDATE()) as days_until_due
            FROM student s
            JOIN fee f ON s.roll_no = f.roll_no
            WHERE s.status = 'Active'
        """
        
        cursor.execute(query)
        records = cursor.fetchall()
        
        defaulters = []
        for record in records:
            pending = int(record['pending_fee'])
            total = int(record['total_fee'])
            days_until_due = record['days_until_due'] if record['days_until_due'] else 0
            
            if pending > 0:
                paid_percent = (int(record['paid_fee']) * 100.0 / total)
                
                # Determine risk
                if days_until_due < 0:
                    risk_level = "Overdue"
                    priority = "Critical"
                    color = "red"
                elif days_until_due <= 7 and paid_percent < 50:
                    risk_level = "High Risk"
                    priority = "High"
                    color = "orange"
                elif paid_percent < 30:
                    risk_level = "Medium Risk"
                    priority = "Medium"
                    color = "yellow"
                else:
                    risk_level = "Low Risk"
                    priority = "Low"
                    color = "blue"
                
                defaulters.append({
                    'roll_no': record['roll_no'],
                    'name': record['name'],
                    'phone': record['phone'],
                    'email': record['email'],
                    'semester': record['semester'],
                    'total_fee': total,
                    'paid_fee': int(record['paid_fee']),
                    'pending_fee': pending,
                    'paid_percent': round(paid_percent, 2),
                    'due_date': str(record['due_date']),
                    'days_until_due': days_until_due,
                    'risk_level': risk_level,
                    'priority': priority,
                    'color': color
                })
        
        # Sort by priority
        priority_order = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3}
        defaulters.sort(key=lambda x: priority_order[x['priority']])
        
        cursor.close()
        conn.close()
        
        return jsonify({
            'success': True,
            'total_defaulters': len(defaulters),
            'defaulters': defaulters
        })
        
    except Exception as e:
        print(f"❌ Error in fee defaulter prediction: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== FEATURE 4: GRADE PREDICTION ====================

@app.route('/api/predict/grades', methods=['GET'])
def predict_grades():
    """
    Predict final grades based on internal marks
    Simple linear extrapolation (BCA-level)
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT 
                s.roll_no,
                s.name,
                m.subject_code,
                m.semester,
                m.internal_marks,
                m.external_marks
            FROM student s
            JOIN marks m ON s.roll_no = m.roll_no
            WHERE s.status = 'Active'
        """
        
        cursor.execute(query)
        records = cursor.fetchall()
        
        predictions = []
        for record in records:
            internal = int(record['internal_marks'])
            external = int(record['external_marks'])
            current_total = internal + external
            
            # Simple prediction: Scale internal marks to predict potential final grade
            # Assuming internal is out of 30, predict if student maintains performance
            predicted_external = (internal / 30) * 70  # Scale to external marks (70 max)
            predicted_total = internal + predicted_external
            
            # Determine grade
            if predicted_total >= 85:
                predicted_grade = "A"
            elif predicted_total >= 70:
                predicted_grade = "B"
            elif predicted_total >= 55:
                predicted_grade = "C"
            elif predicted_total >= 40:
                predicted_grade = "D"
            else:
                predicted_grade = "F"
            
            predictions.append({
                'roll_no': record['roll_no'],
                'name': record['name'],
                'subject': record['subject_code'],
                'semester': record['semester'],
                'internal_marks': internal,
                'current_external': external,
                'current_total': current_total,
                'predicted_external': round(predicted_external, 2),
                'predicted_total': round(predicted_total, 2),
                'predicted_grade': predicted_grade
            })
        
        cursor.close()
        conn.close()
        
        return jsonify({
            'success': True,
            'total_predictions': len(predictions),
            'predictions': predictions
        })
        
    except Exception as e:
        print(f"❌ Error in grade prediction: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== ROOT ENDPOINT ====================

@app.route('/')
def index():
    return jsonify({
        'message': 'UMS AI/ML Backend API',
        'version': '1.0',
        'endpoints': [
            '/api/predict/performance',
            '/api/analyze/attendance',
            '/api/predict/fee_defaulters',
            '/api/predict/grades'
        ]
    })


if __name__ == '__main__':
    print("="*60)
    print("🚀 UMS AI/ML Backend Starting...")
    print("📡 API will be available at: http://localhost:5000")
    print("="*60)
    app.run(debug=True, port=5000, host='0.0.0.0')
