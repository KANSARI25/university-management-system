<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    String username = (String) session.getAttribute("username");
    if (username == null) {
        response.sendRedirect("login.html");
        return;
    }
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI/ML Analytics - UMS</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; background: #f5f7fa; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;
                  padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .container { max-width: 1400px; margin: 20px auto; padding: 0 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                transition: transform 0.3s; cursor: pointer; }
        .card:hover { transform: translateY(-5px); box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
        .card h3 { color: #667eea; margin-bottom: 15px; }
        .card p { color: #666; line-height: 1.6; }
        .btn { padding: 10px 20px; background: #667eea; color: white; text-decoration: none;
               border-radius: 8px; display: inline-block; }
        .btn:hover { background: #764ba2; }
        .icon { font-size: 48px; margin-bottom: 15px; }
        #results { margin-top: 30px; }
        .result-card { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th { background: #667eea; color: white; padding: 10px; text-align: left; }
        td { padding: 10px; border-bottom: 1px solid #e0e0e0; }
        .loading { text-align: center; padding: 40px; color: #666; }
        .error { background: #ffe0e0; color: #c0392b; padding: 15px; border-radius: 8px; }
        .success { background: #d4edda; color: #155724; padding: 15px; border-radius: 8px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 AI/ML Analytics Dashboard</h1>
        <a href="dashboard.jsp" class="btn">← Back to Dashboard</a>
    </div>

    <div class="container">
        <div class="grid">
            <div class="card" onclick="loadPrediction('performance')">
                <div class="icon">🎯</div>
                <h3>Performance Prediction</h3>
                <p>Identify at-risk students based on attendance and marks using AI algorithms.</p>
            </div>

            <div class="card" onclick="loadPrediction('attendance')">
                <div class="icon">📊</div>
                <h3>Attendance Analysis</h3>
                <p>Analyze attendance patterns and trends across all students and courses.</p>
            </div>

            <div class="card" onclick="loadPrediction('fee')">
                <div class="icon">💰</div>
                <h3>Fee Defaulter Prediction</h3>
                <p>Predict potential fee defaulters and send automated reminders.</p>
            </div>

            <div class="card" onclick="loadPrediction('grades')">
                <div class="icon">📈</div>
                <h3>Grade Prediction</h3>
                <p>Predict final grades based on internal marks and performance trends.</p>
            </div>
        </div>

        <div id="results"></div>
    </div>

    <script>
        function loadPrediction(type) {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<div class="loading">🔄 Loading AI predictions...</div>';

            let endpoint = '';
            let title = '';

            switch(type) {
                case 'performance':
                    endpoint = 'http://localhost:5000/api/predict/performance';
                    title = '🎯 Student Performance Prediction';
                    break;
                case 'attendance':
                    endpoint = 'http://localhost:5000/api/analyze/attendance';
                    title = '📊 Attendance Pattern Analysis';
                    break;
                case 'fee':
                    endpoint = 'http://localhost:5000/api/predict/fee_defaulters';
                    title = '💰 Fee Defaulter Prediction';
                    break;
                case 'grades':
                    endpoint = 'http://localhost:5000/api/predict/grades';
                    title = '📈 Grade Prediction';
                    break;
            }

            fetch(endpoint)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        displayResults(data, title, type);
                    } else {
                        resultsDiv.innerHTML = '<div class="error">❌ Error: ' + (data.error || 'Unknown error') + '</div>';
                    }
                })
                .catch(error => {
                    resultsDiv.innerHTML = '<div class="error">❌ Error connecting to AI/ML backend. Make sure Flask server is running on port 5000.<br><br>' + 
                                          '<strong>Quick Fix:</strong> Run "ml_backend\\START_ML_BACKEND.bat"</div>';
                });
        }

        function displayResults(data, title, type) {
            const resultsDiv = document.getElementById('results');
            let html = '<div class="result-card"><h2>' + title + '</h2>';

            if (type === 'performance') {
                html += '<p><strong>Total Students Analyzed:</strong> ' + data.total_students + '</p>';
                html += '<table><thead><tr><th>Roll No</th><th>Name</th><th>Attendance %</th><th>Avg Marks</th><th>Risk Level</th><th>Risk Factors</th></tr></thead><tbody>';
                data.predictions.forEach(p => {
                    html += '<tr><td>' + p.roll_no + '</td><td>' + p.name + '</td><td>' + p.attendance + '%</td><td>' + p.avg_marks + '</td>';
                    html += '<td style="color:' + p.color + '; font-weight:bold;">' + p.risk_level + '</td>';
                    html += '<td>' + (p.risk_factors.length > 0 ? p.risk_factors.join(', ') : 'None') + '</td></tr>';
                });
                html += '</tbody></table>';

            } else if (type === 'attendance') {
                const analysis = data.analysis;
                html += '<p><strong>Total Records:</strong> ' + analysis.total_records + '</p>';
                html += '<p><strong>Excellent (≥90%):</strong> ' + analysis.excellent + ' | ';
                html += '<strong>Good (75-89%):</strong> ' + analysis.good + ' | ';
                html += '<strong>Satisfactory (60-74%):</strong> ' + analysis.satisfactory + ' | ';
                html += '<strong>Poor (<60%):</strong> ' + analysis.poor + '</p>';
                html += '<table><thead><tr><th>Roll No</th><th>Name</th><th>Course</th><th>Attended/Total</th><th>%</th><th>Category</th></tr></thead><tbody>';
                analysis.students.forEach(s => {
                    html += '<tr><td>' + s.roll_no + '</td><td>' + s.name + '</td><td>' + s.course + '</td>';
                    html += '<td>' + s.attended + '/' + s.total_classes + '</td><td>' + s.percentage + '%</td>';
                    html += '<td style="color:' + s.color + '; font-weight:bold;">' + s.category + '</td></tr>';
                });
                html += '</tbody></table>';

            } else if (type === 'fee') {
                html += '<p><strong>Total Defaulters:</strong> ' + data.total_defaulters + '</p>';
                html += '<table><thead><tr><th>Roll No</th><th>Name</th><th>Semester</th><th>Total Fee</th><th>Paid</th><th>Pending</th><th>Priority</th></tr></thead><tbody>';
                data.defaulters.forEach(d => {
                    html += '<tr><td>' + d.roll_no + '</td><td>' + d.name + '</td><td>' + d.semester + '</td>';
                    html += '<td>₹' + d.total_fee.toLocaleString() + '</td><td>₹' + d.paid_fee.toLocaleString() + '</td>';
                    html += '<td>₹' + d.pending_fee.toLocaleString() + '</td>';
                    html += '<td style="color:' + d.color + '; font-weight:bold;">' + d.priority + '</td></tr>';
                });
                html += '</tbody></table>';

            } else if (type === 'grades') {
                html += '<p><strong>Total Predictions:</strong> ' + data.total_predictions + '</p>';
                html += '<table><thead><tr><th>Roll No</th><th>Name</th><th>Subject</th><th>Internal</th><th>Current Total</th><th>Predicted Total</th><th>Predicted Grade</th></tr></thead><tbody>';
                data.predictions.forEach(p => {
                    html += '<tr><td>' + p.roll_no + '</td><td>' + p.name + '</td><td>' + p.subject + '</td>';
                    html += '<td>' + p.internal_marks + '</td><td>' + p.current_total + '</td>';
                    html += '<td>' + p.predicted_total + '</td>';
                    html += '<td style="font-weight:bold;">' + p.predicted_grade + '</td></tr>';
                });
                html += '</tbody></table>';
            }

            html += '</div>';
            resultsDiv.innerHTML = html;
        }
    </script>
</body>
</html>
