USE sql_data_cleaning;

-- Total Sales
SELECT SUM(total_amount) AS total_sales
FROM orders;

-- Sales by Product
SELECT p.product_name,
       SUM(o.total_amount) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

-- Top Customers by Spending
SELECT c.customer_name,
       SUM(o.total_amount) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;

-- Monthly Sales Report
SELECT MONTH(order_date) AS month,
       SUM(total_amount) AS monthly_sales
FROM orders
GROUP BY month
ORDER BY month;
