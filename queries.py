import os
import pandas as pd

ENV = os.environ.get("ENV", "local")


# =============================
# Faturamento por Produto
# =============================
def get_faturamento_por_produto():

    if ENV == "cloud":
        return pd.read_csv("faturamento_produto.csv")

    else:
        from database import get_engine
        engine = get_engine()

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

        return pd.read_sql(query, engine)


# =============================
# Faturamento por Loja
# =============================
def get_top_lojas():

    if ENV == "cloud":
        return pd.read_csv("top_lojas.csv")

    else:
        from database import get_engine
        engine = get_engine()

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

        return pd.read_sql(query, engine)


# =============================
# Vendas por País
# =============================
def get_vendas_por_pais():

    if ENV == "cloud":
        return pd.read_csv("vendas_por_pais.csv")

    else:
        from database import get_engine
        engine = get_engine()

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

        return pd.read_sql(query, engine)


# =============================
# KPIs Gerais
# =============================
def get_kpis_gerais():

    if ENV == "cloud":
        return pd.read_csv("kpis.csv")

    else:
        from database import get_engine
        engine = get_engine()

        query = """
        SELECT
            SUM(SalesAmount) AS Faturamento,
            SUM(TotalCost) AS Custo,
            SUM(SalesAmount) - SUM(TotalCost) AS Lucro,
            SUM(SalesQuantity) AS Quantidade,
            SUM(SalesAmount) / SUM(SalesQuantity) AS Ticket_Medio
        FROM FactSales
        """

        return pd.read_sql(query, engine)




def get_faturamento_por_categoria_produto():
    if ENV == "cloud":
        return pd.read_csv('categoria.csv')
    
    else:
        from database import get_engine
        engine = get_engine()

        query = """
        SELECT
            dp.ProductKey,
            dp.ProductName,
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
            dp.ProductName;
        """

        return pd.read_sql(query, engine)