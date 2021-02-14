
SELECT [Discontinued], count([Discontinued]) as SUBTOTAL
FROM [Northwind].[dbo].[Products]
GROUP BY [Discontinued]