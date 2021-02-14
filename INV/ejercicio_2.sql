/****** Script for SelectTopNRows command from SSMS  ******/
SELECT count([Country]) as TOTAL_CLIENTES
FROM [Northwind].[dbo].[Customers]
WHERE [Country] like 'Brazil' AND [Region] IS NOT NULL