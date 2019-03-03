from Person import Person

class Post:
    active = True

    def __init__ (self, name, item_desc, rating, pid, location, is_avlb):
        self.name       = name
        self.item_desc  = item_desc
        self.rating     = rating
        self.__pid      = 0
        self.__location = 0

    def obj_desc(self):
        item_desc = input("Item Description: ")
        return item_desc

    def get_user(self):
        print("Name: " + str(self.name) + "\nRating: " + str(self.rating))

#    def get_dest(self):
#        return

    def is_avlb(self):
        if ():
