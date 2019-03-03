from pygeocoder import Geocoder as GC

with open('apikey.txt') as f:
    api_key = f.readline()
    f.close()

geocoder = GC(api_key)
address_string = 'CSU San Bernardino'

result = geocoder.geocode(address_string)
print(result)

import geocoder as geoc

# use google maps API for geocoding
g = geoc.google('730 Dover Drive', key = api_key)
print(g.latlng)