# queries.py
import os
import pandas as pd
from v1_database import get_engine

ENV = os.environ.get("ENV", "local")


def _get_df(query: str) -> pd.DataFrame:
    """Executa uma query SQL e retorna um DataFrame. Uso interno."""
    with get_engine().connect() as conn:
        return pd.read_sql(query, conn)


# =============================
# Faturamento por Produto
# =============================
def get_faturamento_por_produto() -> pd.DataFrame:
    if ENV == "cloud":
        return pd.read_csv("raw/faturamento_produto.csv")

    return _get_df("""
        SELECT
            dp.ProductKey,
            dp.ProductName,
            SUM(fs.SalesAmount) AS Total,
            SUM(fs.TotalCost)   AS Custo
        FROM FactSales fs
        LEFT JOIN DimProduct dp ON fs.ProductKey = dp.ProductKey
        GROUP BY dp.ProductKey, dp.ProductName
    """)


# =============================
# Faturamento por Loja
# =============================
def get_top_lojas() -> pd.DataFrame:
    if ENV == "cloud":
        return pd.read_csv("raw/top_lojas.csv")

    return _get_df("""
        SELECT
            ds.StoreKey,
            ds.StoreName,
            SUM(fs.SalesAmount) AS Total
        FROM FactSales fs
        LEFT JOIN DimStore ds ON fs.StoreKey = ds.StoreKey
        GROUP BY ds.StoreKey, ds.StoreName
    """)


# =============================
# Vendas por País
# =============================
def get_vendas_por_pais() -> pd.DataFrame:
    if ENV == "cloud":
        return pd.read_csv("raw/vendas_por_pais.csv")

    return _get_df("""
        SELECT
            dg.RegionCountryName,
            SUM(fs.SalesAmount) AS Total
        FROM FactSales fs
        INNER JOIN DimStore    ds ON fs.StoreKey       = ds.StoreKey
        INNER JOIN DimGeography dg ON ds.GeographyKey  = dg.GeographyKey
        GROUP BY dg.RegionCountryName
    """)


# =============================
# KPIs Gerais
# =============================
def get_kpis_gerais() -> pd.DataFrame:
    if ENV == "cloud":
        return pd.read_csv("raw/kpis.csv")

    return _get_df("""
        SELECT
            SUM(SalesAmount)                              AS Faturamento,
            SUM(TotalCost)                                AS Custo,
            SUM(SalesAmount) - SUM(TotalCost)             AS Lucro,
            SUM(SalesQuantity)                            AS Quantidade,
            SUM(SalesAmount) / SUM(SalesQuantity)         AS Ticket_Medio
        FROM FactSales
    """)


# =============================
# Faturamento por Categoria
# =============================
def get_faturamento_por_categoria_produto() -> pd.DataFrame:
    if ENV == "cloud":
        return pd.read_csv("raw/categoria.csv")

    return _get_df("""
        SELECT
            dp.ProductKey,
            dp.ProductName,
            dpc.ProductCategoryName AS Categoria_Produto,
            SUM(fs.SalesAmount)     AS Total,
            SUM(fs.TotalCost)       AS Custo
        FROM FactSales fs
        INNER JOIN DimProduct            dp   ON fs.ProductKey          = dp.ProductKey
        INNER JOIN DimProductSubCategory dpsc ON dp.ProductSubcategoryKey = dpsc.ProductSubcategoryKey
        INNER JOIN DimProductCategory    dpc  ON dpsc.ProductCategoryKey  = dpc.ProductCategoryKey
        GROUP BY dp.ProductKey, dp.ProductName, dpc.ProductCategoryName
    """)