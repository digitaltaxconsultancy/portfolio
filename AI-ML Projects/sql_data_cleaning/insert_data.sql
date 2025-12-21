-- Customers (duplicates & NULLs)
INSERT INTO customers VALUES
(1,'Ravi','ravi@gmail.com','Mumbai','2024-01-10'),
(2,'Sita','sita@gmail.com','Pune','2024-01-15'),
(2,'Sita','sita@gmail.com','Pune','2024-01-15'),
(3,'Amit',NULL,'Delhi','2024-02-01'),
(4,'Neha','neha@gmail.com',NULL,'2024-02-05');

-- Products (duplicate & NULL price)
INSERT INTO products VALUES
(101,'Laptop','Electronics',55000),
(102,'Mouse','Electronics',NULL),
(103,'Chair','Furniture',3000),
(103,'Chair','Furniture',3000);

-- Orders (NULL total & duplicate)
INSERT INTO orders VALUES
(1001,1,101,'2024-02-10',1,55000),
(1002,2,102,'2024-02-11',2,NULL),
(1003,3,103,'2024-02-12',1,3000),
(1004,3,103,'2024-02-12',1,3000);
