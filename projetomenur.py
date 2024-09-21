# from projetocoretc import *
import projetoautenticar
import projetocoretc
import os
import projetocadastra
import projetoListar_produto
import projetocomprar_produto
import P_registrar_venda
import P_detalhes_produto
import P_listar
import P_financeiro
import P_Atualizar
import P_cancelar
import P_CancelarCompra
import P_Remover
import projetobaradomenu
from projetocoretc import *
def menu_principal():
    while True:
        os.system("cls")
        printYELLOW("▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜")
        projetocoretc.printYELLOW("▌                                                                                                      ▐")
        projetocoretc.printYELLOW("▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟")

    


        
        projetobaradomenu.continuaçãoMenur()


        projetocoretc.gotoxy(6,6); projetocoretc.printBlue("1. Cadastrar Produto")
        projetocoretc.gotoxy(41,6); projetocoretc.printBlue("2. Listar Produtos")
        projetocoretc.gotoxy(77,6); projetocoretc.printBlue("3. Registrar Compra")
        projetocoretc.gotoxy(6,11); projetocoretc.printBlue("4. Registrar Venda")
        projetocoretc.gotoxy(41,11); projetocoretc.printBlue("5. Detalhes do Produto")
        projetocoretc.gotoxy(77,11); projetocoretc.printBlue("6. Listar Todas as Vendas")
        projetocoretc.gotoxy(6,16); projetocoretc.printBlue("7. Relatório Financeiro")
        projetocoretc.gotoxy(41,16); projetocoretc.printBlue("8. Atualizar Produto")
        projetocoretc.gotoxy(77,16); projetocoretc.printBlue("9. Cancelar Venda")
        projetocoretc.gotoxy(42,21); projetocoretc.printBlue("10. Cancelar Produtos")
        projetocoretc.gotoxy(6,21); projetocoretc.printBlue("11. Remover Produto")
        projetocoretc.gotoxy(76,21); projetocoretc.printRed("12. Sair")
    

        
        projetocoretc.gotoxy(4,24); opcao = input("\033[32mEscolha uma opção: ")

        if opcao == '1':
            os.system("cls")
            projetocadastra.cadastrar_produto()
        elif opcao == '2':
            os.system("cls")
            projetoListar_produto.listar_produtos()
        elif opcao == '3':
            os.system("cls")
            projetocomprar_produto.comprar_produto()
        elif opcao == '4':
            os.system("cls")
            P_registrar_venda.registrar_venda()
        elif opcao == '5':
            os.system("cls")
            P_detalhes_produto.detalhes_produto()
        elif opcao == '6':
            os.system("cls")
            P_listar.listar_todas_vendas()
        elif opcao == '7':
            os.system("cls")
            P_financeiro.saldo_financeiro()
        elif opcao == '8':
            os.system("cls")
            P_Atualizar.atualizar_produto()
        elif opcao == '9':
            os.system("cls")
            P_cancelar.cancelar_venda()
        elif opcao == '10':
            os.system("cls")
            P_CancelarCompra.cancelar_compra()
        elif opcao == '11':
            os.system("cls")
            P_Remover.remover_produto()
        elif opcao == '12':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
            
def manuais():
    if projetoautenticar.autenticar():
        menu_principal()

if __name__ == "__main__":
    manuais()
