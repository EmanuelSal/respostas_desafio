faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# CÁLCULANDO O VALOR TOTAL MENSAL DA DISTRIBUIDORA
valor_total = sum(faturamento_estados.values())

# CALCULANDO O PERCENTUAL DE REPRESENTAÇÃO DE CADA ESTADO
percentuais = {}
for estado, valor in faturamento_estados.items():
    percentuais[estado] = (valor / valor_total) * 100

# RESULTADO | IMPRESSÃO
for estado, percentual in percentuais.items():
    print(estado, ":", round(percentual, 2), "%")
