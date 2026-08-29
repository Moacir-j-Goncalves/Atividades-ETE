# ==========================
# ATIVIDADE 2
# Simulador de Meta de Economia
# ==========================

print("você esta economizando todo mês você Guarda 20%. do seu salario para compara um video game 600 R$")

mes1= float(input("Qual o valor que voce recebeu no primeiro mês? "))
mes2= float(input("Qual o valor que voce recebeu no segundo  mês? "))
mes3= float(input("Qual o valor que voce recebeu no terceiro mês? "))

econ = (mes1 * 0.20) + (mes2* 0.20)  + (mes3* 0.20) 
porc = (econ)

if porc >= 600:
    print("Você conseguiu seu objetivo! :D")

elif porc >=500:
    print("Ainda falta pouco para alcançar :/")

else: 
    print ("Não foi dessa vez que você conseguiu :C")

# print("seu valor quardado foi {:.2f}".format(porc))



resultado = ((2/3 - (5 -3 )) + 1 ) * 5 
print(f"O resultado da expressão é : {resultado}")
