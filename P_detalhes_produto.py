def detalhes_produto():
    try:
        codigo_produto = input("Digite o código do produto: ")
        
        produto_info = None
        quantidade_comprada_total = 0
        quantidade_vendida_total = 0
        valor_total_compra = 0
        valor_total_venda = 0
        
        try:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            for produto in produtos:
                dados = produto.strip().split(";")
                if dados[0] == codigo_produto:
                    produto_info = {
                        'nome': dados[1],
                        'descricao': dados[2],
                        'preco_compra': float(dados[3]),
                        'preco_venda': float(dados[4]),
                        'estoque': int(dados[5])
                    }
                    break
            
            if produto_info:
                print(f"\nDetalhes do Produto")
                print(f"Nome: {produto_info['nome']}")
                print(f"Descrição: {produto_info['descricao']}")
                print(f"Preço de Compra: {produto_info['preco_compra']:.2f}")
                print(f"Preço de Venda: {produto_info['preco_venda']:.2f}")
                print(f"Estoque Atual: {produto_info['estoque']}")
                
                movimentos_encontrados = False
                print(f"\n{'Código Compra':<15}{'Data':<12}{'Quantidade Comprada':<20}")
                
                try:
                    with open("compras.txt", "r", encoding="utf8") as arquivo:
                        compras = arquivo.readlines()
                    
                    for compra in compras:
                        dados_compra = compra.strip().split(";")
                        if dados_compra[2] == codigo_produto:
                            movimentos_encontrados = True
                            quantidade_comprada_total += int(dados_compra[3])
                            valor_total_compra += produto_info['preco_compra'] * int(dados_compra[3])
                            print(f"{dados_compra[0]:<15}{dados_compra[1]:<12}{dados_compra[3]:<20}")
                except FileNotFoundError:
                    pass
                
                print(f"\n{'Código Venda':<15}{'Data':<12}{'Quantidade Vendida':<20}")
                
                try:
                    with open("vendas.txt", "r", encoding="utf8") as arquivo:
                        vendas = arquivo.readlines()
                    
                    for venda in vendas:
                        dados_venda = venda.strip().split(";")
                        if dados_venda[2] == codigo_produto:
                            movimentos_encontrados = True
                            quantidade_vendida_total += int(dados_venda[3])
                            valor_total_venda += produto_info['preco_venda'] * int(dados_venda[3])
                            print(f"{dados_venda[0]:<15}{dados_venda[1]:<12}{dados_venda[3]:<20}")
                except FileNotFoundError:
                    pass
                
                if not movimentos_encontrados:
                    print("Não tem movimentações.")
                
                lucro_total = valor_total_venda - valor_total_compra
                
                print(f"\nQuantidade Total Comprada: {quantidade_comprada_total}")
                print(f"Quantidade Total Vendida: {quantidade_vendida_total}")
                print(f"Valor Total Investido: {valor_total_compra:.2f}")
                print(f"Valor Total Arrecadado: {valor_total_venda:.2f}")
                print(f"Lucro Obtido: {lucro_total:.2f}")
            else:
                print("Produto não encontrado.")
        except FileNotFoundError:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao mostrar detalhes do produto: {e}")
    input("\033[32mPrecione Enter para Sair")