import P_removerRegistro

def remover_produto():
    try:
        codigo = input("Digite o código do produto a ser removido: ")
        
        with open("produtos.txt", "r", encoding="utf8") as arquivo:
            produtos = arquivo.readlines()
        
        with open("produtos.txt", "w", encoding="utf8") as arquivo:
            produto_encontrado = False
            for produto in produtos:
                if not produto.startswith(codigo + ";"):
                    arquivo.write(produto)
                else:
                    produto_encontrado = True
        
        if produto_encontrado:
            P_removerRegistro.remover_registros_associados(codigo)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao remover produto: {e}")