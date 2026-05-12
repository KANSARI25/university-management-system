-- ===================================================
-- UNIVERSITY MANAGEMENT SYSTEM - DATABASE SCHEMA
-- Developer: Shabbir Ansari
-- Date: December 2024
-- ===================================================

-- Drop database if exists (for clean setup)
DROP DATABASE IF EXISTS ums_db;

-- Create database
CREATE DATABASE ums_db;
USE ums_db;

-- ===================================================
-- 1. ACCOUNT TABLE (User Authentication)
-- ===================================================
CREATE TABLE account (
    username VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    security_question VARCHAR(255),
    security_answer VARCHAR(255),
    role ENUM('admin', 'user') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default admin account
INSERT INTO account (username, name, password, role) 
VALUES ('admin', 'System Administrator', 'admin123', 'admin');

-- Insert sample user account
INSERT INTO account (username, name, password, role) 
VALUES ('user', 'Regular User', 'user123', 'user');

-- ===================================================
-- 2. STUDENT TABLE (Student Information)
-- ===================================================
CREATE TABLE student (
    roll_no VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    father_name VARCHAR(100),
    dob DATE,
    address VARCHAR(255),
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    aadhar VARCHAR(12) UNIQUE,
    course VARCHAR(50),
    branch VARCHAR(50),
    semester INT,
    year INT,
    gender ENUM('Male', 'Female', 'Other'),
    category ENUM('General', 'OBC', 'SC', 'ST'),
    admission_date DATE DEFAULT (CURRENT_DATE),
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ===================================================
-- 3. TEACHER TABLE (Teacher Information)
-- ===================================================
CREATE TABLE teacher (
    emp_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    father_name VARCHAR(100),
    dob DATE,
    address VARCHAR(255),
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    aadhar VARCHAR(12) UNIQUE,
    qualification VARCHAR(100),
    designation VARCHAR(50),
    department VARCHAR(50),
    subject_specialization VARCHAR(100),
    joining_date DATE,
    gender ENUM('Male', 'Female', 'Other'),
    salary DECIMAL(10, 2),
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ===================================================
-- 4. SUBJECT TABLE
-- ===================================================
CREATE TABLE subject (
    subject_code VARCHAR(20) PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    credits INT DEFAULT 4,
    semester INT,
    department VARCHAR(50),
    course VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ===================================================
-- 5. ATTENDANCE_STUDENT TABLE
-- ===================================================
CREATE TABLE attendance_student (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(20),
    semester INT,
    total_classes INT DEFAULT 0,
    attended_classes INT DEFAULT 0,
    percentage DECIMAL(5, 2) AS (
        CASE 
            WHEN total_classes > 0 THEN (attended_classes * 100.0 / total_classes)
            ELSE 0 
        END
    ) STORED,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (roll_no) REFERENCES student(roll_no) ON DELETE CASCADE,
    UNIQUE KEY unique_attendance (roll_no, semester)
);

-- ===================================================
-- 6. ATTENDANCE_TEACHER TABLE
-- ===================================================
CREATE TABLE attendance_teacher (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id VARCHAR(20),
    month INT,
    year INT,
    total_days INT DEFAULT 0,
    present_days INT DEFAULT 0,
    percentage DECIMAL(5, 2) AS (
        CASE 
            WHEN total_days > 0 THEN (present_days * 100.0 / total_days)
            ELSE 0 
        END
    ) STORED,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES teacher(emp_id) ON DELETE CASCADE,
    UNIQUE KEY unique_teacher_attendance (emp_id, month, year)
);

-- ===================================================
-- 7. MARKS TABLE (Examination Marks)
-- ===================================================
CREATE TABLE marks (
    marks_id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(20),
    subject_code VARCHAR(20),
    semester INT,
    exam_type ENUM('Mid-Term', 'End-Term', 'Internal') DEFAULT 'End-Term',
    marks_obtained DECIMAL(5, 2),
    total_marks DECIMAL(5, 2) DEFAULT 100,
    percentage DECIMAL(5, 2) AS (
        (marks_obtained * 100.0 / total_marks)
    ) STORED,
    grade VARCHAR(2),
    remarks VARCHAR(255),
    exam_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (roll_no) REFERENCES student(roll_no) ON DELETE CASCADE,
    FOREIGN KEY (subject_code) REFERENCES subject(subject_code) ON DELETE CASCADE
);

-- ===================================================
-- 8. FEE TABLE (Fee Management)
-- ===================================================
CREATE TABLE fee (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(20),
    semester INT,
    total_fee DECIMAL(10, 2) DEFAULT 0,
    paid_amount DECIMAL(10, 2) DEFAULT 0,
    balance DECIMAL(10, 2) AS (total_fee - paid_amount) STORED,
    payment_date DATE,
    payment_mode ENUM('Cash', 'Online', 'Cheque', 'DD') DEFAULT 'Cash',
    transaction_id VARCHAR(50),
    status ENUM('Paid', 'Pending', 'Partial') AS (
        CASE 
            WHEN paid_amount >= total_fee THEN 'Paid'
            WHEN paid_amount > 0 THEN 'Partial'
            ELSE 'Pending'
        END
    ) STORED,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (roll_no) REFERENCES student(roll_no) ON DELETE CASCADE,
    UNIQUE KEY unique_fee (roll_no, semester)
);

-- ===================================================
-- INDEXES for Better Performance
-- ===================================================
CREATE INDEX idx_student_name ON student(name);
CREATE INDEX idx_student_course ON student(course, semester);
CREATE INDEX idx_teacher_name ON teacher(name);
CREATE INDEX idx_marks_roll ON marks(roll_no);
CREATE INDEX idx_fee_status ON fee(status);

-- ===================================================
-- End of Schema
-- ===================================================
