import geocoder as geoc

##with open('apikey.txt') as f:
##    api_key = f.readline()
##    f.close()

api_key = 'AIzaSyAzYDaMOhBcqZkmHOz-gwmmIS0Vsd6FN8o'

#user_address = input()

def fetch_geocode(address):
    geolocation = geoc.google(address, key=api_key)
    lat = geolocation.latlng[0]
    lng = geolocation.latlng[1]
    return lat, lng

#print(user_lat, user_lng)

# use google maps API for geocoding
#g = geoc.google('730 Dover Drive', key=api_key)
#print(g.latlng)

#user_lat, user_lng = fetch_geocode(user_address)
#print( user_lat, user_lng)

