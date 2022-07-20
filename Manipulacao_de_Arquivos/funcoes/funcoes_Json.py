def AbrirArquivo:
    with open("teste.json", "r") as arquivo:
        conteudo = arquivo.read()

def EscreverArquivo:
    with open("teste.json", "w") as arquivo:
        arquivo.write("Nunca foi tão fácil criar um arquivo.")

def InserirDados:
    with open("teste.jsonw") as arquivo:
        arquivo.write("Nunca foi tão fácil criar um arquivo.")

    with open("teste.json") as arquivo:
        arquivo.write("Continuação do texto.")