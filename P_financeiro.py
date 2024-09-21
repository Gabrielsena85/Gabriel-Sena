def saldo_financeiro():
    try:
        total_investido = 0
        total_arrecadado = 0
        
        produtos_existentes = False
        
        try:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            for produto in produtos:
                dados = produto.strip().split(";")
                codigo_produto = dados[0]
                preco_compra = float(dados[3])
                preco_venda = float(dados[4])
                
                quantidade_comprada_total = 0
                try:
                    with open("compras.txt", "r", encoding="utf8") as arquivo:
                        compras = arquivo.readlines()
                    
                    for compra in compras:
                        dados_compra = compra.strip().split(";")
                        if dados_compra[2] == codigo_produto:
                            quantidade_comprada_total += int(dados_compra[3])
                except FileNotFoundError:
                    pass
                
                total_investido += preco_compra * quantidade_comprada_total
                
                quantidade_vendida_total = 0
                try:
                    with open("vendas.txt", "r", encoding="utf8") as arquivo:
                        vendas = arquivo.readlines()
                    
                    for venda in vendas:
                        dados_venda = venda.strip().split(";")
                        if dados_venda[2] == codigo_produto:
                            quantidade_vendida_total += int(dados_venda[3])
                except FileNotFoundError:
                    pass
                
                total_arrecadado += preco_venda * quantidade_vendida_total
            
            lucro_total = total_arrecadado - total_investido
            
            if total_investido > 0 or total_arrecadado > 0:
                print(f"\nTotal Investido: {total_investido:.2f}")
                print(f"Total Arrecadado: {total_arrecadado:.2f}")
                
                if lucro_total > 0:
                    print(f"Lucro Acumulado: {lucro_total:.2f}")
                else:
                    print(f"Lucro Acumulado: 0.00 - Não há lucro positivo.")
            else:
                print("Não tem movimentações.")
        except FileNotFoundError:
            print("Não tem movimentações.")
    except Exception as e:
        print(f"Erro ao calcular saldo financeiro: {e}")
    input("\033[32mPrecione Enter para Sair")