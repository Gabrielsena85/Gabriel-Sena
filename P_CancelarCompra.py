def cancelar_compra():
    try:
        codigo_compra = input("Digite o código da compra a ser cancelada: ")
        produto_encontrado = False
        quantidade_cancelada = 0
        codigo_produto = None
        
        with open("compras.txt", "r", encoding="utf8") as arquivo:
            compras = arquivo.readlines()
        
        with open("compras.txt", "w", encoding="utf8") as arquivo:
            for compra in compras:
                dados = compra.strip().split(";")
                if dados[0] == codigo_compra:
                    produto_encontrado = True
                    quantidade_cancelada = int(dados[3])
                    codigo_produto = dados[2]
                else:
                    arquivo.write(compra)
        
        if produto_encontrado:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            with open("produtos.txt", "w", encoding="utf8") as arquivo:
                for produto in produtos:
                    dados = produto.strip().split(";")
                    if dados[0] == codigo_produto:
                        estoque_atual = int(dados[5])
                        novo_estoque = estoque_atual - quantidade_cancelada
                        arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    else:
                        arquivo.write(produto)
            
            print("Compra cancelada com sucesso!")
        else:
            print("Compra não encontrada.")
    except Exception as e:
        print(f"Erro ao cancelar compra: {e}")
    input("\033[32mPrecione Enter para Sair")