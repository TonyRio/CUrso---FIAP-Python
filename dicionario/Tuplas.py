usuarios = {}
emails = ["xpto@xyz.com", "xkcd@phd.com"]
tupla = list(enumerate(emails))



for chave in range (0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o Nome "), input("Digite o nivel ")]

for chave, dado in usuarios.items():
    print("usuario ..: ", chave[0])
    print("email..: ", chave[1])
    print("Nome..: ", dado[0])
    print("nivel..: ", dado[1])