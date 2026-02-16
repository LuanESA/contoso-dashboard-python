# queries.py
import pandas as pd
from database import get_engine


def executar_query(query):
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)


# =============================
# Faturamento por Produto
# =============================

def get_faturamento_por_produto():
    query = """
    SELECT 
        dp.ProductKey,
        dp.ProductName,
        SUM(fs.SalesAmount) AS Total,
        SUM(fs.TotalCost) AS Custo
    FROM FactSales fs
    LEFT JOIN DimProduct dp
        ON fs.ProductKey = dp.ProductKey
    GROUP BY dp.ProductKey, dp.ProductName
    """
    return executar_query(query)


# =============================
# Faturamento por Loja
# =============================

def get_top_lojas():
    query = """
    SELECT 
        ds.StoreKey,
        ds.StoreName,
        SUM(fs.SalesAmount) AS Total
    FROM FactSales fs
    LEFT JOIN DimStore ds
        ON fs.StoreKey = ds.StoreKey
    GROUP BY ds.StoreKey, ds.StoreName
    """
    return executar_query(query)


# =============================
# Vendas por País
# =============================

def get_vendas_por_pais():
    query = """
    SELECT
        dg.RegionCountryName,
        SUM(fs.SalesAmount) AS Total
    FROM FactSales fs
    INNER JOIN DimStore ds
        ON fs.StoreKey = ds.StoreKey
    INNER JOIN DimGeography dg
        ON ds.GeographyKey = dg.GeographyKey
    GROUP BY dg.RegionCountryName
    """
    return executar_query(query)


# =============================
# KPIs Gerais
# =============================

def get_kpis_gerais():
    query = """
    SELECT
        SUM(SalesAmount) AS Faturamento,
        SUM(TotalCost) AS Custo,
        SUM(SalesAmount) - SUM(TotalCost) AS Lucro,
        SUM(SalesQuantity) AS Quantidade,
        SUM(SalesAmount) / SUM(SalesQuantity) AS Ticket_Medio
    FROM FactSales

    """
    return executar_query(query)
