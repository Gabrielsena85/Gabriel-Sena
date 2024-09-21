def registrar_venda():
    try:
        codigo_produto = input("Digite o código do produto que deseja vender: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        codigo_venda = input("Digite o código da venda: ")
        data_venda = input("Digite a data da venda (dd/mm/aaaa): ")
        
        produto_encontrado = False
        estoque_suficiente = False
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            for produto in produtos:
                dados = produto.strip().split(";")
                if dados[0] == codigo_produto:
                    estoque_atual = int(dados[5])
                    if quantidade <= estoque_atual:
                        estoque_suficiente = True
                        novo_estoque = estoque_atual - quantidade
                        arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    else:
                        print("Não temos essa quantidade disponível no momento.")
                        arquivo.write(produto)  # Reescreve o produto sem alterar o estoque
                        return
                    produto_encontrado = True
                else:
                    arquivo.write(produto)
        
        if produto_encontrado and estoque_suficiente:
            with open("vendas.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(f"{codigo_venda};{data_venda};{codigo_produto};{quantidade}\n")
            print("Venda registrada com sucesso!")
        elif not produto_encontrado:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao registrar venda: {e}")
    input("\033[32mPrecione Enter Para Sair")