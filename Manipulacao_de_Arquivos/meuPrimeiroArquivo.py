#arquivo = open("primeiro_arquivo.txt", "w")
#arquivo.write("meu primeiro arquivo !!")

#arquivo.close()

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nHakuna Matata 2 !!")