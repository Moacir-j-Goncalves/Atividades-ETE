# ==========================
# ATIVIDADE 4
# Classificador de Clientes
# ==========================

gasto = float(input("Digite o valor gasto que você gastou: R$ "))

if gasto < 1000:
    print("Categoria Bronze")
    print("Sem desconto")
    

elif gasto < 3000:
    print("Categoria Prata")
    print("Desconto de 5%")

elif gasto < 5000:
    print("Categoria Ouro")
    print("Desconto de 10%")

else:
    print("Categoria Platinum")
    print("Desconto de 15%")

    