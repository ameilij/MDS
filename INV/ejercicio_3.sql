/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [ProductName]
      ,[UnitsInStock]
      ,[UnitsOnOrder]
	  ,[Discontinued]
  FROM [Northwind].[dbo].[Products]
  WHERE [Discontinued]=1