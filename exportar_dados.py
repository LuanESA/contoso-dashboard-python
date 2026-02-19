import pandas as pd
from database import get_engine

engine = get_engine()

# =============================
# Faturamento por Produto
# =============================
#query_produto = """
#SELECT 
#    dp.ProductKey,
#    dp.ProductName,
#    SUM(fs.SalesAmount) AS Total,
#    SUM(fs.TotalCost) AS Custo
#FROM FactSales fs
#LEFT JOIN DimProduct dp
#    ON fs.ProductKey = dp.ProductKey
#GROUP BY dp.ProductKey, dp.ProductName
#"""
#
#df_produto = pd.read_sql(query_produto, engine)
#df_produto.to_csv("faturamento_produto.csv", index=False)
#
#
## =============================
## Top Lojas
## =============================
#query_lojas = """
#SELECT 
#    ds.StoreKey,
#    ds.StoreName,
#    SUM(fs.SalesAmount) AS Total
#FROM FactSales fs
#LEFT JOIN DimStore ds
#    ON fs.StoreKey = ds.StoreKey
#GROUP BY ds.StoreKey, ds.StoreName
#"""
#
#df_lojas = pd.read_sql(query_lojas, engine)
#df_lojas.to_csv("top_lojas.csv", index=False)
#
#
## =============================
## Vendas por País
## =============================
#query_pais = """
#SELECT
#    dg.RegionCountryName,
#    SUM(fs.SalesAmount) AS Total
#FROM FactSales fs
#INNER JOIN DimStore ds
#    ON fs.StoreKey = ds.StoreKey
#INNER JOIN DimGeography dg
#    ON ds.GeographyKey = dg.GeographyKey
#GROUP BY dg.RegionCountryName
#"""
#
#df_pais = pd.read_sql(query_pais, engine)
#df_pais.to_csv("vendas_por_pais.csv", index=False)
#
#
## =============================
## KPIs Gerais
## =============================
#query_kpis = """
#SELECT
#    SUM(SalesAmount) AS Faturamento,
#    SUM(TotalCost) AS Custo,
#    SUM(SalesAmount) - SUM(TotalCost) AS Lucro,
#    SUM(SalesQuantity) AS Quantidade,
#    SUM(SalesAmount) / SUM(SalesQuantity) AS Ticket_Medio
#FROM FactSales
#"""
#
#df_kpis = pd.read_sql(query_kpis, engine)
#df_kpis.to_csv("kpis.csv", index=False)
#
#engine.dispose()
#
#print("CSV gerados com sucesso 🚀")




# =============================
# Faturamento por categoria dos produtos
# =============================


query_categoria = """
SELECT
    dp.ProductKey,
    dp.ProductName,
    dpc.ProductCategoryName AS Categoria_Produto,
    SUM(fs.SalesAmount) AS Total,
    SUM(fs.TotalCost) AS Custo
FROM FactSales fs
INNER JOIN DimProduct dp
    ON fs.ProductKey = dp.ProductKey
INNER JOIN DimProductSubCategory dpsc
    ON dp.ProductSubcategoryKey = dpsc.ProductSubcategoryKey
INNER JOIN DimProductCategory dpc
    ON dpsc.ProductCategoryKey = dpc.ProductCategoryKey
GROUP BY
    dp.ProductKey,
    dp.ProductName,
    dpc.ProductCategoryName;
"""

df_categoria = pd.read_sql(query_categoria, engine)
df_categoria.to_csv("categoria.csv", index=False)

engine.dispose()

print("CSV gerados com sucesso 🚀")