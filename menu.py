from inclusao import incluir
from alteracao import alterar
from exclusao import excluir
from visualizacao import listar
import os

bd = {}
def menu():
    while True:
        os.system('cls')
        print('*' * 30)
        print("1 - Inclusão de Produtos")
        print("2 - Alteração de Nome do Produto")
        print("3 - Exclusão de Produtos")
        print("4 - Listagem de Todos os Produtos")
        print('*' * 30)
        print("0 - Sair")
        
        op = input("Digite um número de uma das opções acima: ")
        
        if (op=='1'):
            incluir(bd)
        elif (op=='2'):
            alterar(bd)
        elif (op=='3'):
            excluir(bd)
        elif (op=='4'):
            listar(bd)
        elif (op=='0'):
            break
        else:
            print("Opção Inválida!!!")
    # Fim do while
    print("Fim do Programa!")