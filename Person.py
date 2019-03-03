#Tyler_Oviatt


class Person:#My class for the Name/Rate/Phone
#Constructor
    def __init__(self, name, rating, phone):
        self.name       = name
        self.rating     = rating
        self.phone      = phone

#Mutator
    def set_name(self, name):
        self.name       = name


    def set_rating(self, rating):
       self.rating    = rating

    def up_rate(self):
        self.rating += 1

    def down_rate(self):
        self.rating -= 1


    def set_phone(self, phone):
        self.phone     = phone

#Accessor

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_phone(self):
        return self.phone

#Test funcion 
#this allows us to test for a single user 

rating = 0

name    = input('What is your name:')
phone   = input('Enter your phone:')
print('Name:', name, '', 'Phone:', phone, '' 'User rating:', rating)

rating  = input ('/1 is yes, 0 is no /Do you want to up vote?:')

if rating == 1:
    rating.up_rate
elif rating == 0:
    rating.down_rate

print('Name:', name, '', 'Phone:', phone, '' 'User rating:', rating)


##this was a test for the person class

#Steve = Person(name, phone)

#print("Rating: ", Steve.get_rating())

#Steve.up_rate()
#print("Rating: ", Steve.get_rating())
