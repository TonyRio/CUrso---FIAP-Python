usuarios={}
opcao=input("O que deseja realizar?" +
            "\n<I> - Para Inserir um usuário"
+
            "\n<P> - Para Pesquisar um usuário"
+
            "\n<E> - Para Excluir um usuário"
+
            "\n<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        usuarios[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                       input("Digite a última data de acesso: "),
                                                       input("Qual a última estação acessada: ").upper()]
        # chave=input("Digite o login: ").upper()
        # usuarios[chave]=[input("Digite o nome: ").upper(),
        #                 input("Digite a última data de acesso: "),
        #                 input("Qual a última estação acessada: ").upper()]

    opcao = input("O que deseja realizar?"+
                  "\n<I> - Para Inserir um usuário"
 +
                  "\n<P> - Para Pesquisar um usuário"
 +
                  "\n<E> - Para Excluir um usuário"
 +
                  "\n<L> - Para Listar um usuário: ").upper()