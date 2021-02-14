/* Ejercicio 4  */

SELECT [ProductName]
      ,[QuantityPerUnit]
      ,[UnitPrice]
  FROM [Northwind].[dbo].[Products]
  WHERE [Discontinued] = 0 AND [UnitPrice] >= 20 AND [UnitPrice] <= 30