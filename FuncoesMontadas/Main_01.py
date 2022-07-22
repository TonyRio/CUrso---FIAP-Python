usuarios={}
usuarios={"Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }
usuarios["Florinda"]=["Florinda Flores", "26/11/2020", "Recep_01"]
print(usuarios)
for dados in (usuarios):
    print(dados  +"  **")
print("dados", usuarios.get(input("quem da Chave quer achar ? : ")))