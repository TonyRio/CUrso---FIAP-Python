import pygeocoder

endereco = '1222, Lins de Vasconcelos '
print(pygeocoder.Geocoder('AIzaSyB-oxiexOxi0P16LaKB5n0qIpGO9VDzuig').geocode(endereco).coordinates)