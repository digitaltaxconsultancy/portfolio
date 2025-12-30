USE sql_data_cleaning;

-- ===============================
-- CUSTOMERS DATA CLEANING
-- ===============================

-- Add temporary unique column
ALTER TABLE customers
ADD COLUMN temp_id INT AUTO_INCREMENT PRIMARY KEY;

-- Remove duplicate customers
DELETE c1
FROM customers c1
JOIN customers c2
ON c1.customer_id = c2.customer_id
AND c1.temp_id > c2.temp_id;

-- Handle NULL values
UPDATE customers
SET email = 'not_available'
WHERE email IS NULL;

UPDATE customers
SET city = 'Unknown'
WHERE city IS NULL;

-- Remove temp primary key
ALTER TABLE customers DROP PRIMARY KEY;
ALTER TABLE customers DROP COLUMN temp_id;

-- Add final primary key
ALTER TABLE customers
ADD PRIMARY KEY (customer_id);

-- ===============================
-- PRODUCTS DATA CLEANING
-- ===============================

ALTER TABLE products
ADD COLUMN temp_id INT AUTO_INCREMENT PRIMARY KEY;

-- Remove duplicate products
DELETE p1
FROM products p1
JOIN products p2
ON p1.product_id = p2.product_id
AND p1.temp_id > p2.temp_id;

-- Fix NULL prices
UPDATE products
SET price = 500
WHERE price IS NULL;

ALTER TABLE products DROP PRIMARY KEY;
ALTER TABLE products DROP COLUMN temp_id;

ALTER TABLE products
ADD PRIMARY KEY (product_id);

-- ===============================
-- ORDERS DATA CLEANING
-- ===============================

ALTER TABLE orders
ADD COLUMN temp_id INT AUTO_INCREMENT PRIMARY KEY;

-- Remove duplicate orders
DELETE o1
FROM orders o1
JOIN orders o2
ON o1.order_id = o2.order_id
AND o1.temp_id > o2.temp_id;

-- Fix NULL total_amount
UPDATE orders o
JOIN products p ON o.product_id = p.product_id
SET o.total_amount = o.quantity * p.price
WHERE o.total_amount IS NULL;

ALTER TABLE orders DROP PRIMARY KEY;
ALTER TABLE orders DROP COLUMN temp_id;

ALTER TABLE orders
ADD PRIMARY KEY (order_id);
