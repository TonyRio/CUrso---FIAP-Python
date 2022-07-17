nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
if idade>=65:
 prioridade="SIM"
else:
 prioridade = "NÃO"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)
print("***** FIM *****")