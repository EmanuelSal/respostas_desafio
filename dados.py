# IMPORTANDO A BIBLIOTECA JSON
import json

# LEITURA DO FATURAMENTO DIÁRO 
with open('dados.json', 'r') as f:
    faturamento = json.load(f)

# CÁLCULO DO MENOR VALOR DE FATURAMENTO DIÁRIO
menor_valor = min(faturamento)

# CÁLCULO DO MAIOR VALOR DE FATURAMENTO DIÁRIO
maior_valor = max(faturamento)

# CÁLCULO DA MÉDIA DE FATURAMENTO DIÁRIO (EXCLUINDO DIAS SEM FATURAMENTO)
faturamento_sem_zero = [f for f in faturamento if f > 0]
media = sum(faturamento_sem_zero) / len(faturamento_sem_zero)

# CÁLCULANDO O NÚMERO DE DIAS EM QUE O FATURAMENTO FOI SUPERIOR À MÉDIA MENSAL
dias_acima_da_media = sum(f > media for f in faturamento)

# RESULTADOS
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média:", dias_acima_da_media)
