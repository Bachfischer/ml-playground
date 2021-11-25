"""
Multiple Apartments:
Write a SOL query to get a list of tenants who are renting more than one apartment.
"""

"""
SELECT TenantName
FROM Tenants
INNER JOIN
(SELECT TenantID FROM AptTenants GROUP BY TenantID HAVING COUNT(*) > 1) C
ON Tenants.TenantID = C.TenantID;
"""