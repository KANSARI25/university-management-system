"""
University Management System - Streamlit Application
Complete UMS with AI/ML Features
Author: Shabbir Ansari
BCA606 Major Project (2025-2026)
"""

import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import hashlib
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO
import shutil
import os

# Page Configuration
st.set_page_config(
    page_title="University Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Amazon/Flipkart Style UI
st.markdown("""
<style>
    /* Hide Streamlit header, footer, and deploy button */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hide the "Deploy" button and toolbar in top-right */
    .stDeployButton {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    header[data-testid="stHeader"] {display: none !important;}
    .css-18ni7ap {display: none !important;}
    .css-vurnku {display: none !important;}

    /* Remove top padding and increase base font size */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        font-size: 16px !important;
    }

    /* Increase all text sizes */
    .stMarkdown, .stText, p, div {
        font-size: 15px !important;
    }

    /* Main background - Light gradient - FORCE IT */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    }

    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    }

    /* Sidebar styling - Amazon style dark sidebar - FORCE VISIBILITY */
    [data-testid="stSidebar"] {
        background: #232f3e !important;
        min-width: 280px !important;
        display: block !important;
        visibility: visible !important;
        left: 0 !important;
    }

    /* Ensure sidebar is shown on page load */
    section[data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
        transform: none !important;
    }

    /* Show collapsed sidebar control button - big and visible */
    [data-testid="collapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Increase font size for sidebar radio buttons */
    [data-testid="stSidebar"] .stRadio label {
        font-size: 17px !important;
        padding: 12px 0 !important;
        line-height: 1.8 !important;
        font-weight: 500 !important;
    }

    /* Sidebar radio buttons spacing */
    [data-testid="stSidebar"] .stRadio > div {
        gap: 8px !important;
    }

    /* Header styling */
    .stTitle {
        color: #232f3e !important;
        font-weight: 700 !important;
        font-family: 'Amazon Ember', Arial, sans-serif !important;
    }

    /* Card styling - Clean cards like Flipkart */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background: #ffffff;
        padding: 0;
        border-bottom: 2px solid #e0e0e0;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 0;
        color: #878787 !important;
        font-weight: 600;
        padding: 15px 30px;
        border: none;
        border-bottom: 3px solid transparent;
    }

    .stTabs [aria-selected="true"] {
        background: transparent;
        color: #2874f0 !important;
        border-bottom: 3px solid #2874f0;
        box-shadow: none;
    }

    /* FORCE labels to be visible - dark text, no background */
    .stTextInput label,
    .stTextInput label *,
    .stTextInput label p,
    .stTextInput label div,
    .stSelectbox label,
    .stSelectbox label *,
    .stNumberInput label,
    .stNumberInput label *,
    .stDateInput label,
    .stDateInput label *,
    .stTextArea label,
    .stTextArea label * {
        color: #1a1a1a !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        font-family: 'Segoe UI', 'Roboto', Arial, sans-serif !important;
        background: transparent !important;
        background-color: transparent !important;
    }

    .stTextInput > label,
    .stSelectbox > label,
    .stNumberInput > label {
        margin-bottom: 8px !important;
        background: none !important;
    }

    /* FIX: Make cursor visible in all input fields */
    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input,
    .stDateInput input,
    .stSelectbox select {
        caret-color: #2c3e50 !important;
        cursor: text !important;
    }

    /* FIX: Make headings visible (dark text) */
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50 !important;
    }

    /* FIX: Sidebar collapse/expand button - LARGE and VISIBLE */
    [data-testid="collapsedControl"] {
        display: flex !important;
        opacity: 1 !important;
        visibility: visible !important;
        position: fixed !important;
        left: 0 !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        z-index: 999999 !important;
        background: #ff6b35 !important;
        padding: 20px 10px !important;
        border-radius: 0 12px 12px 0 !important;
        box-shadow: 3px 0 10px rgba(0,0,0,0.4) !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="collapsedControl"]:hover {
        background: #ff8555 !important;
        padding-right: 15px !important;
    }

    [data-testid="collapsedControl"] svg {
        width: 28px !important;
        height: 28px !important;
        color: #ffffff !important;
    }

    /* When sidebar is collapsed, show the button prominently */
    section[data-testid="stSidebar"][aria-expanded="false"] ~ [data-testid="collapsedControl"] {
        display: flex !important;
        left: 0 !important;
    }

    /* Input fields - Flipkart style */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input,
    .stDateInput > div > div > input,
    .stTextArea textarea {
        background: #ffffff !important;
        border: 1px solid #c2c2c2 !important;
        border-radius: 2px !important;
        font-size: 14px !important;
        padding: 12px !important;
        color: #212121 !important;
        transition: all 0.2s ease;
        font-family: 'Roboto', Arial, sans-serif !important;
    }

    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #2874f0 !important;
        box-shadow: 0 0 4px rgba(40,116,240,.4) !important;
        outline: none !important;
    }

    /* Buttons - Amazon orange style */
    .stButton > button {
        background: linear-gradient(to bottom, #f7dfa5, #f0c14b) !important;
        color: #111 !important;
        border: 1px solid #a88734 !important;
        border-radius: 3px !important;
        padding: 8px 20px !important;
        font-weight: 400 !important;
        font-size: 13px !important;
        box-shadow: 0 1px 0 rgba(255,255,255,.4) inset !important;
        transition: all 0.2s ease !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        font-family: 'Amazon Ember', Arial, sans-serif !important;
    }

    .stButton > button:hover {
        background: linear-gradient(to bottom, #f5d78e, #edb933) !important;
        transform: none !important;
        box-shadow: 0 1px 0 rgba(255,255,255,.6) inset !important;
    }

    /* Primary button (Login button) - Flipkart orange */
    .stButton > button[kind="primary"] {
        background: #fb641b !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 2px 4px 0 rgba(0,0,0,.2) !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: #e85c17 !important;
    }

    .stButton > button[kind="primary"]:active {
        background: #d44d11 !important;
        color: #ffffff !important;
    }

    /* Form submit buttons - Keep dark background */
    .stFormSubmitButton > button {
        background: #232f3e !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 500 !important;
    }

    .stFormSubmitButton > button:hover {
        background: #37475a !important;
        color: #ffffff !important;
    }

    .stFormSubmitButton > button:active {
        background: #131921 !important;
        color: #ffffff !important;
    }

    /* Metrics - Clean style */
    [data-testid="stMetricValue"] {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: #232f3e !important;
        font-family: 'Amazon Ember', Arial, sans-serif !important;
    }

    /* DataFrames - Clean table style with bigger font */
    .dataframe {
        border-radius: 4px !important;
        overflow: hidden !important;
        box-shadow: 0 2px 4px rgba(0,0,0,.1) !important;
        border: 1px solid #e0e0e0 !important;
        font-size: 14px !important;
    }

    .dataframe th {
        font-size: 15px !important;
        font-weight: 600 !important;
        padding: 12px 8px !important;
    }

    .dataframe td {
        font-size: 14px !important;
        padding: 10px 8px !important;
    }

    .dataframe thead th {
        background: #f7f7f7 !important;
        color: #232f3e !important;
        font-weight: 600 !important;
        padding: 12px !important;
        font-size: 13px !important;
        border-bottom: 2px solid #e0e0e0 !important;
        font-family: 'Amazon Ember', Arial, sans-serif !important;
    }

    .dataframe tbody tr:hover {
        background: #f7fafa !important;
        transform: none;
        transition: background 0.2s ease;
    }

    .dataframe tbody td {
        padding: 10px 12px !important;
        font-size: 13px !important;
        color: #0f1111 !important;
        border-bottom: 1px solid #f0f0f0 !important;
    }

    /* Success/Error Messages - Professional and prominent */
    .stSuccess {
        background: #d4edda !important;
        color: #155724 !important;
        border-radius: 6px !important;
        padding: 18px 22px !important;
        border-left: 6px solid #28a745 !important;
        box-shadow: 0 3px 10px rgba(40, 167, 69, 0.2) !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        margin: 20px 0 !important;
        white-space: pre-line !important;
    }

    .stError {
        background: #f8d7da !important;
        color: #721c24 !important;
        border-radius: 6px !important;
        padding: 18px 22px !important;
        border-left: 6px solid #dc3545 !important;
        box-shadow: 0 3px 10px rgba(220, 53, 69, 0.2) !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        margin: 20px 0 !important;
    }

    .stWarning {
        background: #fff3cd !important;
        color: #856404 !important;
        border-radius: 6px !important;
        padding: 18px 22px !important;
        border-left: 6px solid #ffc107 !important;
        box-shadow: 0 3px 10px rgba(255, 193, 7, 0.2) !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        margin: 20px 0 !important;
    }

    .stInfo {
        background: #d1ecf1 !important;
        color: #0c5460 !important;
        border-radius: 6px !important;
        padding: 18px 22px !important;
        border-left: 6px solid #17a2b8 !important;
        box-shadow: 0 3px 10px rgba(23, 162, 184, 0.2) !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        margin: 20px 0 !important;
    }

    /* Form containers - White cards */
    [data-testid="stForm"] {
        background: #ffffff;
        border-radius: 4px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,.1);
        border: 1px solid #e0e0e0;
    }

    /* Radio buttons */
    .stRadio > div {
        background: transparent;
        border-radius: 0;
        padding: 5px;
    }

    .stRadio label {
        color: #232f3e !important;
        font-weight: 400 !important;
        font-size: 14px !important;
        font-family: 'Amazon Ember', Arial, sans-serif !important;
    }

    /* Scrollbar - Minimal style */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }

    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
</style>
""", unsafe_allow_html=True)

# Database Setup
def init_db():
    """Initialize SQLite database with all tables"""
    conn = sqlite3.connect('ums_database.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS account (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS student (
            roll_no TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            father_name TEXT,
            dob DATE,
            address TEXT,
            phone TEXT,
            email TEXT,
            aadhar TEXT,
            course TEXT,
            branch TEXT,
            semester INTEGER,
            year INTEGER,
            gender TEXT,
            category TEXT,
            status TEXT DEFAULT 'Active'
        );
        
        CREATE TABLE IF NOT EXISTS teacher (
            emp_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            father_name TEXT,
            dob DATE,
            address TEXT,
            phone TEXT,
            email TEXT,
            qualification TEXT,
            department TEXT,
            designation TEXT,
            gender TEXT,
            status TEXT DEFAULT 'Active'
        );
        
        CREATE TABLE IF NOT EXISTS attendance_student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            semester INTEGER,
            total_classes INTEGER,
            attended_classes INTEGER,
            FOREIGN KEY (roll_no) REFERENCES student(roll_no)
        );
        
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            subject_code TEXT,
            semester INTEGER,
            internal_marks INTEGER,
            external_marks INTEGER,
            FOREIGN KEY (roll_no) REFERENCES student(roll_no)
        );
        
        CREATE TABLE IF NOT EXISTS fee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            semester INTEGER,
            total_fee INTEGER,
            paid_fee INTEGER,
            due_date DATE,
            FOREIGN KEY (roll_no) REFERENCES student(roll_no)
        );
    ''')
    
    # Insert default accounts if not exists
    cursor.execute("SELECT COUNT(*) FROM account")
    if cursor.fetchone()[0] == 0:
        # Hash passwords (simple hash for demo)
        admin_pass = hashlib.md5("admin123".encode()).hexdigest()
        user_pass = hashlib.md5("user123".encode()).hexdigest()
        
        cursor.executemany("INSERT INTO account VALUES (?, ?, ?, ?)", [
            ('admin', admin_pass, 'Administrator', 'admin'),
            ('user', user_pass, 'Regular User', 'user')
        ])
    
    # Insert sample students if table is empty
    cursor.execute("SELECT COUNT(*) FROM student")
    if cursor.fetchone()[0] == 0:
        sample_students = [
            ('2301001', 'Rahul Kumar', 'Ram Kumar', '2003-05-15', 'Delhi', '9876543210', 
             'rahul@email.com', '123456789012', 'BCA', 'Computer Science', 3, 2023, 'Male', 'General', 'Active'),
            ('2301002', 'Priya Sharma', 'Suresh Sharma', '2003-08-20', 'Mumbai', '9876543211',
             'priya@email.com', '123456789013', 'BCA', 'Computer Science', 3, 2023, 'Female', 'General', 'Active'),
            ('2301003', 'Amit Singh', 'Vijay Singh', '2003-03-10', 'Bangalore', '9876543212',
             'amit@email.com', '123456789014', 'BCA', 'Computer Science', 3, 2023, 'Male', 'OBC', 'Active'),
            ('2301004', 'Sneha Patel', 'Rajesh Patel', '2003-12-05', 'Ahmedabad', '9876543213',
             'sneha@email.com', '123456789015', 'BCA', 'Computer Science', 3, 2023, 'Female', 'General', 'Active'),
            ('2301005', 'Vikash Yadav', 'Ramesh Yadav', '2003-07-25', 'Lucknow', '9876543214',
             'vikash@email.com', '123456789016', 'BCA', 'Computer Science', 3, 2023, 'Male', 'OBC', 'Active'),
        ]
        cursor.executemany("INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", sample_students)
        
        # Sample attendance
        sample_attendance = [
            ('2301001', 3, 100, 92),
            ('2301002', 3, 100, 88),
            ('2301003', 3, 100, 65),
            ('2301004', 3, 100, 95),
            ('2301005', 3, 100, 55),
        ]
        cursor.executemany("INSERT INTO attendance_student (roll_no, semester, total_classes, attended_classes) VALUES (?,?,?,?)", 
                          sample_attendance)
        
        # Sample marks
        sample_marks = [
            ('2301001', 'BCA301', 3, 28, 65),
            ('2301002', 'BCA301', 3, 30, 68),
            ('2301003', 'BCA301', 3, 20, 45),
            ('2301004', 'BCA301', 3, 29, 70),
            ('2301005', 'BCA301', 3, 18, 38),
        ]
        cursor.executemany("INSERT INTO marks (roll_no, subject_code, semester, internal_marks, external_marks) VALUES (?,?,?,?,?)", 
                          sample_marks)
        
        # Sample fees
        sample_fees = [
            ('2301001', 3, 50000, 50000, '2024-01-15'),
            ('2301002', 3, 50000, 25000, '2024-01-15'),
            ('2301003', 3, 50000, 10000, '2024-01-15'),
            ('2301004', 3, 50000, 50000, '2024-01-15'),
            ('2301005', 3, 50000, 5000, '2023-12-15'),
        ]
        cursor.executemany("INSERT INTO fee (roll_no, semester, total_fee, paid_fee, due_date) VALUES (?,?,?,?,?)", 
                          sample_fees)
    
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Session State Management
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'role' not in st.session_state:
    st.session_state.role = None
if 'name' not in st.session_state:
    st.session_state.name = None

# Login Function
def login(username, password):
    """Authenticate user"""
    conn = sqlite3.connect('ums_database.db')
    cursor = conn.cursor()
    
    hashed_pass = hashlib.md5(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM account WHERE username=? AND password=?", (username, hashed_pass))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        st.session_state.logged_in = True
        st.session_state.username = user[0]
        st.session_state.name = user[2]
        st.session_state.role = user[3]
        return True
    return False

# Logout Function
def logout():
    """Logout user"""
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None
    st.session_state.name = None

# Main Application
def main():
    # Login Page - Ultra Compact to Fit Screen
    if not st.session_state.logged_in:
        st.markdown("""
            <style>
                .main {
                    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
                }
                .block-container {
                    max-width: 1350px !important;
                    padding-top: 0.2rem !important;
                    padding-bottom: 0.2rem !important;
                }
            </style>
        """, unsafe_allow_html=True)

        # Very compact header
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<div style='text-align: center; margin-bottom: 8px;'><div style='font-size: 32px; margin-bottom: 4px;'>&#127891;</div><h1 style='color: #2c3e50; font-size: 24px; font-weight: 700; margin: 0;'>University Management System</h1><p style='color: #7f8c8d; font-size: 12px; margin: 3px 0 0 0;'>Smart Education Platform with AI</p></div>", unsafe_allow_html=True)

        st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)

        # Main content - 2 columns
        col_left, col_right = st.columns([1.3, 1])

        with col_left:
            # Feature grid - very compact
            feat_col1, feat_col2 = st.columns(2)

            with feat_col1:
                st.markdown("<div style='background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08); margin-bottom: 12px; border-left: 4px solid #3498db;'><div style='font-size: 30px; margin-bottom: 6px;'>&#128218;</div><h3 style='color: #2c3e50; font-size: 15px; margin: 0 0 4px 0; font-weight: 600;'>Marks Management</h3><p style='color: #7f8c8d; font-size: 11px; margin: 0;'>Track student grades</p></div>", unsafe_allow_html=True)

                st.markdown("<div style='background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08); margin-bottom: 12px; border-left: 4px solid #9b59b6;'><div style='font-size: 30px; margin-bottom: 6px; font-weight: bold; color: #9b59b6;'>AI</div><h3 style='color: #2c3e50; font-size: 15px; margin: 0 0 4px 0; font-weight: 600;'>AI Predictions</h3><p style='color: #7f8c8d; font-size: 11px; margin: 0;'>Smart analytics</p></div>", unsafe_allow_html=True)

            with feat_col2:
                st.markdown("<div style='background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08); margin-bottom: 12px; border-left: 4px solid #2ecc71;'><div style='font-size: 30px; margin-bottom: 6px;'>&#9989;</div><h3 style='color: #2c3e50; font-size: 15px; margin: 0 0 4px 0; font-weight: 600;'>Attendance Tracking</h3><p style='color: #7f8c8d; font-size: 11px; margin: 0;'>Real-time monitoring</p></div>", unsafe_allow_html=True)

                st.markdown("<div style='background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08); margin-bottom: 12px; border-left: 4px solid #e74c3c;'><div style='font-size: 30px; margin-bottom: 6px;'>&#128200;</div><h3 style='color: #2c3e50; font-size: 15px; margin: 0 0 4px 0; font-weight: 600;'>Performance Reports</h3><p style='color: #7f8c8d; font-size: 11px; margin: 0;'>Analytics dashboard</p></div>", unsafe_allow_html=True)

            # Footer - MOVED INSIDE LEFT COLUMN, BELOW THE BOXES!
            st.markdown("<div style='text-align: center; padding: 8px 0; margin-top: 10px; border-top: 1px solid #dfe6e9;'><p style='color: #34495e; font-size: 10px; margin: 1px 0;'>&#169; 2026 University Management System</p><p style='color: #2c3e50; font-size: 12px; margin: 3px 0; font-weight: 700;'>&#10024; Created by Shabbir Ansari &#10024;</p><p style='color: #34495e; font-size: 9px; margin: 1px 0;'>BCA Major Project 2026</p></div>", unsafe_allow_html=True)

        with col_right:
            # Login card - compact
            st.markdown("<div style='background: white; border-radius: 10px; padding: 24px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);'><h2 style='color: #2c3e50; font-size: 20px; font-weight: 700; margin: 0 0 6px 0; text-align: center;'>Welcome Back! 👋</h2><p style='color: #7f8c8d; font-size: 12px; margin: 0 0 18px 0; text-align: center;'>Sign in to your dashboard</p></div>", unsafe_allow_html=True)

            # Use form to enable Enter key support
            with st.form(key="login_form", clear_on_submit=False):
                username = st.text_input("Username", placeholder="Enter your username", key="user_input")
                password = st.text_input("Password", type="password", placeholder="Enter your password", key="pass_input")

                st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

                login_button = st.form_submit_button("LOGIN", use_container_width=True, type="primary")

            if login_button:
                if login(username, password):
                    st.success(f"✅ Login successful! Welcome, {st.session_state.name}!")
                    import time
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials! Please check your username and password.")

            st.markdown("<div style='text-align: center; margin-top: 12px;'><p style='color: #95a5a6; font-size: 10px;'>By continuing, you agree to our Terms</p></div>", unsafe_allow_html=True)

        return
    
    # Main Application (After Login)

    # Top Navigation Bar - Amazon style (FIXED margin)
    st.markdown(f"""
        <div style='background: #232f3e; padding: 12px 20px; margin: -1rem -1rem 20px -1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,.1);'>
            <div style='display: flex; align-items: center; justify-content: space-between;'>
                <div style='display: flex; align-items: center; gap: 25px;'>
                    <div style='font-size: 22px; font-weight: 700; color: #ffffff;'>
                        🎓 UMS
                    </div>
                    <div style='color: #cccccc; font-size: 13px;'>
                        University Management System
                    </div>
                </div>
                <div style='color: #ffffff; font-size: 12px;'>
                    👤 {st.session_state.name} <span style='color: #cccccc;'>({st.session_state.role.upper()})</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar - Clean navigation (FORCE IT TO SHOW)
    with st.sidebar:
        # Force sidebar to be expanded with JavaScript
        st.markdown("""
            <script>
                // Force sidebar to be visible
                const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
                if (sidebar) {
                    sidebar.style.display = 'block';
                    sidebar.style.visibility = 'visible';
                    sidebar.setAttribute('aria-expanded', 'true');
                }
            </script>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style='text-align: center; padding: 15px 0 20px 0; border-bottom: 1px solid #3d4f5f;'>
                <div style='font-size: 18px; font-weight: 600; color: #ffffff;'>📋 Navigation Menu</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

        menu = st.radio("Select Page", [
            "🏠 Dashboard",
            "👨‍🎓 Student Management",
            "👨‍🏫 Teacher Management",
            "📊 Marks Management",
            "💰 Fee Management",
            "✅ Attendance Management",
            "🤖 AI/ML Analytics",
            "📄 Reports & Export",
            "💾 Backup & Restore"
        ], label_visibility="collapsed", key="main_menu")

        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
        st.markdown("<div style='border-top: 1px solid #3d4f5f; padding-top: 15px;'>", unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Dashboard
    if menu == "🏠 Dashboard":
        show_dashboard()
    elif menu == "👨‍🎓 Student Management":
        show_student_management()
    elif menu == "👨‍🏫 Teacher Management":
        show_teacher_management()
    elif menu == "📊 Marks Management":
        show_marks_management()
    elif menu == "💰 Fee Management":
        show_fee_management()
    elif menu == "✅ Attendance Management":
        show_attendance_management()
    elif menu == "🤖 AI/ML Analytics":
        show_ai_analytics()
    elif menu == "📄 Reports & Export":
        show_reports()
    elif menu == "💾 Backup & Restore":
        show_backup_restore()

def show_dashboard():
    """Dashboard with statistics - Flipkart style"""
    # Page header
    st.markdown("""
        <div style='background: #ffffff; padding: 15px 0; margin-bottom: 20px;'>
            <h1 style='color: #212121; font-size: 24px; font-weight: 500; margin: 0;
                font-family: "Roboto", "Amazon Ember", Arial, sans-serif;'>
                Dashboard Overview
            </h1>
        </div>
    """, unsafe_allow_html=True)

    conn = sqlite3.connect('ums_database.db')

    # Get statistics
    total_students = pd.read_sql("SELECT COUNT(*) as count FROM student WHERE status='Active'", conn).iloc[0]['count']
    total_teachers = pd.read_sql("SELECT COUNT(*) as count FROM teacher WHERE status='Active'", conn).iloc[0]['count']

    # Display metrics in cards - Flipkart style
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
            <div style='background: #fff; border: 1px solid #e0e0e0; border-radius: 4px;
                padding: 20px; text-align: center; box-shadow: 0 1px 2px rgba(0,0,0,.05);'>
                <div style='font-size: 32px; color: #2874f0; font-weight: 600;'>{total_students}</div>
                <div style='font-size: 13px; color: #878787; margin-top: 8px;'>👨‍🎓 Total Students</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div style='background: #fff; border: 1px solid #e0e0e0; border-radius: 4px;
                padding: 20px; text-align: center; box-shadow: 0 1px 2px rgba(0,0,0,.05);'>
                <div style='font-size: 32px; color: #388e3c; font-weight: 600;'>{total_teachers}</div>
                <div style='font-size: 13px; color: #878787; margin-top: 8px;'>👨‍🏫 Total Teachers</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        avg_attendance = pd.read_sql("""
            SELECT AVG(attended_classes * 100.0 / total_classes) as avg
            FROM attendance_student WHERE total_classes > 0
        """, conn).iloc[0]['avg']
        st.markdown(f"""
            <div style='background: #fff; border: 1px solid #e0e0e0; border-radius: 4px;
                padding: 20px; text-align: center; box-shadow: 0 1px 2px rgba(0,0,0,.05);'>
                <div style='font-size: 32px; color: #ff6f00; font-weight: 600;'>{avg_attendance:.1f}%</div>
                <div style='font-size: 13px; color: #878787; margin-top: 8px;'>📊 Avg Attendance</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        pending_fees = pd.read_sql("SELECT COUNT(*) as count FROM fee WHERE paid_fee < total_fee", conn).iloc[0]['count']
        st.markdown(f"""
            <div style='background: #fff; border: 1px solid #e0e0e0; border-radius: 4px;
                padding: 20px; text-align: center; box-shadow: 0 1px 2px rgba(0,0,0,.05);'>
                <div style='font-size: 32px; color: #c62828; font-weight: 600;'>{pending_fees}</div>
                <div style='font-size: 13px; color: #878787; margin-top: 8px;'>💰 Pending Fees</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # Charts Section
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Students by Course")
        course_data = pd.read_sql("SELECT course, COUNT(*) as count FROM student WHERE status='Active' GROUP BY course", conn)
        if not course_data.empty:
            fig = px.pie(course_data, values='count', names='course',
                        color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📈 Students by Semester")
        semester_data = pd.read_sql("SELECT semester, COUNT(*) as count FROM student WHERE status='Active' GROUP BY semester ORDER BY semester", conn)
        if not semester_data.empty:
            fig = px.bar(semester_data, x='semester', y='count',
                        color='count', color_continuous_scale='Viridis')
            fig.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0),
                            xaxis_title="Semester", yaxis_title="Students")
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🎯 Attendance Distribution")
        attendance_data = pd.read_sql("""
            SELECT
                CASE
                    WHEN (attended_classes * 100.0 / total_classes) >= 75 THEN '75%+'
                    WHEN (attended_classes * 100.0 / total_classes) >= 60 THEN '60-75%'
                    ELSE 'Below 60%'
                END as range,
                COUNT(*) as count
            FROM attendance_student WHERE total_classes > 0
            GROUP BY range
        """, conn)
        if not attendance_data.empty:
            colors = {'75%+': '#28a745', '60-75%': '#ffc107', 'Below 60%': '#dc3545'}
            fig = px.bar(attendance_data, x='range', y='count',
                        color='range', color_discrete_map=colors)
            fig.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0),
                            xaxis_title="Attendance Range", yaxis_title="Students",
                            showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.subheader("💰 Fee Status")
        fee_data = pd.read_sql("""
            SELECT
                CASE
                    WHEN paid_fee >= total_fee THEN 'Paid'
                    WHEN paid_fee > 0 THEN 'Partial'
                    ELSE 'Pending'
                END as status,
                COUNT(*) as count
            FROM fee
            GROUP BY status
        """, conn)
        if not fee_data.empty:
            colors = {'Paid': '#28a745', 'Partial': '#ffc107', 'Pending': '#dc3545'}
            fig = px.pie(fee_data, values='count', names='status',
                        color='status', color_discrete_map=colors)
            fig.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # Recent Students - Card style
    st.markdown("""
        <div style='background: #fff; border: 1px solid #e0e0e0; border-radius: 4px;
            padding: 20px; box-shadow: 0 1px 2px rgba(0,0,0,.05); margin-bottom: 20px;'>
            <h2 style='color: #212121; font-size: 18px; font-weight: 500; margin: 0 0 15px 0;'>
                📋 Recent Students
            </h2>
        </div>
    """, unsafe_allow_html=True)

    recent_students = pd.read_sql("SELECT roll_no, name, course, semester, status FROM student LIMIT 10", conn)
    st.dataframe(recent_students, use_container_width=True, hide_index=True)

    conn.close()

def show_student_management():
    """Student Management Module"""
    st.title("👨‍🎓 Student Management")

    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Student", "📋 View Students", "✏️ Update Student", "🗑️ Delete Student"])

    conn = sqlite3.connect('ums_database.db')

    # Add Student
    with tab1:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Add New Student")

            # Show success popup if flag is set
            if 'show_student_add_success' in st.session_state and st.session_state.show_student_add_success:
                success_data = st.session_state.show_student_add_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Student Added Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Name: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Course: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Semester: <strong style='color: #28a745;'>{}</strong></p>
                    </div>
                """.format(success_data['roll_no'], success_data['name'], success_data['course'], success_data['semester']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_student_add_success
                st.rerun()

            with st.form("add_student_form"):
                col1, col2 = st.columns(2)
                with col1:
                    roll_no = st.text_input("Roll Number *", placeholder="e.g., 2301001")
                    name = st.text_input("Full Name *")
                    father_name = st.text_input("Father's Name *")
                    dob = st.date_input("Date of Birth")
                    phone = st.text_input("Phone", placeholder="10-digit number")
                    email = st.text_input("Email")
                with col2:
                    course = st.selectbox("Course", ["BCA", "MCA", "B.Tech", "M.Tech"])
                    branch = st.text_input("Branch", value="Computer Science")
                    semester = st.selectbox("Semester", list(range(1, 9)))
                    year = st.number_input("Year", min_value=2020, max_value=2030, value=2023)
                    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                    category = st.selectbox("Category", ["General", "OBC", "SC", "ST"])

                address = st.text_area("Address")
                aadhar = st.text_input("Aadhar Number", placeholder="12-digit number")

                submitted = st.form_submit_button("➕ Add Student")

            if submitted:
                # Validation
                if not roll_no or not name or not father_name:
                    st.error("❌ Please fill all required fields (marked with *)!")
                elif phone and len(phone) != 10:
                    st.error("❌ Phone number must be exactly 10 digits!")
                elif aadhar and len(aadhar) != 12:
                    st.error("❌ Aadhar number must be exactly 12 digits!")
                elif email and '@' not in email:
                    st.error("❌ Please enter a valid email address!")
                else:
                    try:
                        cursor = conn.cursor()
                        cursor.execute("""
                            INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        """, (roll_no, name, father_name, str(dob), address, phone, email, aadhar,
                             course, branch, semester, year, gender, category, 'Active'))
                        conn.commit()

                        # Set flag for showing success popup
                        st.session_state.show_student_add_success = {
                            'roll_no': roll_no,
                            'name': name,
                            'course': course,
                            'semester': semester
                        }
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.error(f"❌ **Failed!** Student with roll number **{roll_no}** already exists!")
                    except Exception as e:
                        st.error(f"❌ **Error:** {str(e)}")

    # View Students
    with tab2:
        st.subheader("All Students")

        # Advanced Search & Filter Section
        with st.expander("🔍 Advanced Search & Filters", expanded=False):
            col1, col2, col3 = st.columns(3)
            with col1:
                search_name = st.text_input("Search by Name", placeholder="Enter name...")
            with col2:
                filter_course = st.selectbox("Filter by Course", ["All", "BCA", "MCA", "B.Tech", "M.Tech"])
            with col3:
                filter_semester = st.selectbox("Filter by Semester", ["All"] + list(range(1, 9)))

            col4, col5 = st.columns(2)
            with col4:
                filter_gender = st.selectbox("Filter by Gender", ["All", "Male", "Female", "Other"])
            with col5:
                filter_status = st.selectbox("Filter by Status", ["All", "Active", "Inactive"])

        # Build query based on filters
        query = "SELECT * FROM student WHERE 1=1"
        if search_name:
            query += f" AND name LIKE '%{search_name}%'"
        if filter_course != "All":
            query += f" AND course='{filter_course}'"
        if filter_semester != "All":
            query += f" AND semester={filter_semester}"
        if filter_gender != "All":
            query += f" AND gender='{filter_gender}'"
        if filter_status != "All":
            query += f" AND status='{filter_status}'"
        query += " ORDER BY roll_no"

        students_df = pd.read_sql(query, conn)

        # Show count
        st.info(f"📊 **Showing {len(students_df)} students**")

        # Display table
        st.dataframe(students_df, use_container_width=True)

        # Download buttons
        col1, col2 = st.columns(2)
        with col1:
            csv = students_df.to_csv(index=False)
            st.download_button("📥 Download CSV", csv, "students.csv", "text/csv", use_container_width=True)
        with col2:
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                students_df.to_excel(writer, index=False, sheet_name='Students')
            st.download_button("📥 Download Excel", buffer.getvalue(), "students.xlsx",
                             "application/vnd.ms-excel", use_container_width=True)

    # Update Student
    with tab3:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Update Student Information")

            # Initialize session state
            if 'student_to_update' not in st.session_state:
                st.session_state.student_to_update = None

            # Search form with Enter key support
            with st.form("search_student_update_form"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    search_roll = st.text_input("Enter Roll Number to Update", key="update_student_roll")
                with col2:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_button = st.form_submit_button("🔍 Search Student", use_container_width=True)

            if search_button:
                if search_roll:
                    student_data = pd.read_sql(f"SELECT * FROM student WHERE roll_no='{search_roll}'", conn)
                    if not student_data.empty:
                        st.session_state.student_to_update = student_data.iloc[0].to_dict()
                        st.session_state.student_to_update['roll_no_searched'] = search_roll
                    else:
                        st.session_state.student_to_update = None
                        st.error(f"❌ Student with Roll Number **{search_roll}** not found!")
                else:
                    st.warning("⚠️ Please enter a Roll Number to search!")

            # Display update form if student found
            if st.session_state.student_to_update:
                student = st.session_state.student_to_update
                st.success(f"✅ Student found: **{student['name']}** ({student['course']})")

                with st.form("update_student_data_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        new_name = st.text_input("Name", value=student['name'])
                        new_phone = st.text_input("Phone", value=student['phone'])
                        new_email = st.text_input("Email", value=student['email'])
                    with col2:
                        new_semester = st.selectbox("Semester", list(range(1, 9)), index=int(student['semester'])-1)
                        new_status = st.selectbox("Status", ["Active", "Inactive"], index=0 if student['status']=='Active' else 1)

                    update_submitted = st.form_submit_button("💾 Update Student", type="primary")

                if update_submitted:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE student SET name=?, phone=?, email=?, semester=?, status=?
                        WHERE roll_no=?
                    """, (new_name, new_phone, new_email, new_semester, new_status, student['roll_no_searched']))
                    conn.commit()

                    # Track what changed
                    changes = []
                    if new_name != student['name']:
                        changes.append(f"Name: {student['name']} → {new_name}")
                    if new_phone != student['phone']:
                        changes.append(f"Phone: {student['phone']} → {new_phone}")
                    if new_email != student['email']:
                        changes.append(f"Email: {student['email']} → {new_email}")
                    if new_semester != student['semester']:
                        changes.append(f"Semester: {student['semester']} → {new_semester}")
                    if new_status != student['status']:
                        changes.append(f"Status: {student['status']} → {new_status}")

                    # Set flag for showing success popup
                    st.session_state.show_student_update_success = {
                        'roll_no': student['roll_no_searched'],
                        'name': new_name,
                        'changes': changes if changes else ['No changes made']
                    }
                    st.session_state.student_to_update = None
                    st.rerun()

            # Show success popup if flag is set
            if 'show_student_update_success' in st.session_state and st.session_state.show_student_update_success:
                success_data = st.session_state.show_student_update_success

                # Build changes HTML
                changes_html = ""
                for change in success_data['changes']:
                    changes_html += f"<p style='color: #2c3e50; font-size: 14px; margin: 8px 0; text-align: left;'>• {change}</p>"

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Student Updated Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0 15px 0;'>Student: <strong style='color: #28a745;'>{}</strong></p>
                        <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 15px 0;'>
                            <p style='color: #495057; font-size: 14px; font-weight: 600; margin: 0 0 10px 0; text-align: left;'>Changes Made:</p>
                            {}
                        </div>
                    </div>
                """.format(success_data['roll_no'], success_data['name'], changes_html), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_student_update_success
                st.rerun()

    # Delete Student
    with tab4:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Delete Student Record")
            st.warning("⚠️ **Warning:** This action cannot be undone!")

            # Initialize session state
            if 'student_to_delete' not in st.session_state:
                st.session_state.student_to_delete = None

            # Search form with Enter key support
            with st.form("search_student_delete_form"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    delete_roll = st.text_input("Enter Roll Number to Delete", key="delete_student_roll")
                with col2:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_delete_button = st.form_submit_button("🔍 Search Student", use_container_width=True)

            if search_delete_button:
                if delete_roll:
                    student_data = pd.read_sql(f"SELECT roll_no, name, course, semester FROM student WHERE roll_no='{delete_roll}'", conn)
                    if not student_data.empty:
                        st.session_state.student_to_delete = student_data.iloc[0].to_dict()
                    else:
                        st.session_state.student_to_delete = None
                        st.error(f"❌ Student with Roll Number **{delete_roll}** not found!")
                else:
                    st.warning("⚠️ Please enter a Roll Number to search!")

            # Display delete confirmation if student found
            if st.session_state.student_to_delete:
                student = st.session_state.student_to_delete
                st.info(f"**Student Found:**\n\n**Name:** {student['name']}\n\n**Roll No:** {student['roll_no']}\n\n**Course:** {student['course']}\n\n**Semester:** {student['semester']}")

                if st.button("🗑️ Confirm Delete", type="primary", use_container_width=True, key="confirm_delete_student"):
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM student WHERE roll_no=?", (student['roll_no'],))
                    cursor.execute("DELETE FROM attendance_student WHERE roll_no=?", (student['roll_no'],))
                    cursor.execute("DELETE FROM marks WHERE roll_no=?", (student['roll_no'],))
                    cursor.execute("DELETE FROM fee WHERE roll_no=?", (student['roll_no'],))
                    conn.commit()

                    # Set flag for showing success popup
                    st.session_state.show_student_delete_success = {
                        'roll_no': student['roll_no'],
                        'name': student['name']
                    }
                    st.session_state.student_to_delete = None
                    st.rerun()

            # Show delete success popup if flag is set
            if 'show_student_delete_success' in st.session_state and st.session_state.show_student_delete_success:
                success_data = st.session_state.show_student_delete_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #dc3545; min-width: 450px; max-width: 500px; text-align: center;'>
                        <h2 style='color: #dc3545; margin: 0 0 25px 0; font-size: 28px;'>🗑️ Deleted!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Student Deleted Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #dc3545;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Name: <strong style='color: #dc3545;'>{}</strong></p>
                    </div>
                """.format(success_data['roll_no'], success_data['name']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_student_delete_success
                st.rerun()

    conn.close()

def show_teacher_management():
    """Teacher Management Module - Full CRUD"""
    st.title("👨‍🏫 Teacher Management")

    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Teacher", "📋 View Teachers", "✏️ Update Teacher", "🗑️ Delete Teacher"])

    conn = sqlite3.connect('ums_database.db')

    # Add Teacher
    with tab1:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Add New Teacher")

            # Show success popup if flag is set
            if 'show_teacher_add_success' in st.session_state and st.session_state.show_teacher_add_success:
                success_data = st.session_state.show_teacher_add_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Teacher Added Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Emp ID: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Name: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Department: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Designation: <strong style='color: #28a745;'>{}</strong></p>
                    </div>
                """.format(success_data['emp_id'], success_data['name'], success_data['department'], success_data['designation']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_teacher_add_success
                st.rerun()

            with st.form("add_teacher_form"):
                col1, col2 = st.columns(2)
                with col1:
                    emp_id = st.text_input("Employee ID *", placeholder="e.g., EMP001")
                    name = st.text_input("Full Name *")
                    phone = st.text_input("Phone", placeholder="10-digit number")
                    email = st.text_input("Email")
                with col2:
                    qualification = st.selectbox("Qualification", ["B.Tech", "M.Tech", "Ph.D", "MCA", "MBA"])
                    department = st.selectbox("Department", ["Computer Science", "IT", "Electronics", "Mechanical"])
                    designation = st.selectbox("Designation", ["Professor", "Associate Professor", "Assistant Professor", "Lecturer"])
                    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

                submitted = st.form_submit_button("👨‍🏫 Add Teacher")

            if submitted:
                # Validation
                if not emp_id or not name:
                    st.error("❌ Please fill all required fields (marked with *)!")
                elif phone and len(phone) != 10:
                    st.error("❌ Phone number must be exactly 10 digits!")
                elif email and '@' not in email:
                    st.error("❌ Please enter a valid email address!")
                else:
                    try:
                        cursor = conn.cursor()
                        cursor.execute("""
                            INSERT INTO teacher (emp_id, name, phone, email, qualification, department, designation, gender, status)
                            VALUES (?,?,?,?,?,?,?,?,?)
                        """, (emp_id, name, phone, email, qualification, department, designation, gender, 'Active'))
                        conn.commit()

                        # Set flag for showing success popup
                        st.session_state.show_teacher_add_success = {
                            'emp_id': emp_id,
                            'name': name,
                            'department': department,
                            'designation': designation
                        }
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.error(f"❌ **Failed!** Teacher with Employee ID **{emp_id}** already exists!")
                    except Exception as e:
                        st.error(f"❌ **Error:** {str(e)}")

    # View Teachers
    with tab2:
        st.subheader("All Teachers")
        teachers_df = pd.read_sql("SELECT * FROM teacher ORDER BY emp_id", conn)
        st.dataframe(teachers_df, use_container_width=True)

        # Download button
        csv = teachers_df.to_csv(index=False)
        st.download_button("📥 Download CSV", csv, "teachers.csv", "text/csv")

    # Update Teacher
    with tab3:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Update Teacher Information")

            # Initialize session state for teacher update
            if 'teacher_to_update' not in st.session_state:
                st.session_state.teacher_to_update = None

            # Search form with Enter key support
            with st.form("search_teacher_update_form"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    search_emp = st.text_input("Enter Employee ID to Update", key="update_emp_search")
                with col2:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_button = st.form_submit_button("🔍 Search Teacher", use_container_width=True)

            if search_button:
                if search_emp:
                    teacher_data = pd.read_sql(f"SELECT * FROM teacher WHERE emp_id='{search_emp}'", conn)
                    if not teacher_data.empty:
                        st.session_state.teacher_to_update = teacher_data.iloc[0].to_dict()
                        st.session_state.teacher_to_update['emp_id_searched'] = search_emp
                    else:
                        st.session_state.teacher_to_update = None
                        st.error(f"❌ Teacher with Employee ID **{search_emp}** not found!")
                else:
                    st.warning("⚠️ Please enter an Employee ID to search!")

            # Display update form if teacher found
            if st.session_state.teacher_to_update:
                teacher = st.session_state.teacher_to_update
                st.success(f"✅ Teacher found: **{teacher['name']}** (Emp ID: {teacher['emp_id_searched']})")

                with st.form("update_teacher_data_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        new_name = st.text_input("Name", value=teacher['name'])
                        new_phone = st.text_input("Phone", value=teacher['phone'])
                        new_email = st.text_input("Email", value=teacher['email'])
                    with col2:
                        new_department = st.selectbox("Department",
                            ["Computer Science", "IT", "Electronics", "Mechanical"],
                            index=["Computer Science", "IT", "Electronics", "Mechanical"].index(teacher['department']) if teacher['department'] in ["Computer Science", "IT", "Electronics", "Mechanical"] else 0)
                        new_designation = st.selectbox("Designation",
                            ["Professor", "Associate Professor", "Assistant Professor", "Lecturer"],
                            index=["Professor", "Associate Professor", "Assistant Professor", "Lecturer"].index(teacher['designation']) if teacher['designation'] in ["Professor", "Associate Professor", "Assistant Professor", "Lecturer"] else 0)
                        new_status = st.selectbox("Status", ["Active", "Inactive"], index=0 if teacher['status']=='Active' else 1)

                    update_submitted = st.form_submit_button("💾 Update Teacher", type="primary")

                if update_submitted:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE teacher SET name=?, phone=?, email=?, department=?, designation=?, status=?
                        WHERE emp_id=?
                    """, (new_name, new_phone, new_email, new_department, new_designation, new_status, teacher['emp_id_searched']))
                    conn.commit()

                    # Track what changed
                    changes = []
                    if new_name != teacher['name']:
                        changes.append(f"Name: {teacher['name']} → {new_name}")
                    if new_phone != teacher['phone']:
                        changes.append(f"Phone: {teacher['phone']} → {new_phone}")
                    if new_email != teacher['email']:
                        changes.append(f"Email: {teacher['email']} → {new_email}")
                    if new_department != teacher['department']:
                        changes.append(f"Department: {teacher['department']} → {new_department}")
                    if new_designation != teacher['designation']:
                        changes.append(f"Designation: {teacher['designation']} → {new_designation}")
                    if new_status != teacher['status']:
                        changes.append(f"Status: {teacher['status']} → {new_status}")

                    # Set flag for showing success popup
                    st.session_state.show_teacher_update_success = {
                        'emp_id': teacher['emp_id_searched'],
                        'name': new_name,
                        'changes': changes if changes else ['No changes made']
                    }
                    st.session_state.teacher_to_update = None
                    st.rerun()

            # Show success popup if flag is set
            if 'show_teacher_update_success' in st.session_state and st.session_state.show_teacher_update_success:
                success_data = st.session_state.show_teacher_update_success

                # Build changes HTML
                changes_html = ""
                for change in success_data['changes']:
                    changes_html += f"<p style='color: #2c3e50; font-size: 14px; margin: 8px 0; text-align: left;'>• {change}</p>"

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Teacher Updated Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Emp ID: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0 15px 0;'>Teacher: <strong style='color: #28a745;'>{}</strong></p>
                        <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 15px 0;'>
                            <p style='color: #495057; font-size: 14px; font-weight: 600; margin: 0 0 10px 0; text-align: left;'>Changes Made:</p>
                            {}
                        </div>
                    </div>
                """.format(success_data['emp_id'], success_data['name'], changes_html), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_teacher_update_success
                st.rerun()

    # Delete Teacher
    with tab4:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Delete Teacher Record")
            st.warning("⚠️ **Warning:** This action cannot be undone!")

            # Initialize session state
            if 'teacher_to_delete' not in st.session_state:
                st.session_state.teacher_to_delete = None

            # Search form with Enter key support
            with st.form("search_teacher_delete_form"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    delete_emp = st.text_input("Enter Employee ID to Delete", key="delete_emp_search")
                with col2:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_delete_button = st.form_submit_button("🔍 Search Teacher", use_container_width=True)

            if search_delete_button:
                if delete_emp:
                    teacher_data = pd.read_sql(f"SELECT emp_id, name, department, designation FROM teacher WHERE emp_id='{delete_emp}'", conn)
                    if not teacher_data.empty:
                        st.session_state.teacher_to_delete = teacher_data.iloc[0].to_dict()
                    else:
                        st.session_state.teacher_to_delete = None
                        st.error(f"❌ Teacher with Employee ID **{delete_emp}** not found!")
                else:
                    st.warning("⚠️ Please enter an Employee ID to search!")

            # Display delete confirmation if teacher found
            if st.session_state.teacher_to_delete:
                teacher = st.session_state.teacher_to_delete
                st.info(f"**Teacher Found:**\n\n**Name:** {teacher['name']}\n\n**Emp ID:** {teacher['emp_id']}\n\n**Department:** {teacher['department']}\n\n**Designation:** {teacher['designation']}")

                if st.button("🗑️ Confirm Delete", type="primary", use_container_width=True, key="confirm_delete_teacher"):
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM teacher WHERE emp_id=?", (teacher['emp_id'],))
                    conn.commit()

                    # Set flag for showing success popup
                    st.session_state.show_teacher_delete_success = {
                        'emp_id': teacher['emp_id'],
                        'name': teacher['name']
                    }
                    st.session_state.teacher_to_delete = None
                    st.rerun()

            # Show delete success popup if flag is set
            if 'show_teacher_delete_success' in st.session_state and st.session_state.show_teacher_delete_success:
                success_data = st.session_state.show_teacher_delete_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #dc3545; min-width: 450px; max-width: 500px; text-align: center;'>
                        <h2 style='color: #dc3545; margin: 0 0 25px 0; font-size: 28px;'>🗑️ Deleted!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Teacher Deleted Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Emp ID: <strong style='color: #dc3545;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Name: <strong style='color: #dc3545;'>{}</strong></p>
                    </div>
                """.format(success_data['emp_id'], success_data['name']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_teacher_delete_success
                st.rerun()

    conn.close()

def show_marks_management():
    """Marks Management Module - Full CRUD"""
    st.title("📊 Marks Management")

    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Marks", "📋 View Marks", "✏️ Update Marks", "🗑️ Delete Marks"])

    conn = sqlite3.connect('ums_database.db')

    with tab1:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Enter Student Marks")

            # Show success popup if flag is set
            if 'show_marks_add_success' in st.session_state and st.session_state.show_marks_add_success:
                success_data = st.session_state.show_marks_add_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Marks Added Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Subject: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Total: <strong style='color: #28a745;'>{}/100</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Grade: <strong style='color: #28a745;'>{}</strong></p>
                    </div>
                """.format(success_data['roll_no'], success_data['subject'], success_data['total'], success_data['grade']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_marks_add_success
                st.rerun()

            with st.form("marks_form"):
                roll_no = st.text_input("Roll Number *", placeholder="e.g., 2301001")
                subject = st.selectbox("Subject", ["BCA101", "BCA102", "BCA103", "BCA201", "BCA202", "BCA301"])
                semester = st.selectbox("Semester", list(range(1, 9)))
                col1, col2 = st.columns(2)
                with col1:
                    internal = st.number_input("Internal Marks (Max 30)", min_value=0, max_value=30)
                with col2:
                    external = st.number_input("External Marks (Max 70)", min_value=0, max_value=70)

                total = internal + external
                if total >= 85: grade = "A"
                elif total >= 70: grade = "B"
                elif total >= 55: grade = "C"
                elif total >= 40: grade = "D"
                else: grade = "F"

                st.info(f"📊 Total: {total}/100 | Grade: **{grade}**")

                submitted = st.form_submit_button("📝 Add Marks")

            if submitted:
                # Validation
                if not roll_no:
                    st.error("❌ Please enter Roll Number!")
                else:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("""
                            INSERT INTO marks (roll_no, subject_code, semester, internal_marks, external_marks)
                            VALUES (?,?,?,?,?)
                        """, (roll_no, subject, semester, internal, external))
                        conn.commit()

                        # Set flag for showing success popup
                        st.session_state.show_marks_add_success = {
                            'roll_no': roll_no,
                            'subject': subject,
                            'total': total,
                            'grade': grade
                        }
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.error(f"❌ **Failed!** Marks already exist for this student and subject!")
                    except Exception as e:
                        st.error(f"❌ **Error:** {str(e)}")

    # View Marks
    with tab2:
        st.subheader("All Marks")
        marks_df = pd.read_sql("""
            SELECT m.*, s.name,
                   (m.internal_marks + m.external_marks) as total,
                   CASE
                       WHEN (m.internal_marks + m.external_marks) >= 85 THEN 'A'
                       WHEN (m.internal_marks + m.external_marks) >= 70 THEN 'B'
                       WHEN (m.internal_marks + m.external_marks) >= 55 THEN 'C'
                       WHEN (m.internal_marks + m.external_marks) >= 40 THEN 'D'
                       ELSE 'F'
                   END as grade
            FROM marks m
            JOIN student s ON m.roll_no = s.roll_no
            ORDER BY m.roll_no
        """, conn)
        st.dataframe(marks_df, use_container_width=True)

        # Download button
        csv = marks_df.to_csv(index=False)
        st.download_button("📥 Download CSV", csv, "marks.csv", "text/csv")

    # Update Marks
    with tab3:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Update Student Marks")

            # Initialize session state
            if 'marks_to_update' not in st.session_state:
                st.session_state.marks_to_update = None

            # Search form with Enter key support
            with st.form("search_marks_update_form"):
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    search_roll = st.text_input("Enter Roll Number", key="update_marks_roll")
                with col2:
                    search_subject = st.selectbox("Select Subject", ["BCA101", "BCA102", "BCA103", "BCA201", "BCA202", "BCA301"], key="update_marks_subject")
                with col3:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_marks_button = st.form_submit_button("🔍 Search", use_container_width=True)

            if search_marks_button:
                if search_roll and search_subject:
                    marks_data = pd.read_sql(f"SELECT m.*, s.name FROM marks m JOIN student s ON m.roll_no = s.roll_no WHERE m.roll_no='{search_roll}' AND m.subject_code='{search_subject}'", conn)
                    if not marks_data.empty:
                        st.session_state.marks_to_update = marks_data.iloc[0].to_dict()
                        st.session_state.marks_to_update['roll_searched'] = search_roll
                        st.session_state.marks_to_update['subject_searched'] = search_subject
                    else:
                        st.session_state.marks_to_update = None
                        st.error(f"❌ No marks record found for Roll No **{search_roll}** and Subject **{search_subject}**!")
                else:
                    st.warning("⚠️ Please enter Roll Number and select Subject!")

            # Display update form if marks found
            if st.session_state.marks_to_update:
                marks = st.session_state.marks_to_update
                current_total = int(marks['internal_marks']) + int(marks['external_marks'])
                st.success(f"✅ Marks found for **{marks['name']}** | Current Total: **{current_total}/100**")

                with st.form("update_marks_data_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        new_internal = st.number_input("Internal Marks (Max 30)", min_value=0, max_value=30, value=int(marks['internal_marks']))
                    with col2:
                        new_external = st.number_input("External Marks (Max 70)", min_value=0, max_value=70, value=int(marks['external_marks']))

                    new_total = new_internal + new_external
                    if new_total >= 85: new_grade = "A"
                    elif new_total >= 70: new_grade = "B"
                    elif new_total >= 55: new_grade = "C"
                    elif new_total >= 40: new_grade = "D"
                    else: new_grade = "F"

                    st.info(f"📊 New Total: {new_total}/100 | Grade: **{new_grade}**")

                    update_marks_submitted = st.form_submit_button("💾 Update Marks", type="primary")

                if update_marks_submitted:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE marks SET internal_marks=?, external_marks=?
                        WHERE roll_no=? AND subject_code=?
                    """, (new_internal, new_external, marks['roll_searched'], marks['subject_searched']))
                    conn.commit()

                    # Track what changed
                    changes = []
                    if new_internal != int(marks['internal_marks']):
                        changes.append(f"Internal Marks: {int(marks['internal_marks'])} → {new_internal}")
                    if new_external != int(marks['external_marks']):
                        changes.append(f"External Marks: {int(marks['external_marks'])} → {new_external}")
                    if changes:
                        old_total = int(marks['internal_marks']) + int(marks['external_marks'])
                        changes.append(f"Total: {old_total} → {new_total}")
                        old_grade = "A" if old_total >= 85 else "B" if old_total >= 70 else "C" if old_total >= 55 else "D" if old_total >= 40 else "F"
                        if old_grade != new_grade:
                            changes.append(f"Grade: {old_grade} → {new_grade}")

                    # Set flag for showing success popup
                    st.session_state.show_marks_update_success = {
                        'roll_no': marks['roll_searched'],
                        'name': marks['name'],
                        'subject': marks['subject_searched'],
                        'changes': changes if changes else ['No changes made']
                    }
                    st.session_state.marks_to_update = None
                    st.rerun()

            # Show success popup if flag is set
            if 'show_marks_update_success' in st.session_state and st.session_state.show_marks_update_success:
                success_data = st.session_state.show_marks_update_success

                # Build changes HTML
                changes_html = ""
                for change in success_data['changes']:
                    changes_html += f"<p style='color: #2c3e50; font-size: 14px; margin: 8px 0; text-align: left;'>• {change}</p>"

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Marks Updated Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Student: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0 15px 0;'>Subject: <strong style='color: #28a745;'>{}</strong></p>
                        <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 15px 0;'>
                            <p style='color: #495057; font-size: 14px; font-weight: 600; margin: 0 0 10px 0; text-align: left;'>Changes Made:</p>
                            {}
                        </div>
                    </div>
                """.format(success_data['roll_no'], success_data['name'], success_data['subject'], changes_html), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_marks_update_success
                st.rerun()

    # Delete Marks
    with tab4:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Delete Marks Record")
            st.warning("⚠️ **Warning:** This action cannot be undone!")

            # Initialize session state
            if 'marks_to_delete' not in st.session_state:
                st.session_state.marks_to_delete = None

            # Search form with Enter key support
            with st.form("search_marks_delete_form"):
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    delete_roll = st.text_input("Roll Number to Delete", key="delete_marks_roll")
                with col2:
                    delete_subject = st.selectbox("Subject to Delete", ["BCA101", "BCA102", "BCA103", "BCA201", "BCA202", "BCA301"], key="delete_marks_subject")
                with col3:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_delete_marks_button = st.form_submit_button("🔍 Search", use_container_width=True)

            if search_delete_marks_button:
                if delete_roll and delete_subject:
                    marks_data = pd.read_sql(f"""
                        SELECT m.*, s.name, (m.internal_marks + m.external_marks) as total
                        FROM marks m
                        JOIN student s ON m.roll_no = s.roll_no
                        WHERE m.roll_no='{delete_roll}' AND m.subject_code='{delete_subject}'
                    """, conn)
                    if not marks_data.empty:
                        st.session_state.marks_to_delete = marks_data.iloc[0].to_dict()
                    else:
                        st.session_state.marks_to_delete = None
                        st.error(f"❌ No marks record found for Roll No **{delete_roll}** and Subject **{delete_subject}**!")
                else:
                    st.warning("⚠️ Please enter Roll Number!")

            # Display delete confirmation if marks found
            if st.session_state.marks_to_delete:
                record = st.session_state.marks_to_delete
                st.info(f"**Marks Record Found:**\n\n**Student:** {record['name']}\n\n**Roll No:** {record['roll_no']}\n\n**Subject:** {record['subject_code']}\n\n**Internal:** {record['internal_marks']}/30 | **External:** {record['external_marks']}/70\n\n**Total:** {record['total']}/100")

                if st.button("🗑️ Confirm Delete", type="primary", use_container_width=True, key="confirm_delete_marks"):
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM marks WHERE roll_no=? AND subject_code=?", (record['roll_no'], record['subject_code']))
                    conn.commit()

                    # Set flag for showing success popup
                    st.session_state.show_marks_delete_success = {
                        'roll_no': record['roll_no'],
                        'name': record['name'],
                        'subject': record['subject_code']
                    }
                    st.session_state.marks_to_delete = None
                    st.rerun()

            # Show delete success popup if flag is set
            if 'show_marks_delete_success' in st.session_state and st.session_state.show_marks_delete_success:
                success_data = st.session_state.show_marks_delete_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #dc3545; min-width: 450px; max-width: 500px; text-align: center;'>
                        <h2 style='color: #dc3545; margin: 0 0 25px 0; font-size: 28px;'>🗑️ Deleted!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Marks Record Deleted Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #dc3545;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Student: <strong style='color: #dc3545;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Subject: <strong style='color: #dc3545;'>{}</strong></p>
                    </div>
                """.format(success_data['roll_no'], success_data['name'], success_data['subject']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_marks_delete_success
                st.rerun()

    conn.close()

def show_fee_management():
    """Fee Management Module - Full CRUD"""
    st.title("💰 Fee Management")

    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Fee Record", "📋 View Fees", "✏️ Update Fee", "🗑️ Delete Fee"])

    conn = sqlite3.connect('ums_database.db')

    with tab1:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Record Fee Payment")

            # Show success popup if flag is set
            if 'show_fee_add_success' in st.session_state and st.session_state.show_fee_add_success:
                success_data = st.session_state.show_fee_add_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Fee Record Added Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Semester: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Total Fee: <strong style='color: #28a745;'>₹{:,}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Paid: <strong style='color: #28a745;'>₹{:,}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Pending: <strong style='color: #dc3545;'>₹{:,}</strong></p>
                    </div>
                """.format(success_data['roll_no'], success_data['semester'], success_data['total_fee'],
                          success_data['paid_fee'], success_data['pending']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_fee_add_success
                st.rerun()

            with st.form("fee_form"):
                roll_no = st.text_input("Roll Number *", placeholder="e.g., 2301001")
                semester = st.selectbox("Semester", list(range(1, 9)))
                col1, col2 = st.columns(2)
                with col1:
                    total_fee = st.number_input("Total Fee (₹)", min_value=0, value=50000, step=1000)
                with col2:
                    paid_fee = st.number_input("Paid Fee (₹)", min_value=0, value=0, step=1000)

                due_date = st.date_input("Due Date")

                pending = total_fee - paid_fee
                status = "✅ Paid" if paid_fee >= total_fee else "⚠️ Partial" if paid_fee > 0 else "❌ Pending"

                st.info(f"Pending: ₹{pending:,} | Status: {status}")

                submitted = st.form_submit_button("💰 Add Fee Record")

            if submitted:
                # Validation
                if not roll_no:
                    st.error("❌ Please enter Roll Number!")
                elif paid_fee > total_fee:
                    st.error("❌ Paid fee cannot be greater than total fee!")
                else:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("""
                            INSERT INTO fee (roll_no, semester, total_fee, paid_fee, due_date)
                            VALUES (?,?,?,?,?)
                        """, (roll_no, semester, total_fee, paid_fee, str(due_date)))
                        conn.commit()

                        # Set flag for showing success popup
                        st.session_state.show_fee_add_success = {
                            'roll_no': roll_no,
                            'semester': semester,
                            'total_fee': total_fee,
                            'paid_fee': paid_fee,
                            'pending': pending
                        }
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.error(f"❌ **Failed!** Fee record already exists for this student and semester!")
                    except Exception as e:
                        st.error(f"❌ **Error:** {str(e)}")

    # View Fees
    with tab2:
        st.subheader("All Fee Records")
        fees_df = pd.read_sql("""
            SELECT f.*, s.name,
                   (f.total_fee - f.paid_fee) as pending
            FROM fee f
            JOIN student s ON f.roll_no = s.roll_no
            ORDER BY f.due_date
        """, conn)
        st.dataframe(fees_df, use_container_width=True)

        # Download button
        csv = fees_df.to_csv(index=False)
        st.download_button("📥 Download CSV", csv, "fees.csv", "text/csv")

    # Update Fee
    with tab3:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Update Fee Payment")

            # Initialize session state
            if 'fee_to_update' not in st.session_state:
                st.session_state.fee_to_update = None

            # Search form with Enter key support
            with st.form("search_fee_update_form"):
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    search_roll = st.text_input("Enter Roll Number", key="update_fee_roll")
                with col2:
                    search_semester = st.selectbox("Select Semester", list(range(1, 9)), key="update_fee_semester")
                with col3:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_fee_button = st.form_submit_button("🔍 Search", use_container_width=True)

            if search_fee_button:
                if search_roll:
                    fee_data = pd.read_sql(f"SELECT f.*, s.name FROM fee f JOIN student s ON f.roll_no = s.roll_no WHERE f.roll_no='{search_roll}' AND f.semester={search_semester}", conn)
                    if not fee_data.empty:
                        st.session_state.fee_to_update = fee_data.iloc[0].to_dict()
                        st.session_state.fee_to_update['roll_searched'] = search_roll
                        st.session_state.fee_to_update['semester_searched'] = search_semester
                    else:
                        st.session_state.fee_to_update = None
                        st.error(f"❌ No fee record found for Roll No **{search_roll}** and Semester **{search_semester}**!")
                else:
                    st.warning("⚠️ Please enter a Roll Number!")

            # Display update form if fee found
            if st.session_state.fee_to_update:
                fee = st.session_state.fee_to_update
                current_pending = int(fee['total_fee']) - int(fee['paid_fee'])
                st.success(f"✅ Fee record found for **{fee['name']}** | Pending: **₹{current_pending:,}**")

                with st.form("update_fee_data_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        new_total_fee = st.number_input("Total Fee (₹)", min_value=0, value=int(fee['total_fee']), step=1000)
                    with col2:
                        new_paid_fee = st.number_input("Paid Fee (₹)", min_value=0, value=int(fee['paid_fee']), step=1000)

                    new_due_date = st.date_input("Due Date", value=pd.to_datetime(fee['due_date']))

                    new_pending = new_total_fee - new_paid_fee
                    new_status = "✅ Paid" if new_paid_fee >= new_total_fee else "⚠️ Partial" if new_paid_fee > 0 else "❌ Pending"

                    st.info(f"Pending: ₹{new_pending:,} | Status: {new_status}")

                    update_fee_submitted = st.form_submit_button("💾 Update Fee", type="primary")

                if update_fee_submitted:
                    # Validation
                    if new_paid_fee > new_total_fee:
                        st.error("❌ Paid fee cannot be greater than total fee!")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("""
                            UPDATE fee SET total_fee=?, paid_fee=?, due_date=?
                            WHERE roll_no=? AND semester=?
                        """, (new_total_fee, new_paid_fee, str(new_due_date), fee['roll_searched'], fee['semester_searched']))
                        conn.commit()

                        # Track what changed
                        changes = []
                        if new_total_fee != int(fee['total_fee']):
                            changes.append(f"Total Fee: ₹{int(fee['total_fee']):,} → ₹{new_total_fee:,}")
                        if new_paid_fee != int(fee['paid_fee']):
                            changes.append(f"Paid Fee: ₹{int(fee['paid_fee']):,} → ₹{new_paid_fee:,}")
                        if str(new_due_date) != str(fee['due_date']):
                            changes.append(f"Due Date: {fee['due_date']} → {new_due_date}")
                        if changes:
                            old_pending = int(fee['total_fee']) - int(fee['paid_fee'])
                            if new_pending != old_pending:
                                changes.append(f"Pending: ₹{old_pending:,} → ₹{new_pending:,}")

                        # Set flag for showing success popup
                        st.session_state.show_fee_update_success = {
                            'roll_no': fee['roll_searched'],
                            'name': fee['name'],
                            'semester': fee['semester_searched'],
                            'changes': changes if changes else ['No changes made']
                        }
                        st.session_state.fee_to_update = None
                        st.rerun()

            # Show success popup if flag is set
            if 'show_fee_update_success' in st.session_state and st.session_state.show_fee_update_success:
                success_data = st.session_state.show_fee_update_success

                # Build changes HTML
                changes_html = ""
                for change in success_data['changes']:
                    changes_html += f"<p style='color: #2c3e50; font-size: 14px; margin: 8px 0; text-align: left;'>• {change}</p>"

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Fee Record Updated Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Student: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0 15px 0;'>Semester: <strong style='color: #28a745;'>{}</strong></p>
                        <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 15px 0;'>
                            <p style='color: #495057; font-size: 14px; font-weight: 600; margin: 0 0 10px 0; text-align: left;'>Changes Made:</p>
                            {}
                        </div>
                    </div>
                """.format(success_data['roll_no'], success_data['name'], success_data['semester'], changes_html), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_fee_update_success
                st.rerun()

    # Delete Fee
    with tab4:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Delete Fee Record")
            st.warning("⚠️ **Warning:** This action cannot be undone!")

            # Initialize session state
            if 'fee_to_delete' not in st.session_state:
                st.session_state.fee_to_delete = None

            # Search form with Enter key support
            with st.form("search_fee_delete_form"):
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    delete_roll = st.text_input("Roll Number", key="delete_fee_roll")
                with col2:
                    delete_semester = st.selectbox("Semester", list(range(1, 9)), key="delete_fee_semester")
                with col3:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_delete_fee_button = st.form_submit_button("🔍 Search", use_container_width=True)

            if search_delete_fee_button:
                if delete_roll:
                    fee_data = pd.read_sql(f"""
                        SELECT f.*, s.name, (f.total_fee - f.paid_fee) as pending
                        FROM fee f
                        JOIN student s ON f.roll_no = s.roll_no
                        WHERE f.roll_no='{delete_roll}' AND f.semester={delete_semester}
                    """, conn)
                    if not fee_data.empty:
                        st.session_state.fee_to_delete = fee_data.iloc[0].to_dict()
                    else:
                        st.session_state.fee_to_delete = None
                        st.error(f"❌ No fee record found for Roll No **{delete_roll}** and Semester **{delete_semester}**!")
                else:
                    st.warning("⚠️ Please enter a Roll Number!")

            # Display delete confirmation if fee found
            if st.session_state.fee_to_delete:
                record = st.session_state.fee_to_delete
                st.info(f"**Fee Record Found:**\n\n**Student:** {record['name']}\n\n**Roll No:** {record['roll_no']}\n\n**Semester:** {record['semester']}\n\n**Total Fee:** ₹{record['total_fee']:,}\n\n**Paid:** ₹{record['paid_fee']:,}\n\n**Pending:** ₹{record['pending']:,}")

                if st.button("🗑️ Confirm Delete", type="primary", use_container_width=True, key="confirm_delete_fee"):
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM fee WHERE roll_no=? AND semester=?", (record['roll_no'], record['semester']))
                    conn.commit()

                    # Set flag for showing success popup
                    st.session_state.show_fee_delete_success = {
                        'roll_no': record['roll_no'],
                        'name': record['name'],
                        'semester': record['semester']
                    }
                    st.session_state.fee_to_delete = None
                    st.rerun()

            # Show delete success popup if flag is set
            if 'show_fee_delete_success' in st.session_state and st.session_state.show_fee_delete_success:
                success_data = st.session_state.show_fee_delete_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #dc3545; min-width: 450px; max-width: 500px; text-align: center;'>
                        <h2 style='color: #dc3545; margin: 0 0 25px 0; font-size: 28px;'>🗑️ Deleted!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Fee Record Deleted Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #dc3545;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Student: <strong style='color: #dc3545;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Semester: <strong style='color: #dc3545;'>{}</strong></p>
                    </div>
                """.format(success_data['roll_no'], success_data['name'], success_data['semester']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_fee_delete_success
                st.rerun()

    conn.close()

def show_attendance_management():
    """Attendance Management Module"""
    st.title("✅ Attendance Management")

    tab1, tab2, tab3 = st.tabs(["➕ Mark Attendance", "📋 View Attendance", "✏️ Update Attendance"])

    conn = sqlite3.connect('ums_database.db')

    with tab1:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Record Student Attendance")

            # Show success popup if flag is set
            if 'show_attendance_add_success' in st.session_state and st.session_state.show_attendance_add_success:
                success_data = st.session_state.show_attendance_add_success

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Attendance Recorded Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Semester: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Attended: <strong style='color: #28a745;'>{}/{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Percentage: <strong style='color: #28a745;'>{:.2f}%</strong></p>
                    </div>
                """.format(success_data['roll_no'], success_data['semester'], success_data['attended'],
                          success_data['total'], success_data['percentage']), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_attendance_add_success
                st.rerun()

            with st.form("attendance_form"):
                roll_no = st.text_input("Roll Number *", placeholder="e.g., 2301001")
                semester = st.selectbox("Semester", list(range(1, 9)))
                col1, col2 = st.columns(2)
                with col1:
                    total_classes = st.number_input("Total Classes", min_value=1, value=100)
                with col2:
                    attended = st.number_input("Classes Attended", min_value=0, value=0)

                percentage = (attended / total_classes * 100) if total_classes > 0 else 0
                status = "✅ Good" if percentage >= 75 else "⚠️ Warning" if percentage >= 60 else "❌ Critical"

                st.metric("Attendance Percentage", f"{percentage:.2f}%", delta=status)

                submitted = st.form_submit_button("✅ Mark Attendance")

            if submitted:
                # Validation
                if not roll_no:
                    st.error("❌ Please enter Roll Number!")
                elif attended > total_classes:
                    st.error("❌ Classes attended cannot be greater than total classes!")
                else:
                    cursor = conn.cursor()
                    try:
                        # Check if record exists
                        cursor.execute("SELECT id FROM attendance_student WHERE roll_no=? AND semester=?", (roll_no, semester))
                        existing = cursor.fetchone()

                        if existing:
                            st.warning("⚠️ Attendance record already exists! Please use 'Update Attendance' tab to modify.")
                        else:
                            cursor.execute("""
                                INSERT INTO attendance_student (roll_no, semester, total_classes, attended_classes)
                                VALUES (?,?,?,?)
                            """, (roll_no, semester, total_classes, attended))
                            conn.commit()

                            # Set flag for showing success popup
                            st.session_state.show_attendance_add_success = {
                                'roll_no': roll_no,
                                'semester': semester,
                                'attended': attended,
                                'total': total_classes,
                                'percentage': percentage
                            }
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ **Error:** {str(e)}")

    with tab2:
        st.subheader("Attendance Records")
        attendance_df = pd.read_sql("""
            SELECT a.*, s.name,
                   (a.attended_classes * 100.0 / a.total_classes) as percentage
            FROM attendance_student a
            JOIN student s ON a.roll_no = s.roll_no
            ORDER BY percentage DESC
        """, conn)
        st.dataframe(attendance_df, use_container_width=True)

    # Update Attendance
    with tab3:
        if st.session_state.role != 'admin':
            st.warning("⚠️ Admin access required!")
        else:
            st.subheader("Update Student Attendance")

            # Initialize session state
            if 'attendance_to_update' not in st.session_state:
                st.session_state.attendance_to_update = None

            # Search form with Enter key support
            with st.form("search_attendance_update_form"):
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    search_roll = st.text_input("Enter Roll Number", key="update_attendance_roll")
                with col2:
                    search_semester = st.selectbox("Select Semester", list(range(1, 9)), key="update_attendance_semester")
                with col3:
                    st.markdown("<div style='height: 31px;'></div>", unsafe_allow_html=True)
                    search_attendance_button = st.form_submit_button("🔍 Search", use_container_width=True)

            if search_attendance_button:
                if search_roll:
                    attendance_data = pd.read_sql(f"SELECT a.*, s.name FROM attendance_student a JOIN student s ON a.roll_no = s.roll_no WHERE a.roll_no='{search_roll}' AND a.semester={search_semester}", conn)
                    if not attendance_data.empty:
                        st.session_state.attendance_to_update = attendance_data.iloc[0].to_dict()
                        st.session_state.attendance_to_update['roll_searched'] = search_roll
                        st.session_state.attendance_to_update['semester_searched'] = search_semester
                    else:
                        st.session_state.attendance_to_update = None
                        st.error(f"❌ No attendance record found for Roll No **{search_roll}** and Semester **{search_semester}**!")
                else:
                    st.warning("⚠️ Please enter a Roll Number!")

            # Display update form if attendance found
            if st.session_state.attendance_to_update:
                att = st.session_state.attendance_to_update
                current_percentage = (int(att['attended_classes']) / int(att['total_classes']) * 100) if int(att['total_classes']) > 0 else 0
                st.success(f"✅ Attendance found for **{att['name']}** | Current: **{int(att['attended_classes'])}/{int(att['total_classes'])}** ({current_percentage:.2f}%)")

                with st.form("update_attendance_data_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        new_total_classes = st.number_input("Total Classes", min_value=1, value=int(att['total_classes']))
                    with col2:
                        new_attended = st.number_input("Classes Attended", min_value=0, value=int(att['attended_classes']))

                    new_percentage = (new_attended / new_total_classes * 100) if new_total_classes > 0 else 0
                    new_status = "✅ Good" if new_percentage >= 75 else "⚠️ Warning" if new_percentage >= 60 else "❌ Critical"

                    st.metric("New Attendance Percentage", f"{new_percentage:.2f}%", delta=new_status)

                    update_attendance_submitted = st.form_submit_button("💾 Update Attendance", type="primary")

                if update_attendance_submitted:
                    # Validation
                    if new_attended > new_total_classes:
                        st.error("❌ Classes attended cannot be greater than total classes!")
                    else:
                        cursor = conn.cursor()
                        cursor.execute("""
                            UPDATE attendance_student SET total_classes=?, attended_classes=?
                            WHERE roll_no=? AND semester=?
                        """, (new_total_classes, new_attended, att['roll_searched'], att['semester_searched']))
                        conn.commit()

                        # Track what changed
                        changes = []
                        if new_total_classes != int(att['total_classes']):
                            changes.append(f"Total Classes: {int(att['total_classes'])} → {new_total_classes}")
                        if new_attended != int(att['attended_classes']):
                            changes.append(f"Attended: {int(att['attended_classes'])} → {new_attended}")
                        if changes:
                            old_percentage = (int(att['attended_classes']) / int(att['total_classes']) * 100) if int(att['total_classes']) > 0 else 0
                            if abs(new_percentage - old_percentage) > 0.01:
                                changes.append(f"Percentage: {old_percentage:.2f}% → {new_percentage:.2f}%")

                        # Set flag for showing success popup
                        st.session_state.show_attendance_update_success = {
                            'roll_no': att['roll_searched'],
                            'name': att['name'],
                            'semester': att['semester_searched'],
                            'changes': changes if changes else ['No changes made']
                        }
                        st.session_state.attendance_to_update = None
                        st.rerun()

            # Show success popup if flag is set
            if 'show_attendance_update_success' in st.session_state and st.session_state.show_attendance_update_success:
                success_data = st.session_state.show_attendance_update_success

                # Build changes HTML
                changes_html = ""
                for change in success_data['changes']:
                    changes_html += f"<p style='color: #2c3e50; font-size: 14px; margin: 8px 0; text-align: left;'>• {change}</p>"

                # Full-screen overlay with modal
                st.markdown("""
                    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                        background: rgba(0,0,0,0.5); z-index: 999998;'></div>
                    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        z-index: 999999; background: white; padding: 40px 50px;
                        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.4);
                        border: 4px solid #28a745; min-width: 500px; max-width: 600px; text-align: center;'>
                        <h2 style='color: #28a745; margin: 0 0 25px 0; font-size: 28px;'>✅ Success!</h2>
                        <p style='color: #2c3e50; font-size: 18px; margin: 15px 0; font-weight: 600;'>Attendance Updated Successfully!</p>
                        <hr style='border: 1px solid #e0e0e0; margin: 20px 0;'>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Roll No: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0;'>Student: <strong style='color: #28a745;'>{}</strong></p>
                        <p style='color: #2c3e50; font-size: 15px; margin: 10px 0 15px 0;'>Semester: <strong style='color: #28a745;'>{}</strong></p>
                        <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 15px 0;'>
                            <p style='color: #495057; font-size: 14px; font-weight: 600; margin: 0 0 10px 0; text-align: left;'>Changes Made:</p>
                            {}
                        </div>
                    </div>
                """.format(success_data['roll_no'], success_data['name'], success_data['semester'], changes_html), unsafe_allow_html=True)

                # Auto-close after 5 seconds
                import time
                time.sleep(5)
                del st.session_state.show_attendance_update_success
                st.rerun()

    conn.close()

def show_ai_analytics():
    """AI/ML Analytics Dashboard"""
    st.title("🤖 AI/ML Analytics Dashboard")

    conn = sqlite3.connect('ums_database.db')

    # Select Analysis Type
    analysis_type = st.selectbox("📊 Select Analysis", [
        "🎯 Student Performance Prediction",
        "📊 Attendance Pattern Analysis",
        "💰 Fee Defaulter Prediction",
        "📈 Grade Prediction"
    ])

    st.markdown("---")

    # Performance Prediction
    if "Performance" in analysis_type:
        st.subheader("🎯 Student Performance Prediction")
        st.info("Identifies at-risk students based on attendance and marks")

        predictions_df = pd.read_sql("""
            SELECT s.roll_no, s.name, s.semester,
                   COALESCE(AVG((a.attended_classes * 100.0 / a.total_classes)), 0) as attendance_percent,
                   COALESCE(AVG(m.internal_marks + m.external_marks), 0) as avg_marks
            FROM student s
            LEFT JOIN attendance_student a ON s.roll_no = a.roll_no
            LEFT JOIN marks m ON s.roll_no = m.roll_no
            WHERE s.status = 'Active'
            GROUP BY s.roll_no, s.name, s.semester
        """, conn)

        # Calculate risk
        def calculate_risk(row):
            risk_score = 0
            factors = []

            if row['attendance_percent'] < 60:
                risk_score += 40
                factors.append("Very Low Attendance")
            elif row['attendance_percent'] < 75:
                risk_score += 20
                factors.append("Low Attendance")

            if row['avg_marks'] < 40:
                risk_score += 40
                factors.append("Failing Marks")
            elif row['avg_marks'] < 55:
                risk_score += 20
                factors.append("Below Average")

            if risk_score >= 50:
                return "🔴 High Risk", risk_score, ", ".join(factors) if factors else "None"
            elif risk_score >= 25:
                return "🟠 Medium Risk", risk_score, ", ".join(factors) if factors else "None"
            else:
                return "🟢 Low Risk", risk_score, ", ".join(factors) if factors else "None"

        predictions_df[['risk_level', 'risk_score', 'risk_factors']] = predictions_df.apply(
            calculate_risk, axis=1, result_type='expand'
        )

        st.dataframe(predictions_df, use_container_width=True)

        # Summary
        col1, col2, col3 = st.columns(3)
        with col1:
            high_risk = len(predictions_df[predictions_df['risk_level'] == '🔴 High Risk'])
            st.metric("High Risk Students", high_risk, delta="⚠️")
        with col2:
            medium_risk = len(predictions_df[predictions_df['risk_level'] == '🟠 Medium Risk'])
            st.metric("Medium Risk Students", medium_risk)
        with col3:
            low_risk = len(predictions_df[predictions_df['risk_level'] == '🟢 Low Risk'])
            st.metric("Low Risk Students", low_risk, delta="✅")

    # Attendance Analysis
    elif "Attendance" in analysis_type:
        st.subheader("📊 Attendance Pattern Analysis")

        attendance_df = pd.read_sql("""
            SELECT s.roll_no, s.name, s.course, s.semester,
                   a.total_classes, a.attended_classes,
                   (a.attended_classes * 100.0 / a.total_classes) as percentage
            FROM student s
            JOIN attendance_student a ON s.roll_no = a.roll_no
            WHERE s.status = 'Active' AND a.total_classes > 0
        """, conn)

        # Categorize
        def categorize(pct):
            if pct >= 90: return "🟢 Excellent"
            elif pct >= 75: return "🔵 Good"
            elif pct >= 60: return "🟠 Satisfactory"
            else: return "🔴 Poor"

        attendance_df['category'] = attendance_df['percentage'].apply(categorize)

        st.dataframe(attendance_df, use_container_width=True)

        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Excellent (≥90%)", len(attendance_df[attendance_df['category'] == '🟢 Excellent']))
        with col2:
            st.metric("Good (75-89%)", len(attendance_df[attendance_df['category'] == '🔵 Good']))
        with col3:
            st.metric("Satisfactory (60-74%)", len(attendance_df[attendance_df['category'] == '🟠 Satisfactory']))
        with col4:
            st.metric("Poor (<60%)", len(attendance_df[attendance_df['category'] == '🔴 Poor']))

    # Fee Defaulter Prediction
    elif "Fee" in analysis_type:
        st.subheader("💰 Fee Defaulter Prediction")

        fees_df = pd.read_sql("""
            SELECT s.roll_no, s.name, s.phone, s.email,
                   f.semester, f.total_fee, f.paid_fee,
                   (f.total_fee - f.paid_fee) as pending,
                   f.due_date,
                   julianday(f.due_date) - julianday('now') as days_until_due
            FROM student s
            JOIN fee f ON s.roll_no = f.roll_no
            WHERE s.status = 'Active'
        """, conn)

        # Calculate risk
        def fee_risk(row):
            pending = row['pending']
            total = row['total_fee']
            days = row['days_until_due']
            paid_pct = (row['paid_fee'] / total * 100) if total > 0 else 0

            if days < 0:
                return "🔴 Overdue", "Critical"
            elif days <= 7 and paid_pct < 50:
                return "🟠 High Risk", "High"
            elif paid_pct < 30:
                return "🟡 Medium Risk", "Medium"
            else:
                return "🟢 Low Risk", "Low"

        fees_df[['risk_level', 'priority']] = fees_df.apply(fee_risk, axis=1, result_type='expand')

        st.dataframe(fees_df[fees_df['pending'] > 0], use_container_width=True)

        # Summary
        total_pending = fees_df['pending'].sum()
        st.metric("💰 Total Pending Amount", f"₹{total_pending:,}")

    # Grade Prediction
    elif "Grade" in analysis_type:
        st.subheader("📈 Grade Prediction")
        st.info("Predicts final grades based on internal marks")

        marks_df = pd.read_sql("""
            SELECT s.roll_no, s.name, m.subject_code, m.semester,
                   m.internal_marks, m.external_marks,
                   (m.internal_marks + m.external_marks) as current_total
            FROM student s
            JOIN marks m ON s.roll_no = m.roll_no
            WHERE s.status = 'Active'
        """, conn)

        # Predict based on internal marks
        marks_df['predicted_external'] = (marks_df['internal_marks'] / 30 * 70).round(2)
        marks_df['predicted_total'] = marks_df['internal_marks'] + marks_df['predicted_external']
        marks_df['predicted_grade'] = marks_df['predicted_total'].apply(
            lambda x: 'A' if x >= 85 else 'B' if x >= 70 else 'C' if x >= 55 else 'D' if x >= 40 else 'F'
        )

        st.dataframe(marks_df, use_container_width=True)

    conn.close()

def show_reports():
    """Reports & Export Module - PDF and Excel exports"""
    st.title("📄 Reports & Export")

    conn = sqlite3.connect('ums_database.db')

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Student Reports", "👨‍🏫 Teacher Reports", "📈 Analytics Reports", "📥 Bulk Export"])

    with tab1:
        st.subheader("Student Reports")

        report_type = st.selectbox("Select Report Type", [
            "All Students List",
            "Students by Course",
            "Students by Semester",
            "Student Performance Report",
            "Low Attendance Students"
        ])

        if report_type == "All Students List":
            df = pd.read_sql("SELECT * FROM student WHERE status='Active' ORDER BY roll_no", conn)
            st.dataframe(df, use_container_width=True)

            # Excel Export
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Students')
                workbook = writer.book
                worksheet = writer.sheets['Students']
                header_format = workbook.add_format({'bold': True, 'bg_color': '#4472C4', 'font_color': 'white'})
                for col_num, value in enumerate(df.columns.values):
                    worksheet.write(0, col_num, value, header_format)

            st.download_button(
                label="📥 Download as Excel",
                data=buffer.getvalue(),
                file_name=f"all_students_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.ms-excel"
            )

        elif report_type == "Students by Course":
            course = st.selectbox("Select Course", ["BCA", "MCA", "B.Tech", "M.Tech"])
            df = pd.read_sql(f"SELECT * FROM student WHERE course='{course}' AND status='Active' ORDER BY semester, roll_no", conn)
            st.dataframe(df, use_container_width=True)

            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name=course)

            st.download_button(
                label=f"📥 Download {course} Students",
                data=buffer.getvalue(),
                file_name=f"{course}_students_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.ms-excel"
            )

        elif report_type == "Low Attendance Students":
            threshold = st.slider("Attendance Threshold (%)", 0, 100, 75)
            df = pd.read_sql(f"""
                SELECT s.roll_no, s.name, s.course, s.semester,
                       a.attended_classes, a.total_classes,
                       ROUND((a.attended_classes * 100.0 / a.total_classes), 2) as percentage
                FROM student s
                JOIN attendance_student a ON s.roll_no = a.roll_no
                WHERE (a.attended_classes * 100.0 / a.total_classes) < {threshold}
                ORDER BY percentage
            """, conn)

            st.warning(f"⚠️ Found {len(df)} students with attendance below {threshold}%")
            st.dataframe(df, use_container_width=True)

            if not df.empty:
                buffer = BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='Low Attendance')

                st.download_button(
                    label="📥 Download Low Attendance Report",
                    data=buffer.getvalue(),
                    file_name=f"low_attendance_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.ms-excel"
                )

    with tab2:
        st.subheader("Teacher Reports")

        df = pd.read_sql("SELECT emp_id, name, department, designation, qualification, phone, email FROM teacher WHERE status='Active' ORDER BY department", conn)
        st.dataframe(df, use_container_width=True)

        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Teachers')
            workbook = writer.book
            worksheet = writer.sheets['Teachers']
            header_format = workbook.add_format({'bold': True, 'bg_color': '#28a745', 'font_color': 'white'})
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)

        st.download_button(
            label="📥 Download Teachers List",
            data=buffer.getvalue(),
            file_name=f"teachers_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.ms-excel"
        )

    with tab3:
        st.subheader("Analytics Reports")

        # Comprehensive Analytics
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**📊 Student Statistics**")
            stats_df = pd.read_sql("""
                SELECT
                    course,
                    COUNT(*) as total_students,
                    SUM(CASE WHEN gender='Male' THEN 1 ELSE 0 END) as male,
                    SUM(CASE WHEN gender='Female' THEN 1 ELSE 0 END) as female
                FROM student WHERE status='Active'
                GROUP BY course
            """, conn)
            st.dataframe(stats_df, use_container_width=True)

        with col2:
            st.markdown("**💰 Fee Collection Summary**")
            fee_summary = pd.read_sql("""
                SELECT
                    semester,
                    COUNT(*) as total_records,
                    SUM(total_fee) as total_fee,
                    SUM(paid_fee) as paid_fee,
                    SUM(total_fee - paid_fee) as pending
                FROM fee
                GROUP BY semester
                ORDER BY semester
            """, conn)
            st.dataframe(fee_summary, use_container_width=True)

        # Combined Export
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            stats_df.to_excel(writer, index=False, sheet_name='Student Stats')
            fee_summary.to_excel(writer, index=False, sheet_name='Fee Summary')

        st.download_button(
            label="📥 Download Complete Analytics",
            data=buffer.getvalue(),
            file_name=f"analytics_report_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.ms-excel"
        )

    with tab4:
        st.subheader("Bulk Data Export")
        st.info("💡 Export all data from all tables in one Excel file")

        if st.button("📥 Generate Complete Export", use_container_width=True):
            with st.spinner("Generating comprehensive export..."):
                buffer = BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    # Export all tables
                    pd.read_sql("SELECT * FROM student", conn).to_excel(writer, index=False, sheet_name='Students')
                    pd.read_sql("SELECT * FROM teacher", conn).to_excel(writer, index=False, sheet_name='Teachers')
                    pd.read_sql("SELECT * FROM marks", conn).to_excel(writer, index=False, sheet_name='Marks')
                    pd.read_sql("SELECT * FROM fee", conn).to_excel(writer, index=False, sheet_name='Fees')
                    pd.read_sql("SELECT * FROM attendance_student", conn).to_excel(writer, index=False, sheet_name='Attendance')

                st.success("✅ Export generated successfully!")
                st.download_button(
                    label="📥 Download Complete Database Export",
                    data=buffer.getvalue(),
                    file_name=f"complete_ums_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    mime="application/vnd.ms-excel",
                    use_container_width=True
                )

    conn.close()

def show_backup_restore():
    """Backup & Restore Module"""
    st.title("💾 Backup & Restore")

    tab1, tab2 = st.tabs(["💾 Create Backup", "📥 Restore Backup"])

    with tab1:
        st.subheader("Create Database Backup")
        st.info("💡 Create a backup copy of your entire database for safety")

        backup_name = st.text_input("Backup Name (optional)", placeholder="e.g., before_semester_end")

        if st.button("💾 Create Backup Now", type="primary", use_container_width=True):
            try:
                # Create backups directory if it doesn't exist
                os.makedirs("backups", exist_ok=True)

                # Generate backup filename
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                if backup_name:
                    backup_file = f"backups/ums_backup_{backup_name}_{timestamp}.db"
                else:
                    backup_file = f"backups/ums_backup_{timestamp}.db"

                # Copy database file
                shutil.copy2('ums_database.db', backup_file)

                # Get file size
                file_size = os.path.getsize(backup_file) / 1024  # KB

                st.success(f"✅ **Backup Created Successfully!**")
                st.info(f"📁 **File:** `{backup_file}`\n\n💾 **Size:** {file_size:.2f} KB")

                # Download button
                with open(backup_file, 'rb') as f:
                    st.download_button(
                        label="📥 Download Backup File",
                        data=f.read(),
                        file_name=os.path.basename(backup_file),
                        mime="application/octet-stream",
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"❌ **Backup Failed:** {str(e)}")

        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

        # List existing backups
        st.subheader("📋 Existing Backups")
        if os.path.exists("backups"):
            backup_files = [f for f in os.listdir("backups") if f.endswith('.db')]
            if backup_files:
                backup_data = []
                for file in sorted(backup_files, reverse=True):
                    file_path = os.path.join("backups", file)
                    size_kb = os.path.getsize(file_path) / 1024
                    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    backup_data.append({
                        'File Name': file,
                        'Size (KB)': f"{size_kb:.2f}",
                        'Created': modified_time.strftime('%Y-%m-%d %H:%M:%S')
                    })

                st.dataframe(pd.DataFrame(backup_data), use_container_width=True, hide_index=True)
            else:
                st.info("No backups found. Create your first backup above!")
        else:
            st.info("No backups directory found. Create your first backup to get started!")

    with tab2:
        st.subheader("Restore from Backup")
        st.warning("⚠️ **Warning:** Restoring will replace your current database!")

        if os.path.exists("backups"):
            backup_files = [f for f in os.listdir("backups") if f.endswith('.db')]
            if backup_files:
                selected_backup = st.selectbox("Select Backup to Restore", sorted(backup_files, reverse=True))

                st.info(f"📁 Selected: `{selected_backup}`")

                # Confirmation
                confirm = st.checkbox("⚠️ I understand this will replace the current database")

                if confirm:
                    if st.button("🔄 Restore Database", type="primary", use_container_width=True):
                        try:
                            backup_path = os.path.join("backups", selected_backup)

                            # Create a backup of current database before restoring
                            emergency_backup = f"backups/emergency_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
                            shutil.copy2('ums_database.db', emergency_backup)

                            # Restore the selected backup
                            shutil.copy2(backup_path, 'ums_database.db')

                            st.success("✅ **Database Restored Successfully!**")
                            st.info(f"💡 **Tip:** Your previous database was backed up to `{emergency_backup}` for safety")
                            st.warning("⚠️ **Please refresh the page** to see the restored data")
                        except Exception as e:
                            st.error(f"❌ **Restore Failed:** {str(e)}")
            else:
                st.info("No backups available to restore")
        else:
            st.info("No backups directory found")

# Run the app
if __name__ == "__main__":
    main()
