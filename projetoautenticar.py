import projetomenur
import projetocoretc
import os

def autenticar():
    os.system("cls")
    senha_correta = "Tripulação"
    tentativas = 3

    while tentativas > 0:
        senha = input("\033[1;33mDigite a senha de acesso: ")
        if senha == senha_correta:
            print("Autenticado com sucesso!")
            return True
        else:
            tentativas -= 1
            projetocoretc.printRed(f"Senha incorreta. Tentativas restantes: {tentativas}")
    
    projetocoretc.printRed("Acesso negado.")
    return False