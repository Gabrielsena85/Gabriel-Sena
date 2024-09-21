def comprar_produto():
    try:
        codigo_produto = input("Digite o código do produto que deseja comprar: ")
        quantidade = int(input("Digite a quantidade comprada: "))
        codigo_compra = input("Digite o código da compra: ")
        data_compra = input("Digite a data da compra (dd/mm/aaaa): ")
        
        produto_encontrado = False
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            for produto in produtos:
                dados = produto.strip().split(";")
                if dados[0] == codigo_produto:
                    estoque_atual = int(dados[5])
                    novo_estoque = estoque_atual + quantidade
                    arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    produto_encontrado = True
                else:
                    arquivo.write(produto)
        
        if produto_encontrado:
            with open("compras.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(f"{codigo_compra};{data_compra};{codigo_produto};{quantidade}\n")
            print("Compra registrada com sucesso!")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao registrar compra: {e}")
    input("\033[32mPrecione Enter Para Sair")