INSERT INTO [Northwind].[dbo].[Movement]

SELECT CAT.CategoryName
	,[ProductName]
	,CAST(YEAR(INVOICE.OrderDate) as INT) as YEAR_X
	,sum(DETAILS.UnitPrice * DETAILS.Quantity) as AMOUNT
FROM [Northwind].[dbo].[Products] as PROD

INNER JOIN [Northwind].[dbo].[Categories] as CAT
ON (PROD.CategoryID=CAT.CategoryID)

INNER JOIN [Northwind].[dbo].[Order Details] as DETAILS
ON (PROD.ProductID=DETAILS.ProductID)

INNER JOIN [Northwind].[dbo].[Orders] as INVOICE
ON (DETAILS.OrderID=INVOICE.OrderID)

GROUP BY CAT.CategoryName, PROD.ProductName, YEAR(INVOICE.OrderDate)