import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "TONY" and senha == "1111":
    print("Usuário logado")
else:
    print("Login Negado")