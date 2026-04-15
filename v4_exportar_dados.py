import pandas as pd
import argparse
from pathlib import Path
from v1_database import get_engine
from v2_queries import get_faturamento_por_produto, get_top_lojas, get_kpis_gerais, get_vendas_por_pais, get_faturamento_por_categoria_produto


BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "raw"
RAW_DIR.mkdir(exist_ok=True)


EXPORTERS = {
    "produto": (get_faturamento_por_produto, RAW_DIR/"faturamento_produto.csv"),
    "lojas":   (get_top_lojas,               RAW_DIR/"top_lojas.csv"),
    "kpis":    (get_kpis_gerais,             RAW_DIR/"kpis.csv"),
    "pais":    (get_vendas_por_pais,         RAW_DIR/"vendas_por_pais.csv"),
    "categoria":(get_faturamento_por_categoria_produto, RAW_DIR/"categoria.csv"),
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=list(EXPORTERS) + ["all"], default="all")
    args = parser.parse_args()

    targets = EXPORTERS.items() if args.dataset == "all" else [(args.dataset, EXPORTERS[args.dataset])]
    for name, (fn, path) in targets:
        fn().to_csv(path, index=False)
        print(f"✓ {name} → {path}")