/* ejercicio 8 */

SELECT Top 5 PROD.ProductName, sum([Quantity]) as SUBTOTAL
FROM [Northwind].[dbo].[Order Details] AS MOVEMENT
INNER JOIN
[Northwind].[dbo].[Products] AS PROD
ON (MOVEMENT.ProductID=PROD.ProductID)
GROUP BY PROD.ProductName
ORDER BY [SUBTOTAL] DESC