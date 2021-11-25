"""
Open Requests:
Write a SQL query to get a list of all buildings and the number of open requests (Requests in which status equals'Open').
"""

"""
SELECT BuildingName
FROM Buildings
LEFT JOIN 
(SELECT Apartments.BuildingID, count(*) as 'Count'
 FROM Requests INNER JOIN Apartments
 ON Requests.AptID = Apartments.AptID
 WHERE Requests.Status = 'Open'
 GROUP BY Apartments.BuildingID) ReqCounts
ON Buildings.BuildingID = ReqCounts.BuildingID;
"""