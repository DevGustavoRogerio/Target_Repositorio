faturamento_diario = [
    22174.1664, 
    24537.6698, 
    26139.6134, 
    0.0,
    0.0,
    26742.6612,
    0.0,
    42889.2258,
    46251.174,
    11191.4722,
    0.0,
    0.0,
    3847.4823,
    373.7838,
    2659.7563,
    48924.2448,
    18419.2614,
    0.0,
    0.0,
    35240.1826,
    43829.1667,
    18235.6852,
    4355.0662,
    13327.1025
]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
faturamento_valido = [valor for valor in faturamento_diario if valor > 0]
media_mensal = sum(faturamento_valido) / len(faturamento_valido)
acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Média mensal: {media_mensal}")
print(f"Número de dias com faturamento acima da média: {acima_media}")
