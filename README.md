# Student Management System

A web-based **Student Management System** developed using **Python (Flask)** and **MongoDB**.
This application allows teachers and students to manage academic information such as attendance, marks, and student records through a simple web interface.

## Features

* Teacher login authentication
* Student login authentication
* Teacher dashboard
* Student dashboard
* Add and remove student records
* Record student attendance
* Undo attendance records
* Enter student marks
* View student marks
* View student attendance
* Manage student relationships

## Technologies Used

* Python
* Flask
* MongoDB
* HTML
* CSS

## Project Structure

```
Student_Management_System
│
├── app.py
├── README.md
├── requirements.txt
│
├── database
│   └── db.py
│
├── services
│   ├── attendance_service.py
│   ├── marks_service.py
│   ├── relationship_service.py
│   └── student_service.py
│
├── static
│   ├── images
│   └── style.css
│
└── templates
    ├── index.html
    ├── student_login.html
    ├── teacher_login.html
    ├── student_dashboard.html
    ├── teacher_dashboard.html
    ├── add_student.html
    ├── remove_student.html
    ├── mark_attendance.html
    ├── undo_attendance.html
    ├── view_attendance.html
    ├── enter_marks.html
    ├── view_marks.html
    ├── student_relationship.html
    ├── add_friend.html
    └── view_students.html
```

## Installation

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/Student_Management_System.git
```

### 2. Navigate to the project folder

```
cd Student_Management_System
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a file named `.env` in the project root directory.

Example:

```
MONGO_URI=mongodb://localhost:27017/
DB_NAME=student_db
```

### 5. Run the application

```
python app.py
```

### 6. Open the application in your browser

```
http://127.0.0.1:5000
```

## Default Login Credentials

To access the teacher dashboard, a default teacher account is available.

Teacher Login

Username: admin
Password: admin123

You can use these credentials to log in as a teacher and manage students, attendance, and marks.

Students can log in using their registered student credentials stored in the database.

## Database Setup

This project uses **MongoDB** as the database.
Before running the project, configure the MongoDB connection in the `.env` file.

Collections used in the project:

* students
* marks
* attendance
* relationships

Collections will be created automatically when data is inserted.

## Future Improvements

* Implement **teacher registration / sign-up system**
* Improve authentication and security
* Enhance user interface design

## Screenshots

### Login Page

![Login Page](screenshots/login_page.png)

### Teacher Login

![Teacher Login](screenshots/teacher_login.png)

### Student Login

![Student Login](screenshots/student_login.png)

### Teacher Dashboard

![Teacher Dashboard](screenshots/teacher_dashboard.png)

### Student Dashboard

![Student Dashboard](screenshots/student_dashboard.png)
