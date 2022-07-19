def perguntar():
    return input("O que deseja realizar ? \n" +
                 "<I> - Para inserir um usuario\n"+
                 "<P> - Para pesquisar um usuario\n"+
                 "<E> - Para excluir um usuario\n"+
                 "<L> - Para Listar um usuario: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o Login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a Ultima data de acesso : "),
                                                     input("qual a ultima estacao acessada : ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def excluir(dicionario):
    usuario =input("\nDigite o Nome do usuário que será excluido: ")
    for elemento, valor in dicionario.items:
        if elemento[usuario]==dicionario.items:
            dicionario.remove(elemento)
            return "Itens excluídos."