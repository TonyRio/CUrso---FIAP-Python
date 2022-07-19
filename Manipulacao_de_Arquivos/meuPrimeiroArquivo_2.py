#arquivo = open("primeiro_arquivo.txt", "w")
#arquivo.write("meu primeiro arquivo !!")

#arquivo.close()

with open("primeiro_arquivo.txt", "r") as arquivo:
    #conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha+ "***** ")