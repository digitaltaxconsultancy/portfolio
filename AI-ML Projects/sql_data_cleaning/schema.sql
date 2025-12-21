-- Create Database
CREATE DATABASE IF NOT EXISTS sql_data_cleaning;
USE sql_data_cleaning;

-- Customers table (raw data)
CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    created_date DATE
);

-- Products table (raw data)
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Orders table (raw data)
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    total_amount DECIMAL(10,2)
);
