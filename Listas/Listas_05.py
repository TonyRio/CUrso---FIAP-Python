
equipamentos = []
valores = []
continua = "S"
while continua == "S":
    equipamentos.append(input("digite o nome do equipamento:"))
    valores.append(float(input("Qual o Valor : ")))
    continua = input("Quer continuar ? : ").upper()

for indice in range(0,len(equipamentos)):
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])
    else:
        print("Equipamento nao encontrado")