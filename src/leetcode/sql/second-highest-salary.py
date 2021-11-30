# Source: https://leetcode.com/problems/second-highest-salary
"""
# Write your MySQL query statement below
SELECT
(
SELECT salary AS 'SecondHighestSalary'
FROM Employee
GROUP BY salary
ORDER BY salary DESC LIMIT 1,1
) as SecondHighestSalary
FROM Dual;
"""