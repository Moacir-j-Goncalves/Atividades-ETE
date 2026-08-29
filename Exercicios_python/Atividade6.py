
# ==========================
# ATIVIDADE 6
# Validação de Acesso
# ==========================

idade = int(input("Digite sua idade: "))
ano = float(input("Digite o tempo de empresa em anos: "))
mes = float(input("Digite quantos meses de empresa: "))

total = ano * 12 + mes


if idade >= 18 and total > 24:
    print("Acesso Premium")
else:
    print("Acesso Standard")
