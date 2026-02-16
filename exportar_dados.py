from queries import get_faturamento_por_produto, get_kpis_gerais

get_faturamento_por_produto().to_csv("faturamento_produto.csv", index=False)
get_kpis_gerais().to_csv("kpis.csv", index=False)