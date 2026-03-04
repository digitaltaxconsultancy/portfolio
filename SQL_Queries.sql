-- ==========================================
-- HR Analytics Project - SQL Queries
-- Table: ibm_hr_employee_attrition_data
-- ==========================================

CREATE DATABASE IF NOT EXISTS hr_project;
USE hr_project;

-- Create Table
CREATE TABLE IF NOT EXISTS ibm_hr_employee_attrition_data (
    Age INT,
    Attrition VARCHAR(10),
    Department VARCHAR(50),
    JobRole VARCHAR(50),
    MonthlyIncome INT,
    YearsAtCompany INT,
    Gender VARCHAR(10),
    Education INT,
    MaritalStatus VARCHAR(20),
    OverTime VARCHAR(10),
    JobSatisfaction INT
);

-- ==========================================
-- BASIC ANALYSIS
-- ==========================================

-- Total Employees
SELECT COUNT(*) AS Total_Employees
FROM ibm_hr_employee_attrition_data;

-- Attrition Count
SELECT COUNT(*) AS Attrition_Count
FROM ibm_hr_employee_attrition_data
WHERE Attrition = 'Yes';

-- Attrition Rate (%)
SELECT 
    (SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) 
    AS Attrition_Rate_Percentage
FROM ibm_hr_employee_attrition_data;

-- Department Wise Attrition
SELECT Department, COUNT(*) AS Attrition_Count
FROM ibm_hr_employee_attrition_data
WHERE Attrition = 'Yes'
GROUP BY Department
ORDER BY Attrition_Count DESC;

-- Job Role Wise Attrition
SELECT JobRole, COUNT(*) AS Attrition_Count
FROM ibm_hr_employee_attrition_data
WHERE Attrition = 'Yes'
GROUP BY JobRole
ORDER BY Attrition_Count DESC;

-- Average Salary by Job Role
SELECT JobRole, ROUND(AVG(MonthlyIncome),2) AS Avg_Salary
FROM ibm_hr_employee_attrition_data
GROUP BY JobRole
ORDER BY Avg_Salary DESC;

-- Salary Category Distribution
SELECT 
    CASE
        WHEN MonthlyIncome < 3000 THEN 'Low Salary'
        WHEN MonthlyIncome BETWEEN 3000 AND 7000 THEN 'Medium Salary'
        ELSE 'High Salary'
    END AS Salary_Category,
    COUNT(*) AS Employee_Count
FROM ibm_hr_employee_attrition_data
GROUP BY Salary_Category;

-- Years at Company vs Attrition
SELECT YearsAtCompany, COUNT(*) AS Attrition_Count
FROM ibm_hr_employee_attrition_data
WHERE Attrition = 'Yes'
GROUP BY YearsAtCompany
ORDER BY YearsAtCompany;

-- Gender Distribution
SELECT Gender, COUNT(*) AS Total_Employees
FROM ibm_hr_employee_attrition_data
GROUP BY Gender;

-- Overtime Impact
SELECT OverTime, COUNT(*) AS Attrition_Count
FROM ibm_hr_employee_attrition_data
WHERE Attrition = 'Yes'
GROUP BY OverTime;