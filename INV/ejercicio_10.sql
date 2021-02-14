/* ejercicio 10 */

SELECT CUST.CompanyName, count([OrderID]) AS subtotal
FROM [Northwind].[dbo].[Orders] AS ORDS

INNER JOIN
[Northwind].[dbo].[Customers] as CUST
ON (ORDS.CustomerID=CUST.CustomerID)

GROUP BY (CUST.CompanyName)
HAVING count(ORDS.OrderID)=0
