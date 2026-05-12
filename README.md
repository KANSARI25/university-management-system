# 🎓 University Management System (UMS)

**A Complete Web-Based University Management System with AI/ML Analytics**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📌 Project Overview

**Major Project (BCA606 - 2025-2026)**
A comprehensive, modern web-based University Management System built with **Streamlit** and **SQLite**, featuring a clean, professional UI design with advanced AI/ML analytics capabilities.

**Developer**: Shabbir Ansari
**Project Type**: BCA Major Project (2025-2026)
**Tech Stack**: Python, Streamlit, SQLite, Plotly, Pandas, XlsxWriter

---

## ✨ Implemented Features

### 🎯 **Core CRUD Modules** (100% Complete)

#### 1. **👨‍🎓 Student Management**
- ✅ Add new students with comprehensive validation
- ✅ Update student information with change tracking
- ✅ Delete students with confirmation popup
- ✅ Advanced search by name, course, semester, gender
- ✅ Filter and export student lists
- ✅ View all students in sortable table
- ✅ Validations: Phone (10 digits), Email, Aadhar (12 digits)

#### 2. **👨‍🏫 Teacher Management**
- ✅ Add teachers with department and designation
- ✅ Update teacher records with change tracking
- ✅ Delete teachers with confirmation
- ✅ View all active teachers
- ✅ Export teacher data to Excel/CSV
- ✅ Email and phone validation

#### 3. **📊 Marks Management**
- ✅ Add student marks (Internal + External)
- ✅ Automatic grade calculation (A/B/C/D/F)
- ✅ Update marks with change tracking
- ✅ Delete marks records
- ✅ Search by Roll Number and Subject
- ✅ View all marks with student names
- ✅ Grade distribution analysis

#### 4. **💰 Fee Management**
- ✅ Add fee records with due dates
- ✅ Track total fee, paid amount, pending amount
- ✅ Update fee payments with change tracking
- ✅ Delete fee records
- ✅ Auto-calculate payment status (Paid/Partial/Pending)
- ✅ Fee defaulter identification

#### 5. **✅ Attendance Management**
- ✅ Mark student attendance (New Records)
- ✅ Update attendance records
- ✅ Automatic percentage calculation
- ✅ Track total classes and attended classes
- ✅ View all attendance records
- ✅ Low attendance alerts (< 75%)

### 🚀 **Advanced Features** (100% Complete)

#### 6. **🤖 AI/ML Analytics Dashboard**
- ✅ **Student Performance Prediction** - Identify at-risk students
- ✅ **Attendance Pattern Analysis** - Track attendance trends
- ✅ **Fee Defaulter Prediction** - Risk assessment based on payment history
- ✅ **Grade Prediction** - Predict final grades from mid-term marks
- ✅ Interactive data visualizations with Plotly

#### 7. **📄 Reports & Export Module** (NEW!)
- ✅ **Student Reports**:
  - All students list with filters
  - Students by course
  - Students by semester
  - Low attendance students (customizable threshold)
- ✅ **Teacher Reports**: Complete teacher directory
- ✅ **Analytics Reports**: Student statistics, fee summary
- ✅ **Bulk Export**: Export all database tables in one Excel file
- ✅ **Excel Export** with formatted headers
- ✅ **CSV Export** for all data tables

#### 8. **👥 User Management Module** (NEW!)
- ✅ **Add Users**: Create new admin, teacher, or student accounts
- ✅ **View All Users**: List all users with roles
- ✅ **Manage Users**: Edit or delete existing users
- ✅ **Reset Password**: Admin can reset any user's password
- ✅ **Role-Based Access**: Different permissions for admin/teacher/student

#### 9. **👨‍🎓 Student Portal** (NEW!)
- ✅ **Student Dashboard**: Personalized dashboard for students
- ✅ **My Marks**: Students can view their marks and grades
- ✅ **My Fees**: View fee records and payment status
- ✅ **My Attendance**: Check attendance percentage
- ✅ **Separate Login**: Students login with their roll number

#### 10. **🔐 Change Password** (NEW!)
- ✅ **Self-Service**: All users can change their own password
- ✅ **Secure**: Requires current password verification
- ✅ **Validation**: Minimum 6 characters, confirmation required

#### 11. **📊 Enhanced Dashboard** (NEW!)
- ✅ **Interactive Charts**: Pie charts, bar charts using Plotly
- ✅ **Visual Analytics**: Students by course, semester distribution
- ✅ **Attendance Distribution**: Color-coded attendance ranges
- ✅ **Fee Status Visualization**: Paid/Partial/Pending breakdown
- ✅ **Real-time Statistics**: Live count of students, teachers, attendance

#### 12. **🔍 Advanced Search & Filters** (NEW!)
- ✅ Multi-field search across all modules
- ✅ Filter by course, semester, gender, status
- ✅ Search by name (partial matching)
- ✅ Dynamic result count display
- ✅ Export filtered results

### 🎨 **UI/UX Features**
- ✅ **Modern Design**: Clean, professional interface
- ✅ **Success Popups**: 5-second auto-close modals with change tracking
- ✅ **Change Tracking**: Shows "before → after" for all updates
- ✅ **Responsive Layout**: Works on desktop and mobile
- ✅ **Sidebar Navigation**: Always accessible menu
- ✅ **Professional Color Scheme**: Light gradients, clean cards

### ✅ **Smart Validations**
- ✅ Required field indicators (*)
- ✅ Phone number: Exactly 10 digits
- ✅ Email: Must contain @
- ✅ Aadhar: Exactly 12 digits
- ✅ Fees: Paid ≤ Total
- ✅ Attendance: Attended ≤ Total Classes
- ✅ Duplicate prevention

---

## 🛠️ Tech Stack

### **Full-Stack Architecture**

This is a **complete full-stack web application** with:

#### **Frontend (Presentation Layer)**
- **Streamlit** - Web UI framework (HTML/CSS/JS auto-generated)
- **Plotly** - Interactive charts and visualizations
- **Custom CSS** - Professional styling with high-contrast alerts

#### **Backend (Application Layer)**
- **Python 3.13** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning algorithms
- **Hashlib** - Password encryption (SHA-256)
- **XlsxWriter** - Excel report generation

#### **Database (Data Layer)**
- **SQLite** - Lightweight relational database
- **6 Tables** - login, student, teacher, marks, fee, attendance

### **Technology Details**

| Component | Technology | Version |
|-----------|------------|---------|
| **Language** | Python | 3.13 |
| **Framework** | Streamlit | Latest |
| **Database** | SQLite | 3.x |
| **Data Analysis** | Pandas | Latest |
| **Numerical Computing** | NumPy | Latest |
| **Visualization** | Plotly | Latest |
| **Excel Export** | XlsxWriter | Latest |
| **Excel Read** | Openpyxl | Latest |
| **PDF Generation** | ReportLab | 4.5.0 |

### **Architecture Type**
**3-Tier Full-Stack Application**
- **Tier 1**: Presentation (Streamlit UI)
- **Tier 2**: Business Logic (Python)
- **Tier 3**: Data Storage (SQLite)

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.13 or higher
- pip (Python package manager)

### Quick Start (5 Minutes)

1. **Clone the repository**
```bash
git clone https://github.com/KANSARI25/university-management-system.git
cd university-management-system
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Initialize the database**
```bash
python init_database.py
```

4. **Run the application**
```bash
streamlit run streamlit_app.py
```

5. **Access the application**
```
Your browser will automatically open:
http://localhost:8501
```

---

## 🔐 Default Login Credentials

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin123` | Administrator (Full Access) |
| `2301001` | `student123` | Student (View Own Data) |
| `teacher1` | `teacher123` | Teacher (Limited Access) |

⚠️ **Important**: Change passwords after first login for security

### Role-Based Access:
- **Admin**: Full access to all modules, can manage users
- **Student**: Can only view their own marks, fees, and attendance
- **Teacher**: Can view all data but limited edit access

---

## 📁 Project Structure

```
university-management-system/
├── streamlit_app.py          # Main application file
├── init_database.py          # Database initialization script
├── requirements.txt          # Python dependencies
├── ums_database.db          # SQLite database (auto-created)
├── backups/                 # Database backups folder
├── screenshots/             # Application screenshots
├── README.md               # This file
└── LICENSE                 # MIT License
```

---

## 🗄️ Database Schema

**6 Core Tables:**

1. **`login`** - User authentication
   - username, password (SHA-256 hashed), name, role

2. **`student`** - Student information
   - roll_no (PK), name, father_name, dob, address, phone, email, aadhar
   - course, branch, semester, year, gender, category, status

3. **`teacher`** - Teacher information
   - emp_id (PK), name, phone, email, qualification
   - department, designation, gender, status

4. **`marks`** - Student marks
   - roll_no, subject_code, semester, internal_marks, external_marks
   - Auto-calculated: total, grade

5. **`fee`** - Fee management
   - roll_no, semester, total_fee, paid_fee, due_date
   - Auto-calculated: pending_fee, status

6. **`attendance_student`** - Attendance tracking
   - roll_no, semester, total_classes, attended_classes
   - Auto-calculated: percentage

---

## 🎯 Usage Guide

### Adding a Student
1. Navigate to **👨‍🎓 Student Management**
2. Click **➕ Add Student** tab
3. Fill required fields (marked with *)
4. Click **Add Student**
5. ✅ Success popup appears for 5 seconds

### Generating Reports
1. Go to **📄 Reports & Export**
2. Select report type (Student/Teacher/Analytics)
3. Apply filters as needed
4. Click **Download Excel** or **Download CSV**

### Creating Database Backup
1. Navigate to **💾 Backup & Restore**
2. Enter optional backup name
3. Click **Create Backup Now**
4. Download or keep in backups folder

### Viewing Analytics
1. Go to **🤖 AI/ML Analytics**
2. Select analysis type:
   - Student Performance Prediction
   - Attendance Pattern Analysis
   - Fee Defaulter Prediction
   - Grade Prediction
3. View interactive visualizations and insights

---

## 📊 Dashboard Features

The enhanced dashboard provides:
- **Quick Stats**: Students, Teachers, Avg Attendance, Pending Fees
- **Students by Course**: Interactive pie chart
- **Semester Distribution**: Bar chart
- **Attendance Ranges**: Color-coded visualization
- **Fee Status**: Payment status breakdown
- **Recent Students**: Last 10 added students

---

## 🎓 Project Highlights

### What Makes This Project Special?

1. **✅ Complete CRUD Operations**: All 5 modules fully functional
2. **🎨 Professional UI**: Clean, modern design with intuitive navigation
3. **📊 Interactive Visualizations**: Plotly charts and graphs
4. **🤖 AI/ML Integration**: Performance prediction and analytics
5. **💾 Data Management**: Backup, restore, export capabilities
6. **🔍 Advanced Search**: Multi-field search and filtering
7. **✨ Smart Popups**: 5-second auto-close with change tracking
8. **📄 Report Generation**: Excel exports with formatting
9. **🔐 Secure**: Password hashing, session management
10. **📱 Responsive**: Works on all screen sizes

---

## 📸 Screenshots

### Login Page
*Clean and professional login interface*

### Dashboard
*Interactive charts showing real-time statistics*

### Student Management
*Complete CRUD with advanced search and filters*

### AI/ML Analytics
*Performance prediction and insights*

### Reports & Export
*Generate and download comprehensive reports*

### Backup & Restore
*One-click database backup and restore*

---

## 🚀 Future Enhancements

- 📧 Email notification system
- 📱 SMS integration for alerts
- 👤 Student/Teacher self-service portals
- 📄 PDF report generation
- 🔔 In-app notification system
- 📊 More advanced ML models
- 🌐 Multi-language support

---

## 🔒 Security Features

- ✅ SHA-256 password hashing
- ✅ Session management with Streamlit
- ✅ SQL injection prevention
- ✅ Input validation and sanitization
- ✅ Role-based access control (Admin/User)
- ✅ Secure database backups

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Shabbir Ansari**
- Project: BCA606 Major Project (2025-2026)
- GitHub: [@KANSARI25](https://github.com/KANSARI25)
- Repository: [University Management System](https://github.com/KANSARI25/university-management-system)

---

## 🙏 Acknowledgments

- **Streamlit** - For the amazing web framework
- **Plotly** - For interactive visualizations
- **Pandas** - For data manipulation
- **The Open Source Community** - For continuous support

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact via email
- Check documentation in `docs/` folder

---

## 🎯 Project Status

**Status**: ✅ **COMPLETE**
**Version**: 1.0.0
**Last Updated**: January 2025
**Production Ready**: Yes

---

**⭐ If you find this project helpful, please give it a star! ⭐**

**Made with ❤️ by Shabbir Ansari**
