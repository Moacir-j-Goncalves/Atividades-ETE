# ==========================
# ATIVIDADE 2
# Operações Aritméticas Básicas
# ==========================

aluno1 = float(input("Digite um número: "))
aluno2 = float(input("Digite outro número: "))

soma = aluno1 + aluno2

print(f"A soma é:", soma)


# ==========================
# ATIVIDADE 3
# Análise de Código Python
# ==========================

nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo ((F) para Feminino e (M) para Masculino): ")

print(nome)

if idade < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")

if sexo == "f":
    print("Seu sexo é Feminino")
else:
    print("Seu sexo é Masculino")


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

    


# ==========================
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


# ==========================
# ATIVIDADE 7
# Sistema de Helpdesk
# ==========================

print("1 - Problemas com Internet / Rede")
print("2 - Mau funcionamento de Hardware")
print("3 - Instalação ou Erro de Software")
print("4 - Troca de Senha / Acesso Corporativo")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Você será encaminhado para o setor de Redes.")
    case 2:
        print("Você será encaminhado para o setor de Hardware.")
    case 3:
        print("Você será encaminhado para o suporte de Software.")
    case 4:
        print("Você será encaminhado para o setor de Acesso Corporativo.")
    case _:
        print("Opção inválida.")


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


# ==========================
# ATIVIDADE 9
# Validador de Acesso de Segurança
# ==========================

senha_correta = "Admin@2026"

for tentativa in range(1, 4):
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta.")

else:
    print("Conta bloqueada temporariamente.")


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





# no= input("Qual o nome do aluno: ")
# n1= float(input("Digite sua 1° nota: "))
# n2= float(input("Digite sua 2° nota: "))
# n3= float(input("Digite sua 3° nota: "))
# n4= float(input("Digite sua 4° nota: "))


# me= (n1 + n2 + n3 + n4)/4

# if me >= 7: 

#      print("Aprovado(a)") 

# elif me == 6:
#      print ("Recuperação")


# else: 
    
#      print("Reprovado(a)")


 
# print("você esta economizando todo mês você Guarda 20%. do seu salario para compara um video game 600 R$")

# mes1= float(input("Qual o valor que voce recebeu no primeiro mês? "))
# mes2= float(input("Qual o valor que voce recebeu no segundo  mês? "))
# mes3= float(input("Qual o valor que voce recebeu no terceiro mês? "))

# econ = (mes1 * 0.20) + (mes2* 0.20)  + (mes3* 0.20) 
# porc = (econ)

# if porc >= 600:
#     print("Você conseguiu seu objetivo! :D")

# elif porc >=500:
#     print("Ainda falta pouco para alcançar :/")

# else: 
#     print ("Não foi dessa vez que você conseguiu :C")

# # print("seu valor quardado foi {:.2f}".format(porc))



# resultado = ((2/3 - (5 -3 )) + 1 ) * 5 
# print(f"O resultado da expressão é : {resultado}")







# =======================================================================================
# guanabara atividades 
# ======================================================================================







# # n1= int (input("Digite um numero:"))
# # #n2= float (input("Digite outro numero:"))

# # d = n1 * 2
# # t = n1 * 3
# # r =n1 **(1/2)
# # print("o dobro de {} vale {}".format(n1, d))
# # print("o triblo de {} vale {}.\nA raiz quadrada de {} vale {:.2f}".format(n1, t, n1, r))
# # print(n1*2,n1**3, n1**1\2) |outra forma|

# # ma= n1 + n2 
# # me = (n1 + n2) / 2
# # print("{} esse valor somado a esse outro {} é {}".format(n1, n2, ma))
# # print("a media desses números  é {:.2f}".format(me))

# # medida= float (input(" uma distáncia em metros:"))
# # km= medida /1000
# # hm= medida /100
# # dam= medida /10
# # dm=medida * 10
# # cm = medida * 100
# # mm = medida * 1000
# # print("A medida de {}km corresponde a\n {}hm \n e {}dam \n e {}dm \n e {}cm \n e {}mm".format(medida, km, hm, dam, dm, cm, mm))



# # print("-"* 12)
# # tab= int(input("Digite um número para ver sua tabuada:"))
# # print("{} x {} = {}".format(tab, 1, tab * 1))
# # print("{} x {} = {}".format(tab, 2, tab * 2))
# # print("{} x {} = {}".format(tab, 3, tab * 3))
# # print("{} x {} = {}".format(tab, 4, tab * 4))
# # print("{} x {} = {}".format(tab, 5, tab * 5))
# # print("{} x {} = {}".format(tab, 6, tab * 6))
# # print("{} x {} = {}".format(tab, 7, tab * 7))
# # print("{} x {} = {}".format(tab, 8, tab * 8))
# # print("{} x {} = {}".format(tab, 9, tab * 9))
# # print("{} x {} = {}".format(tab, 10, tab * 10))
# # print("-" * 12)



# # dinheiro= float(input("quanto dinheiro vocé tem na carteira? R$"))
# # dolar= dinheiro /5.14
# # print("seu valor é R${} coonvertido em dolar fica US${:.2f}".format(dinheiro, dolar))



# # lp= float(input("larguura da parede:"))
# # alt= float(input("altura da parede:"))
# # cvs= lp * alt
# # di= cvs /2
# # print("sua parede tem a dimenção de {:.2f}m² x {:.2f}m² e sua area é de {:.2f}m².".format(lp, alt, cvs,))
# # print("Para pintar sua parede, vocé precisará de {:.2f}l de tinta.".format(di)



# # preço= float(input("qual o valor do seu produto? R$"))
# # novo= preço *5/ 100
# # # desconto= preço - novo
# # print("seu valor é {}R$ você teve um descontoo de 5% que ficou {:.2f}R$ você pagará {:.2f}R$".format(preço, novo, desconto))




# # salario= float(input("Qual o valor do salario do funcionário? R$"))
# # aumento= salario +(salario *15/100)
# # print("Um funcionario que ganhava R${:.2f}, com 15%  de aumento, passa a receber R${:.2f}".format(salario, aumento))


# # tem= float(input("Informe a temperatura em °C:"))
# # f= ((9 * tem)/ 5)+ 32
# # print("A temperatura de {}°C corespponden a {}°F".format(tem, f))

# # dia= int(input("Quantos dia o carro ficou alugado?"))
# # km=float(input("Quantos KM rodados?"))
# # tot=(dia* 60) + (km * 0.15)
# # print("O total a pagar pelo aluguel é:R${}".format(tot))

# # math (ceil{arredonda p/ cima}, floor{arredonda p/ baixo}, trunc{elimina da "," pra frente}, pow {potência}, sqrt {raiz quadrada}, factorial  )

# # import math
# # num= int(input("digite um número:"))
# # raiz = math.sqrt(num)
# # print("A raiz quadrada de {} é igual a {}".format(num, raiz))


# # import math
# # num = float(input("Digite um número: "))
# # print("seu numero foi {} e a porção inteira dele é {}".format(num, math.trunc(num)))


# n11= float (input("comprimento do cateto oposto:"))
# n21= float (input("comprimento do cateto adjacente:"))
# hi = (n11 **2 + n21 ** 2) ** (1/2)
# print("A hipotenusa vai medir {:.2f}". format(hi))
# #
# nome= input("Digite seu nome: ")
# val= float(input("Digite o valor do seu salário: "))


# if val <= 1903.99:
#    imposto = "Isento"

# elif val <= 2826.65: 
#     imposto =(val* 0.075)

# elif val <= 3751.05: 
#     imposto =(val* 0.15)

# elif val <= 4664.68: 
#     imposto =(val* 0.225)

# else:
#     val >= 4664.68 
#     imposto =(val* 0.25)

# print("{} Seu salario foi {} e sua situação de imposto é: {}".format (nome, val, imposto ) )




print("Digite seu Nome:")
nome = input()

print("Digite seu Sobrenome:")
sobrenome = input()

print("Digite sua Idade:")
idade = input()

print("Digite seu Peso:")
peso = input()

print(f"Olá {nome} {sobrenome}! Você tem {idade} anos e seu peso é {peso}.")



















