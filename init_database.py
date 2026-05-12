"""
Database Initialization Script
Creates the UMS database with sample data including admin and student users
"""

import sqlite3
import hashlib

def init_database():
    """Initialize the database with tables and sample data"""
    conn = sqlite3.connect('ums_database.db')
    cursor = conn.cursor()
    
    print("🔧 Initializing University Management System Database...")
    
    # Create login table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    
    # Insert default users
    # Admin user
    admin_password = hashlib.sha256('admin123'.encode()).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO login VALUES (?, ?, ?, ?)",
                   ('admin', admin_password, 'Administrator', 'admin'))
    
    # Sample student user (username = roll number)
    student_password = hashlib.sha256('student123'.encode()).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO login VALUES (?, ?, ?, ?)",
                   ('2301001', student_password, 'Rahul Kumar', 'student'))
    
    # Sample teacher user
    teacher_password = hashlib.sha256('teacher123'.encode()).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO login VALUES (?, ?, ?, ?)",
                   ('teacher1', teacher_password, 'Prof. Sharma', 'teacher'))
    
    print("✅ Login table created with default users:")
    print("   - admin / admin123 (Admin)")
    print("   - 2301001 / student123 (Student)")
    print("   - teacher1 / teacher123 (Teacher)")
    
    # Create student table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll_no TEXT PRIMARY KEY,
            name TEXT,
            father_name TEXT,
            dob TEXT,
            address TEXT,
            phone TEXT,
            email TEXT,
            aadhar TEXT UNIQUE,
            course TEXT,
            branch TEXT,
            semester INTEGER,
            year INTEGER,
            gender TEXT,
            category TEXT,
            status TEXT
        )
    """)
    
    # Insert sample student
    cursor.execute("""
        INSERT OR REPLACE INTO student VALUES 
        ('2301001', 'Rahul Kumar', 'Suresh Kumar', '2005-03-15', 
         'Delhi', '9876543210', 'rahul@email.com', '123456789012',
         'BCA', 'Computer Science', 3, 2023, 'Male', 'General', 'Active')
    """)
    
    print("✅ Student table created with sample data")
    
    # Create teacher table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher (
            emp_id TEXT PRIMARY KEY,
            name TEXT,
            phone TEXT,
            email TEXT,
            qualification TEXT,
            department TEXT,
            designation TEXT,
            gender TEXT,
            status TEXT
        )
    """)
    
    print("✅ Teacher table created")
    
    # Create marks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            subject_code TEXT,
            semester INTEGER,
            internal_marks INTEGER,
            external_marks INTEGER,
            UNIQUE(roll_no, subject_code, semester)
        )
    """)
    
    # Insert sample marks for student 2301001
    cursor.execute("INSERT OR REPLACE INTO marks (roll_no, subject_code, semester, internal_marks, external_marks) VALUES (?, ?, ?, ?, ?)",
                   ('2301001', 'BCA101', 3, 25, 65))
    cursor.execute("INSERT OR REPLACE INTO marks (roll_no, subject_code, semester, internal_marks, external_marks) VALUES (?, ?, ?, ?, ?)",
                   ('2301001', 'BCA102', 3, 28, 68))
    
    print("✅ Marks table created with sample data")
    
    # Create fee table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            semester INTEGER,
            total_fee INTEGER,
            paid_fee INTEGER,
            due_date TEXT,
            UNIQUE(roll_no, semester)
        )
    """)
    
    # Insert sample fee for student 2301001
    cursor.execute("INSERT OR REPLACE INTO fee (roll_no, semester, total_fee, paid_fee, due_date) VALUES (?, ?, ?, ?, ?)",
                   ('2301001', 3, 50000, 30000, '2025-02-28'))
    
    print("✅ Fee table created with sample data")
    
    # Create attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance_student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            semester INTEGER,
            total_classes INTEGER,
            attended_classes INTEGER,
            UNIQUE(roll_no, semester)
        )
    """)
    
    # Insert sample attendance for student 2301001
    cursor.execute("INSERT OR REPLACE INTO attendance_student (roll_no, semester, total_classes, attended_classes) VALUES (?, ?, ?, ?)",
                   ('2301001', 3, 100, 85))
    
    print("✅ Attendance table created with sample data")
    
    conn.commit()
    conn.close()
    
    print("\n🎉 Database initialization complete!")
    print("\n📋 Login Credentials:")
    print("=" * 50)
    print("ADMIN:")
    print("  Username: admin")
    print("  Password: admin123")
    print("\nSTUDENT:")
    print("  Username: 2301001")
    print("  Password: student123")
    print("\nTEACHER:")
    print("  Username: teacher1")
    print("  Password: teacher123")
    print("=" * 50)
    print("\n✅ Ready to run: streamlit run streamlit_app.py")

if __name__ == "__main__":
    init_database()
