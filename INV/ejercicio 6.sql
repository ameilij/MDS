/* ejercicio 6*/

SELECT CAT.CategoryName, max([UnitPrice]) AS Precio_Maximo, min([UnitPrice]) as Precio_Minimo
FROM [Northwind].[dbo].[Products] AS PROD
INNER JOIN
[Northwind].[dbo].[Categories] AS CAT
ON (PROD.CategoryID=CAT.CategoryID)
GROUP BY CAT.CategoryName
HAVING max([UnitPrice]) > 50