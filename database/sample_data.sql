-- ===================================================
-- SAMPLE DATA FOR TESTING
-- ===================================================

USE ums_db;

-- ===================================================
-- SAMPLE STUDENTS
-- ===================================================
INSERT INTO student (roll_no, name, father_name, dob, address, phone, email, aadhar, course, branch, semester, year, gender, category) VALUES
('2301001', 'Shabbir Ansari', 'Mohammed Ansari', '2003-05-15', 'Meerut, UP', '9876543210', 'shabbir@example.com', '123456789012', 'BCA', 'Computer Science', 5, 2024, 'Male', 'General'),
('2301002', 'Priya Sharma', 'Rajesh Sharma', '2003-08-20', 'Delhi', '9876543211', 'priya@example.com', '123456789013', 'BCA', 'Computer Science', 5, 2024, 'Female', 'General'),
('2301003', 'Rahul Kumar', 'Suresh Kumar', '2003-03-10', 'Noida, UP', '9876543212', 'rahul@example.com', '123456789014', 'BCA', 'Computer Science', 5, 2024, 'Male', 'OBC'),
('2301004', 'Anjali Singh', 'Vikram Singh', '2003-11-25', 'Ghaziabad, UP', '9876543213', 'anjali@example.com', '123456789015', 'BCA', 'Computer Science', 3, 2024, 'Female', 'General'),
('2301005', 'Amit Verma', 'Ramesh Verma', '2003-07-18', 'Lucknow, UP', '9876543214', 'amit@example.com', '123456789016', 'BCA', 'Computer Science', 3, 2024, 'Male', 'SC');

-- ===================================================
-- SAMPLE TEACHERS
-- ===================================================
INSERT INTO teacher (emp_id, name, father_name, dob, address, phone, email, aadhar, qualification, designation, department, subject_specialization, joining_date, gender, salary) VALUES
('EMP001', 'Dr. Khusbu Pandey', 'R.K. Pandey', '1985-06-15', 'Meerut, UP', '9123456780', 'khusbu.pandey@hbs.edu', '234567890123', 'Ph.D. Computer Science', 'Assistant Professor', 'Computer Science', 'Database Management', '2018-07-01', 'Female', 55000),
('EMP002', 'Dr. Anand Kiran', 'S.N. Kiran', '1982-03-20', 'Delhi', '9123456781', 'anand.kiran@hbs.edu', '234567890124', 'Ph.D. Computer Science', 'Associate Dean', 'Computer Science', 'Data Structures', '2015-08-15', 'Male', 75000),
('EMP003', 'Mr. Chanchal Bhattacharya', 'B.K. Bhattacharya', '1990-11-10', 'Kolkata', '9123456782', 'chanchal@hbs.edu', '234567890125', 'M.Tech CS', 'Lecturer', 'Computer Science', 'Web Development', '2020-01-10', 'Male', 45000);

-- ===================================================
-- SAMPLE SUBJECTS
-- ===================================================
INSERT INTO subject (subject_code, subject_name, credits, semester, department, course) VALUES
('BCA501', 'Database Management Systems', 4, 5, 'Computer Science', 'BCA'),
('BCA502', 'Web Technologies', 4, 5, 'Computer Science', 'BCA'),
('BCA503', 'Software Engineering', 4, 5, 'Computer Science', 'BCA'),
('BCA504', 'Operating Systems', 4, 5, 'Computer Science', 'BCA'),
('BCA505', 'Computer Networks', 4, 5, 'Computer Science', 'BCA'),
('BCA301', 'Data Structures', 4, 3, 'Computer Science', 'BCA'),
('BCA302', 'Object Oriented Programming', 4, 3, 'Computer Science', 'BCA');

-- ===================================================
-- SAMPLE ATTENDANCE (Students)
-- ===================================================
INSERT INTO attendance_student (roll_no, semester, total_classes, attended_classes) VALUES
('2301001', 5, 100, 92),
('2301002', 5, 100, 88),
('2301003', 5, 100, 65),
('2301004', 3, 80, 78),
('2301005', 3, 80, 55);

-- ===================================================
-- SAMPLE ATTENDANCE (Teachers)
-- ===================================================
INSERT INTO attendance_teacher (emp_id, month, year, total_days, present_days) VALUES
('EMP001', 12, 2024, 26, 25),
('EMP002', 12, 2024, 26, 26),
('EMP003', 12, 2024, 26, 24);

-- ===================================================
-- SAMPLE MARKS
-- ===================================================
INSERT INTO marks (roll_no, subject_code, semester, exam_type, marks_obtained, total_marks, grade, exam_date) VALUES
-- Shabbir's Marks (Semester 5)
('2301001', 'BCA501', 5, 'Mid-Term', 42, 50, 'A', '2024-10-15'),
('2301001', 'BCA502', 5, 'Mid-Term', 45, 50, 'A+', '2024-10-16'),
('2301001', 'BCA503', 5, 'Mid-Term', 38, 50, 'B+', '2024-10-17'),

-- Priya's Marks (Semester 5)
('2301002', 'BCA501', 5, 'Mid-Term', 48, 50, 'A+', '2024-10-15'),
('2301002', 'BCA502', 5, 'Mid-Term', 46, 50, 'A+', '2024-10-16'),
('2301002', 'BCA503', 5, 'Mid-Term', 44, 50, 'A+', '2024-10-17'),

-- Rahul's Marks (Semester 5)
('2301003', 'BCA501', 5, 'Mid-Term', 28, 50, 'C', '2024-10-15'),
('2301003', 'BCA502', 5, 'Mid-Term', 25, 50, 'C', '2024-10-16'),
('2301003', 'BCA503', 5, 'Mid-Term', 22, 50, 'D', '2024-10-17');

-- ===================================================
-- SAMPLE FEE RECORDS
-- ===================================================
INSERT INTO fee (roll_no, semester, total_fee, paid_amount, payment_date, payment_mode, transaction_id, due_date) VALUES
('2301001', 5, 45000, 45000, '2024-07-15', 'Online', 'TXN001234567', '2024-07-31'),
('2301002', 5, 45000, 45000, '2024-07-20', 'Online', 'TXN001234568', '2024-07-31'),
('2301003', 5, 45000, 25000, '2024-07-25', 'Cash', NULL, '2024-07-31'),
('2301004', 3, 45000, 45000, '2024-07-10', 'Cheque', 'CHQ123456', '2024-07-31'),
('2301005', 3, 45000, 0, NULL, NULL, NULL, '2024-07-31');

-- ===================================================
-- VERIFY DATA
-- ===================================================
SELECT 'Students Inserted:' AS Info, COUNT(*) AS Count FROM student
UNION ALL
SELECT 'Teachers Inserted:', COUNT(*) FROM teacher
UNION ALL
SELECT 'Subjects Inserted:', COUNT(*) FROM subject
UNION ALL
SELECT 'Attendance Records:', COUNT(*) FROM attendance_student
UNION ALL
SELECT 'Marks Records:', COUNT(*) FROM marks
UNION ALL
SELECT 'Fee Records:', COUNT(*) FROM fee;

-- ===================================================
-- End of Sample Data
-- ===================================================
