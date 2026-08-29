
# ==========================
# ATIVIDADE 8
# Simulador de Caixa Eletrônico
# ==========================

while True:
    valor = int(input("Digite o valor do saque: "))

    if valor > 0 and valor % 10 == 0:
        break

    print("Valor inválido. Digite um múltiplo de 10.")

nota50 = valor // 50
valor %= 50

nota20 = valor // 20
valor %= 20

nota10 = valor // 10

print("Notas de R$50:", nota50)
print("Notas de R$20:", nota20)
print("Notas de R$10:", nota10)

