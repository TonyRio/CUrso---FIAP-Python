import json
dicionario = {
"CHAVES":["PEDRO", "12/12/2021", "ROOM1"],
  "KIKO":["TONY", "15/12/2021", "MASTER_2"],
  "FLORINDA":["JOAQUIM", "23/12/2021", "SALA2"],
  "MARCIO":["MARCIO", "21/1/2021", "SEDE2"],
  "JOAQUIM":["PEDRO", "12/12/2021", "DEP_1"]
}
with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)

# with open ("bd.json", "r") as arq_json:
#     dicionario = json.load(arq_json)
#     print(dicionario)
#     for chave, dados in dicionario.items():
#         print(chave + " --- " + str(dados))