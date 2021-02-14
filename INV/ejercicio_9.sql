/* ejercicio 9 */

SELECT Top 5 CAT.CategoryName as CATEGORIA, sum([Quantity]) as SUBTOTAL
FROM [Northwind].[dbo].[Order Details] AS MOVEMENT

INNER JOIN [Northwind].[dbo].[Products] AS PROD
ON (MOVEMENT.ProductID=PROD.ProductID)

INNER JOIN [Northwind].[dbo].[Categories] AS CAT
on (PROD.CategoryID=CAT.CategoryID)

GROUP BY CAT.CategoryName
ORDER BY [SUBTOTAL] DESC