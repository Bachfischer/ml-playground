# Link to Question: https://www.hackerrank.com/challenges/earnings-of-employees/

"""
/*
Enter your query here.
*/

SELECT months * salary, count(*)
FROM Employee
WHERE months * salary = (SELECT MAX(months * salary) FROM Employee)
GROUP BY months * salary
"""