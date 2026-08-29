
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