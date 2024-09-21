from projetocoretc import *
def remover_registros_associados(codigo_produto):
    try:
        with open("compras.txt", "r", encoding="utf8") as arquivo:
            compras = arquivo.readlines()
        
        with open("compras.txt", "w", encoding="utf8") as arquivo:
            for compra in compras:
                if not compra.split(";")[2] == codigo_produto:
                    arquivo.write(compra)
        
        with open("vendas.txt", "r", encoding="utf8") as arquivo:
            vendas = arquivo.readlines()
        
        with open("vendas.txt", "w", encoding="utf8") as arquivo:
            for venda in vendas:
                if not venda.split(";")[2] == codigo_produto:
                    arquivo.write(venda)
        
    except:
        printRed(f"Erro ao remover registros associados: ")
    input("\033[32mPrecione Enter Para Sair")