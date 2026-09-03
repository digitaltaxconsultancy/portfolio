# SQL Data Cleaning & Reporting Project

## Project Overview
This project demonstrates how to clean raw SQL data and generate business reports using MySQL.
The dataset intentionally contains duplicates, NULL values, and missing constraints to simulate real-world data issues.

The project focuses on:
- Data cleaning using SQL
- Removing duplicate records
- Handling NULL values
- Adding primary keys after cleaning
- Generating analytical reports

---

## Tools & Technologies Used
- MySQL
- phpMyAdmin (XAMPP)
- SQL
- GitHub

---

## Project Structure
sql-data-cleaning-reporting
├── schema.sql
├── insert_data.sql
├── cleaning_queries.sql
├── reporting_queries.sql
├── screenshots/
└── README.md

---

## Dataset Description

### customers table
Columns:
- customer_id
- customer_name
- email
- city
- created_date

Data issues:
- Duplicate customer_id values
- NULL email values
- NULL city values
- No primary key

---

### products table
Columns:
- product_id
- product_name
- category
- price

Data issues:
- Duplicate product_id values
- NULL price values
- No primary key

---

### orders table
Columns:
- order_id
- customer_id
- product_id
- order_date
- quantity
- total_amount

Data issues:
- Duplicate order records
- NULL total_amount values
- No primary key

---

## Data Cleaning Process

### Step 1: Identify Data Issues
- Checked for duplicate records using GROUP BY and COUNT
- Identified NULL values in important columns
- Verified missing primary key constraints

---

### Step 2: Add Temporary Identifier
- Added a temporary AUTO_INCREMENT column (temp_id) to uniquely identify rows
- This allowed safe deletion of duplicate records

---

### Step 3: Remove Duplicates
- Used self-join technique with temp_id
- Kept one valid record and removed extra duplicate rows

---

### Step 4: Handle NULL Values
- Replaced NULL emails with 'not_available'
- Replaced NULL cities with 'Unknown'
- Updated missing product prices with a default value
- Calculated missing order total_amount values using quantity and product price

---

### Step 5: Enforce Data Integrity
- Removed temporary temp_id column
- Added PRIMARY KEY constraints after cleaning
- Ensured clean and consistent data

---

## Reporting & Analysis

The following business reports were generated:

- Total sales revenue
- Sales by product
- Top customers by spending
- Monthly sales trend

These queries help understand overall business performance and customer behavior.

---

## Key Learnings
- Real-world data often comes without primary keys
- Temporary identifiers are useful for cleaning duplicate records
- Data should be cleaned before applying constraints
- SQL is powerful for both data cleaning and reporting

---

## How to Run the Project

1. Run schema.sql to create database and tables
2. Run insert_data.sql to insert raw (dirty) data
3. Run cleaning_queries.sql to clean and standardize data
4. Run reporting_queries.sql to generate reports
5. Capture screenshots for documentation

---

## Conclusion
This project showcases practical SQL skills used by data analysts to clean messy data and generate meaningful insights.
It reflects real-world data cleaning challenges and professional SQL practices.

Author: Anita Navale
Role: Data Analyst | AI-ML Enthusiast | Ex-PHP Developer
