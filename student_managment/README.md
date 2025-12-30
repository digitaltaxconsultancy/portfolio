Student Management System
=========================

Project Overview
----------------
This is a backend-based Student Management System developed using Python and MySQL.
The project allows managing student records including adding, viewing, updating,
and deleting student information. It demonstrates database connectivity, CRUD
operations, and structured backend logic.

Tech Stack
----------
- Language: Python
- Database: MySQL
- DB Tool: MySQL Workbench
- Connector: MySQLdb / PyMySQL
- Environment: Virtual Environment (venv)

Features
--------
- Add new student records
- View all students
- Update student details
- Delete student records
- MySQL database integration
- Error handling and validation

Database Schema
---------------
Table: students

Columns:
- id (INT, Primary Key, Auto Increment)
- name (VARCHAR)
- email (VARCHAR)
- course (VARCHAR)
- created_at (TIMESTAMP)

How to Run the Project
----------------------
1. Install Python (3.10+ recommended)
2. Install MySQL and MySQL Workbench
3. Create database:
   CREATE DATABASE student_db;
4. Create required tables in MySQL
5. Create virtual environment:
   python -m venv venv
6. Activate environment:
   venv\Scripts\activate
7. Install dependencies:
   pip install mysqlclient
8. Update database credentials in code
9. Run the Python file:
   python main.py

Learning Outcomes
-----------------
- Python-MySQL connectivity
- SQL CRUD operations
- Backend logic implementation
- Database design basics

Future Enhancements
-------------------
- REST API using FastAPI
- Web UI integration
- Authentication system
- Pagination and search

Author
------
Anita Navale
