from projetocoretc import *

def listar_produtos():
    try:
        produtos_encontrados = False
        produtos_existentes = False
        printBlue(f"\n{'Código':<10}{'Nome':<30}{'Total Comprado':<15}{'Total Vendido':<15}")
        
        # Verificar se o arquivo de produtos existe e está acessível
        try:
            with open("produtos.txt", "r", encoding="utf8") as arquivo:
                produtos = arquivo.readlines()
            
            if not produtos:
                printRed("Não tem movimentações.")
                return
            
            for produto in produtos:
                dados = produto.strip().split(";")
                codigo_produto = dados[0]
                nome_produto = dados[1]
                
                quantidade_comprada_total = 0
                quantidade_vendida_total = 0
                
                # Ler o arquivo de compras
                try:
                    with open("compras.txt", "r", encoding="utf8") as arquivo:
                        compras = arquivo.readlines()
                    
                    for compra in compras:
                        dados_compra = compra.strip().split(";")
                        if dados_compra[2] == codigo_produto:
                            quantidade_comprada_total += int(dados_compra[3])
                except FileNotFoundError:
                    pass
                
                # Ler o arquivo de vendas
                try:
                    with open("vendas.txt", "r", encoding="utf8") as arquivo:
                        vendas = arquivo.readlines()
                    
                    for venda in vendas:
                        dados_venda = venda.strip().split(";")
                        if dados_venda[2] == codigo_produto:
                            quantidade_vendida_total += int(dados_venda[3])
                except FileNotFoundError:
                    pass
                
                if quantidade_comprada_total > 0 or quantidade_vendida_total > 0:
                    produtos_encontrados = True
                    produtos_existentes = True
                    printBlue(f"{codigo_produto:<10}{nome_produto:<30}{quantidade_comprada_total:<15}{quantidade_vendida_total:<15}")
        
        except FileNotFoundError:
            printRed("Não tem movimentações.")
            return
        
        if not produtos_existentes:
            printRed("Não tem movimentações.")
    except Exception as e:
        printRed(f"Erro ao listar produtos: {e}")
    input("\033[32mPrecione Enter Para Sair")
    input()