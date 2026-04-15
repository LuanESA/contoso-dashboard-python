# 📊 Dashboard Executivo — Contoso Retail

Dashboard interativo de análise de vendas construído com **Python** e **Streamlit**, conectado ao banco de dados **Contoso Retail DW** (Microsoft SQL Server).

O projeto transforma dados transacionais brutos em indicadores de negócio acionáveis: faturamento, margem, análise ABC de produtos, performance de lojas e distribuição geográfica de vendas.

---

## 📁 Estrutura do projeto

```
contoso-dashboard/
│
├── app.py                  # Interface Streamlit (entry point)
├── v1_database.py             # Conexão com SQL Server via SQLAlchemy
├── v2_queries.py              # Consultas SQL ao banco de dados
├── v3_services.py             # Regras de negócio e transformações
├── v4_exportar_dados.py       # Script para exportar CSVs (modo cloud)
│
├── raw/                    # CSVs gerados para deploy em cloud
│   ├── faturamento_produto.csv
│   ├── top_lojas.csv
│   ├── vendas_por_pais.csv
│   ├── kpis.csv
│   └── categoria.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Pré-requisitos

* Python 3.10+
* ODBC Driver 17 for SQL Server
  👉 https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server
* Acesso ao banco `ContosoRetailDW` (modo local) **ou** CSVs na pasta `raw/` (modo cloud)

---

## 🚀 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seuusuario/contoso-dashboard
cd contoso-dashboard
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

Conteúdo do `.env`:

```env
ENV=local
DB_SERVER=nome-do-seu-servidor
DB_DATABASE=ContosoRetailDW
```

### 4. Executar a aplicação

```bash
streamlit run app.py
```

---

## 🔄 Modos de execução

| Variável `ENV` | Fonte de dados       | Quando usar                    |
| -------------- | -------------------- | ------------------------------ |
| `local`        | SQL Server via ODBC  | Desenvolvimento local          |
| `cloud`        | CSVs na pasta `raw/` | Deploy (Streamlit Cloud, etc.) |

Para gerar os CSVs antes de fazer deploy:

```bash
python exportar_dados.py --dataset all
```

---

## 📊 Funcionalidades

### 📈 Visão Executiva

* Faturamento total
* Lucro
* Margem
* Ticket médio

### 📦 Produtos

* Classificação ABC por faturamento
* Top 10 produtos com gráfico interativo
* Detalhamento por categoria

### 🏬 Lojas

* Ranking de lojas por faturamento
* Participação percentual por loja

### 🌍 Países

* Distribuição geográfica das vendas
* Ranking e participação por país

---

## 🛠️ Tecnologias

| Tecnologia    | Uso                         |
| ------------- | --------------------------- |
| Python 3.10+  | Linguagem principal         |
| Streamlit     | Interface do dashboard      |
| Pandas        | Manipulação de dados        |
| SQLAlchemy    | Conexão com banco de dados  |
| PyODBC        | Driver ODBC para SQL Server |
| python-dotenv | Variáveis de ambiente       |

---

## 📚 Sobre o dataset

O **Contoso Retail DW** é um banco de dados de demonstração disponibilizado pela Microsoft, contendo dados fictícios de uma rede varejista global.

Mais informações:
👉 https://www.microsoft.com/en-us/download/details.aspx?id=18279

---

## 🔮 Próximas melhorias

* [ ] Evolução mensal de faturamento (análise temporal)
* [ ] Gráficos com Plotly (hover + formatação de moeda)
* [ ] Margem de lucro por categoria
* [ ] Detecção de anomalias em vendas por loja
