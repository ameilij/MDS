UPDATE [Northwind].[dbo].[Movement]
SET SumOrder = SumOrder * 1.05
WHERE YEAR(OrderYear) = 1998