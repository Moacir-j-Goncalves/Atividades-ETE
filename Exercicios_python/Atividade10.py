# ==========================
# ATIVIDADE 10
# Análise de Dados de Telemetria
# ==========================

quantidade = int(input("Quantas temperaturas deseja registrar? "))

soma = 0
maior = None
acima_28 = 0

for i in range(quantidade):
    temperatura = float(input(f"Digite a {i+1}ª temperatura: "))

    soma += temperatura

    if maior is None or temperatura > maior:
        maior = temperatura

    if temperatura > 28:
        acima_28 += 1

media = soma / quantidade

print("Temperatura média:", round(media, 2), "°C")
print("Maior temperatura:", maior, "°C")
print("Quantidade acima de 28°C:", acima_28)
