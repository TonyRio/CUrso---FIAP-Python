import socket

print(f"A Porta de dominio disponivel é :", (socket.getservbyname("domain")))
print(f"A Porta de HTTP disponivel é    :",(socket.getservbyname("http")))
print(f"A Porta de FTP disponivel é     :",(socket.getservbyname("ftp")))

# resp="S"
# while(resp=="S"):
#     url=input("Digite uma url: ")
#     ip=socket.gethostbyname(url)
#     if ip!= None:
#         print("O IP referente à url informada é: ", ip)
#     else:
#         print("## ERRO ## - URL não cadastrada! ")
#
#     resp=input("Digite <s> para continuar: ").upper()