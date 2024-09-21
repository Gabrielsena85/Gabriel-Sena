from projetocoretc import *
def cadastrar_produto():
    try:
        printGreen("▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜")
        printGreen("▌             \033[34mCadasTrar Poduto\033[m \033[32m               ▐")
        printGreen("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")
        printGreen("▌                                             ▐")
        codigo = int(input("\033[32m▌\033[34m Digite o código do produto: "))
        nome = input("\033[32m▌\033[34m Digite o nome do produto: ")
        descricao = input("\033[32m▌\033[34m Digite a descrição do produto: ")
        preco_compra = float(input("\033[32m▌\033[34m Digite o preço de compra do produto: "))
        preco_venda = float(input("\033[32m▌\033[34m Digite o preço de venda do produto: "))
        estoque = 0  # Inicialmente o estoque é zero
        printGreen("▌                                             ▐")
        printGreen("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")
        with open("produtos.txt", "a", encoding="utf8") as arquivo:
            arquivo.write(f"{codigo};{nome};{descricao};{preco_compra};{preco_venda};{estoque}\n")
        
        printGreen("Produto cadastrado com sucesso!")
    except:
        printRed(f"Erro ao cadastrar produto: ")
    input("\033[32mPrecione Enter Para Sair")