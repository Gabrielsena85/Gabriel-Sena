from projetocoretc import *
def listar_todas_vendas():
    try:
        # Abre o arquivo de vendas e lê todas as linhas
        with open("vendas.txt", "r", encoding="utf8") as arquivo:
            vendas = arquivo.readlines()

        # Verifica se o arquivo de vendas está vazio
        if not vendas:
            print("Nenhuma venda registrada.")
            input("\033[32mPrecione Enter Para Sair")
            return

        # Exibe um cabeçalho para as vendas
        printBlue(f"\n{'Código Venda':<15}{'Data':<12}{'Código Produto':<15}{'Quantidade Vendida':<20}")

        # Itera sobre cada linha do arquivo e exibe as informações de venda
        for venda in vendas:
            dados_venda = venda.strip().split(";")
            print(f"{dados_venda[0]:<15}{dados_venda[1]:<12}{dados_venda[2]:<15}{dados_venda[3]:<20}")

    except FileNotFoundError:
        printRed("Arquivo de vendas não encontrado.")

    except Exception as e:
        printRed(f"Erro ao listar vendas: {e}")
    input("\033[32mPrecione Enter Para Sair")