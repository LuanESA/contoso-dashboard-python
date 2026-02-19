import pandas as pd
from queries import (
    get_faturamento_por_produto,
    get_kpis_gerais,    
    get_top_lojas,
    get_vendas_por_pais,
    get_faturamento_por_categoria_produto
)

# Genericos - Gerais

def aplicar_ranking(df, coluna):
    df = df.sort_values(coluna, ascending=False)
    df['Ranking'] = range(1, len(df) + 1)
    return df


def aplicar_participacao(df, coluna):
    df['Participacao_%'] = df[coluna] / df[coluna].sum()
    return df

def aplicar_percentual_acumulado(df, coluna):
    df = df.sort_values(coluna, ascending=False)
    df['Percentual_Acumulado'] = (
        df[coluna].cumsum() / df[coluna].sum()
    )
    return df



# KPIs Gerais
def service_kpis():
    df = get_kpis_gerais()
    
    # Numero
    df['Faturamento'] = pd.to_numeric(df['Faturamento'])
    df['Lucro'] = pd.to_numeric(df['Lucro'])
    df['Quantidade'] = pd.to_numeric(df['Lucro'])

    # Metricas
    df['Margem_%'] = df['Lucro'] / df['Faturamento']
    df['Ticket Medio'] = df['Faturamento'] / df['Quantidade']

    return df


# produtos ABC

def service_produtos_abc():
    df = get_faturamento_por_produto()
    df['Total'] = pd.to_numeric(df['Total'])
    df = aplicar_participacao(df, 'Total')
    df = aplicar_percentual_acumulado(df, 'Total')

    def classifcar_abc(x):
        if x <= 8:
            return 'A'
        elif x <= 0.95:
            return 'B'
        else:
            return 'C'
        
    df['Classe_ABC'] = df['Percentual_Acumulado'].apply(classifcar_abc)
    df = aplicar_ranking(df, 'Total')

    return df


# top produtos

def service_top_produtos():
    df = get_top_lojas()

    df['Quantidade'] = pd.to_numeric(df['Quantidade'])
    df = aplicar_ranking(df, 'Quantidade')

    return df

# lojas

def service_lojas():
    df = get_top_lojas()

    df['Total'] = pd.to_numeric(df['Total'])

    df = aplicar_participacao(df, 'Total')
    df = aplicar_ranking(df, 'Total')

    return df

# vendas por pais

def service_paises():
    df = get_vendas_por_pais()

    df['Total'] = pd.to_numeric(df['Total'])

    df = aplicar_participacao(df, 'Total')
    df = aplicar_ranking(df , 'Total')

    return df


def service_categorias():
    df = get_faturamento_por_categoria_produto()
    df['Total'] = pd.to_numeric(df['Total'])
    df = aplicar_participacao(df, 'Total')
    df = aplicar_percentual_acumulado(df, 'Total')

    def classifcar_abc(x):
        if x <= 8:
            return 'A'
        elif x <= 0.95:
            return 'B'
        else:
            return 'C'
        
    df['Classe_ABC'] = df['Percentual_Acumulado'].apply(classifcar_abc)
    df = aplicar_ranking(df, 'Total')

    return df