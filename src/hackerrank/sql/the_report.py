# Link to Question: https://www.hackerrank.com/challenges/the-report

"""
/*
Enter your query here.
*/

SELECT CASE WHEN Grade >= 8 THEN Name
         ELSE "NULL" END AS Name,
         Grade, Marks
FROM (SELECT Name, Marks FROM Students) C,  Grades
WHERE Marks >= Min_Mark and Marks <= Max_Mark
ORDER BY Grade DESC, Name ASC;
"""