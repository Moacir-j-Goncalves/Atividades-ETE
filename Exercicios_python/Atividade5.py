#  ==========================
# ATIVIDADE 5
# Promoção das Maçãs
# ==========================

quantidade = int(input("Digite a quantidade de maçãs a serem compradas: "))

if quantidade < 12:
    preco = 0.30
    com_desconto = False
else:
    preco = 0.25
    com_desconto = True

valor = quantidade * preco

print("A quantidade de maçãs compradas foi {} e o valor final ficou: R$ {:.2f}".format(quantidade, valor))

if com_desconto:
    print("Você recebeu desconto, pois comprou 12 ou mais maçãs.")
else:
    print("Você não teve desconto.")
