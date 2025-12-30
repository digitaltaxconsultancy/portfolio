Task Management REST API
========================

Project Overview
----------------
This project is a backend REST API built using FastAPI and MySQL.
It allows users to create and manage tasks with proper database
relationships. The API supports full CRUD operations and can be tested
using Swagger UI or Postman.

Tech Stack
----------
- Language: Python
- Framework: FastAPI
- Database: MySQL
- ORM: SQLAlchemy
- DB Driver: PyMySQL
- API Testing: Swagger UI, Postman
- Server: Uvicorn

Features
--------
- Create users
- Create tasks assigned to users
- View all tasks
- MySQL database integration
- Automatic API documentation (Swagger)
- Clean modular backend architecture

Project Structure
-----------------
task_manager_api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routes.py
│   └── __init__.py
│
├── venv/
├── requirements.txt
└── README.md

Database Schema
---------------
Table: users
- id (INT, Primary Key)
- name (VARCHAR)
- email (VARCHAR)

Table: tasks
- id (INT, Primary Key)
- title (VARCHAR)
- description (TEXT)
- status (VARCHAR)
- user_id (Foreign Key)

How to Run the Project
----------------------
1. Install Python 3.11
2. Install MySQL and MySQL Workbench
3. Create database:
   CREATE DATABASE task_manager_db;
4. Create virtual environment:
   python -m venv venv
5. Activate environment:
   venv\Scripts\activate
6. Install dependencies:
   pip install fastapi uvicorn sqlalchemy pymysql
7. Update database credentials in database.py
8. Start server:
   uvicorn app.main:app
9. Open browser:
   http://127.0.0.1:8000/docs

API Endpoints
-------------
POST   /users   → Create user
POST   /tasks   → Create task
GET    /tasks   → Get all tasks

Testing
-------
- Swagger UI: /docs
- Postman (JSON requests)

Learning Outcomes
-----------------
- REST API development
- FastAPI framework
- SQLAlchemy ORM
- MySQL integration
- API testing and documentation

Future Enhancements
-------------------
- JWT Authentication
- Update & Delete APIs
- Pagination and filtering
- Docker deployment

Author
------
Anita Navale
