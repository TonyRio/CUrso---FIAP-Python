
from Manipulacao_de_Arquivos.funcoes.funcoes import *
usuarios={}
opcao = perguntar()

while opcao=="I" or opcao == "P" or opcao =="E" or opcao== "L":
    if opcao=="I":
        inserir(usuarios)

    elif opcao=="E":
        excluir(usuarios)
    opcao= perguntar()
