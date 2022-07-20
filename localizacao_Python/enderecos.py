from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my project 48862")
endereco = geolocator.geocode("Lins de Vasconcelos")
# resultado = Geocoder('AIzaSyB-oxiexOxi0P16LaKB5n0qIpGO9VDzuig').geocode(endereco)
print(endereco.address)
print((endereco.latitude, endereco.longitude))