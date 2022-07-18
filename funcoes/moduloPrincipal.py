from funcoes_1 import *

minhaLista=[]
print("**** preenchendo ****")
preencherInventario(minhaLista)
print("**** Exibindo ****")
exibirInventario(minhaLista)

print("**** pesquisando ****")

localizarPorNome(minhaLista)
print("**** Alterando ****")
depreciarPorNome(minhaLista, 20)

print("**** Excluindo ****")
print(excluirPorSerial(minhaLista))
excluirPorSerial(minhaLista)
exibirInventario(minhaLista)

print("#### Resumindo ####")
resumirValores()