def cancelar_venda():
    try:
        codigo_venda = input("Digite o código da venda a ser cancelada: ")
        produto_encontrado = False
        quantidade_cancelada = 0
        codigo_produto = None
        
        with open("vendas.txt", "r", encoding="utf8") as arquivo:
            vendas = arquivo.readlines()
        
        with open("vendas.txt", "w", encoding="utf8") as arquivo:
            for venda in vendas:
                dados = venda.strip().split(";")
                if dados[0] == codigo_venda:
                    produto_encontrado = True
                    quantidade_cancelada = int(dados[3])
                    codigo_produto = dados[2]
                else:
                    arquivo.write(venda)
        
        if produto_encontrado:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            with open("produtos.txt", "w", encoding="utf8") as arquivo:
                for produto in produtos:
                    dados = produto.strip().split(";")
                    if dados[0] == codigo_produto:
                        estoque_atual = int(dados[5])
                        novo_estoque = estoque_atual + quantidade_cancelada
                        arquivo.write(f"{codigo_produto};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{novo_estoque}\n")
                    else:
                        arquivo.write(produto)
            
            print("Venda cancelada com sucesso!")
        else:
            print("Venda não encontrada.")
    except Exception as e:
        print(f"Erro ao cancelar venda: {e}")
    input("\033[32mPrecione Enter Para Sair")