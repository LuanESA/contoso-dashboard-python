# app.py
import streamlit as st
import pandas as pd

from tratamento import (
    service_kpis,
    service_produtos_abc,
    service_lojas,
    service_paises
)

# =============================
# CONFIGURAÇÃO INICIAL
# =============================

st.set_page_config(
    page_title="Dashboard Executivo - Contoso",
    layout="wide"
)

st.title("📊 Dashboard Executivo - Contoso Retail")

# =============================
# MENU LATERAL
# =============================

menu = st.sidebar.radio(
    "Navegação",
    [
        "Visão Executiva",
        "Produtos",
        "Lojas",
        "Países"
    ]
)

# =============================
# VISÃO EXECUTIVA
# =============================

if menu == "Visão Executiva":

    st.subheader("📌 KPIs Gerais")

    df_kpis = service_kpis()

    faturamento = df_kpis.loc[0, "Faturamento"]
    lucro = df_kpis.loc[0, "Lucro"]
    margem = df_kpis.loc[0, "Margem_%"]
    ticket = df_kpis.loc[0, "Ticket_Medio"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Faturamento", f"R$ {faturamento:,.2f}")
    col2.metric("📈 Lucro", f"R$ {lucro:,.2f}")
    col3.metric("📊 Margem", f"{margem:.2%}")
    col4.metric("🧾 Ticket Médio", f"R$ {ticket:,.2f}")

    st.divider()

    st.info(
        "Este painel apresenta uma visão geral do desempenho de vendas, "
        "lucro e eficiência operacional da Contoso."
    )

# =============================
# PRODUTOS
# =============================

elif menu == "Produtos":

    st.subheader("📦 Análise de Produtos")

    df_prod = service_produtos_abc()

    # --- FILTRO ---
    classe = st.multiselect(
        "Filtrar por Classe ABC:",
        options=df_prod["Classe_ABC"].unique(),
        default=df_prod["Classe_ABC"].unique()
    )

    df_prod = df_prod[df_prod["Classe_ABC"].isin(classe)]

    # --- TOP 10 ---
    st.markdown("### 🔝 Top 10 Produtos por Faturamento")

    top10 = df_prod.sort_values("Total", ascending=False).head(10)

    st.bar_chart(
        top10.set_index("ProductName")["Total"]
    )

    # --- TABELA ---
    st.markdown("### 📋 Detalhamento dos Produtos")

    st.dataframe(
        df_prod[[
            "ProductName",
            "Total",
            "Participacao_%",
            "Percentual_Acumulado",
            "Classe_ABC",
            "Ranking"
        ]]
        .style.format({
            "Total": "R$ {:,.2f}",
            "Participacao_%": "{:.2%}",
            "Percentual_Acumulado": "{:.2%}"
        }),
        use_container_width=True
    )

# =============================
# LOJAS
# =============================

elif menu == "Lojas":

    st.subheader("🏬 Performance das Lojas")

    df_lojas = service_lojas()

    st.markdown("### 🔝 Top Lojas por Faturamento")

    top_lojas = df_lojas.sort_values("Total", ascending=False).head(10)

    st.bar_chart(
        top_lojas.set_index("StoreName")["Total"]
    )

    st.markdown("### 📋 Detalhamento por Loja")

    st.dataframe(
        df_lojas[[
            "StoreName",
            "Total",
            "Participacao_%",
            "Ranking"
        ]]
        .style.format({
            "Total": "R$ {:,.2f}",
            "Participacao_%": "{:.2%}"
        }),
        use_container_width=True
    )

# =============================
# PAÍSES
# =============================

elif menu == "Países":

    st.subheader("🌎 Vendas por País")

    df_paises = service_paises()

    st.markdown("### 🌍 Distribuição de Vendas por País")

    st.bar_chart(
        df_paises.set_index("RegionCountryName")["Total"]
    )

    st.markdown("### 📋 Detalhamento por País")

    st.dataframe(
        df_paises[[
            "RegionCountryName",
            "Total",
            "Participacao_%",
            "Ranking"
        ]]
        .style.format({
            "Total": "R$ {:,.2f}",
            "Participacao_%": "{:.2%}"
        }),
        use_container_width=True
    )
