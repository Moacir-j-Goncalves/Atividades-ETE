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

