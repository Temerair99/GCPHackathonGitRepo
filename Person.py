class Person:
#Constructor
    def __init__(self, name, rating, phone):
        self.name = name
        self.rating = rating
        self.phone = phone

#Mutator
    def set_name(self, name):
        self.name = name

    def set_rating(self, rating):
        self.rating = rating

    def set_phone(self, phone):
        self.phone = phone

#Accessor

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_phone(self):
        return self.phone

