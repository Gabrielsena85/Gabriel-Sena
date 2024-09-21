def atualizar_produto():
    try:
        codigo = input("Digite o código do produto a ser atualizado: ")
        
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        produto_encontrado = False
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            for produto in produtos:
                if produto.startswith(codigo + ";"):
                    nome = input("Digite o novo nome do produto: ")
                    descricao = input("Digite a nova descrição do produto: ")
                    preco_compra = float(input("Digite o novo preço de compra: "))
                    preco_venda = float(input("Digite o novo preço de venda: "))
                    estoque = int(input("Digite o estoque atual do produto: "))
                    arquivo.write(f"{codigo};{nome};{descricao};{preco_compra};{preco_venda};{estoque}\n")
                    produto_encontrado = True
                else:
                    arquivo.write(produto)
        
        if produto_encontrado:
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")
    input("\033[32mPrecione Enter Para Sair")