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

