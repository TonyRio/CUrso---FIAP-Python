import socket

resp="S"
while(resp=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    if ip!= None:
        print("O IP referente à url informada é: ", ip)
    else:
        print("## ERRO ## - URL não cadastrada! ")

    resp=input("Digite <s> para continuar: ").upper()