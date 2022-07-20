from pygeocoder import Geocoder,GeocoderError,GeocoderResult

endereco ='1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('AIzaSyB-oxiexOxi0P16LaKB5n0qIpGO9VDzuig').geocode(endereco).coordinates)