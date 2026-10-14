"""Prepara a base de vendas Porsche para a dashboard.

Uso: python tratar_base.py caminho/da/planilha.xlsx
Gera: base_tratada.csv (a mesma tabela que vai embutida no index.html)
"""
import sys
import pandas as pd

ORIGEM = sys.argv[1] if len(sys.argv) > 1 else "planilha_porsche.xlsx"

df = pd.read_excel(ORIGEM, dtype=str)

# 1) Fica só com as colunas sanitizadas (mais o id da venda).
#    customer_name e salesperson ficam de fora: são dados pessoais e a base vai embutida no HTML.
base = pd.DataFrame({
    "id": df["sale_id"].astype(int),
    "modelo": df["PorscheModelSanitized"],
    "ano_modelo": df["ModelYearSanitized"].astype(int),
    "preco_usd": pd.to_numeric(df["SalesPriceSanitized"]).round(0).astype(int),
    "km_milhas": pd.to_numeric(df["VehicleMileageSanitized"]).astype(int),
    "pagamento": df["PayMethodSanitized"],
    "cidade": df["CitySanitized"],
    "estado": df["StateSanitized"],
    "status_original": df["DeliveryStatusSanitized"],
})

# 2) Família do modelo: 40 variações viram 6 famílias legíveis.
def familia(modelo: str) -> str:
    for f in ("911", "718", "Cayenne", "Macan", "Taycan", "Panamera"):
        if modelo.startswith(f):
            return f
    return "Outros"

base["familia"] = base["modelo"].map(familia)

# 3) Status de entrega: 10 valores viram 4 grupos.
GRUPOS = {
    "Delivered": "Entregue",
    "In Transit": "Em trânsito",
    "Shipped": "Em trânsito",
    "Pending": "Aguardando",
    "Pending Approval": "Aguardando",
    "Pending Review": "Aguardando",
    "Awaiting Review": "Aguardando",
    "Awaiting Delivery": "Aguardando",
    "Awaiting Pickup": "Aguardando",
    "Cancelled": "Cancelada",
}
base["status"] = base["status_original"].map(GRUPOS)

# 4) Conferências: nada vazio, nada fora dos grupos, preço e ano numéricos.
assert base.isna().sum().sum() == 0, "há valores vazios"
assert (base["familia"] != "Outros").all(), "modelo sem família"
assert base["id"].is_unique, "id repetido"

# A data de venda não entra: 24 dos 100 registros ficaram INVALID na sanitização.
base.to_csv("base_tratada.csv", index=False)
print(base.shape, "linhas e colunas gravadas em base_tratada.csv")
print(base["status"].value_counts().to_string())
