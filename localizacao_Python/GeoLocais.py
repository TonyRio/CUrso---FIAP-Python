
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

endereco = input("Digite um endereco com número e cidade.    "
                 "\nExemplo: avenida paulista, 100 São Paulo: ")
resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    # for cont in resultado:
        print("Endereço completo.: ", resultado)
        print("Bairro............: ", resultado[1])
        print("Cidade............: ", resultado[3])
        print("Regiao............: ", resultado[5])