from flask import Flask, render_template

from flask_googlemaps import GoogleMaps

from flask_googlemaps import Map

myfile = open('person.txt', 'r')
mytext = myfile.read()
myfile.close()

myList = (mytext)
s = ""

s.join(myList)

app = Flask(__name__, template_folder=".")

# you can set key as config

app.config['GOOGLEMAPS_KEY'] = "AIzaSyCjmcW8uZhOU0DoZ7kWKjx11WrlJsDsAR4"



# Initialize the extension

GoogleMaps(app)



@app.route("/")

def mapview():

    # creating a map in the view

    mymap = Map(

        identifier="view-side",

        lat=37.4419,

        lng=-122.1419,

        markers=[(37.4419, -122.1419)]

    )

    sndmap = Map(

        identifier="sndmap",

        lat=37.4419,

        lng=-122.1419,

        markers=[

          {

             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',

             'lat': 37.4419,

             'lng': -122.1419,

             'infobox': mytext

          },

          {

             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',

             'lat': 37.4300,

             'lng': -122.1400,

             'infobox': "<b>Hello World from other place</b>"

          }

        ]

    )

    return render_template('Template.html', mymap=mymap, sndmap=sndmap)



if __name__ == "__main__":

    app.run(debug=True)
