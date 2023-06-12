# Multiple Inheritance
# Using the attributes and methods from multiple classes, when one class inherits from multiple classes,
# and is able to use attributes and methods from both classes

# Examples 1: 
# class Animal():
#     def __init__(self, sound, look):
#         .....

# class Place():
#     def __init__(self, climate, lat, lon):
#         .....

# class Mammal(Animal, Place):
#     def __init__(self, sound, look, climate, lat, lon, food)
#     Animal.__init__(self, sound, look)
#     Place.__init__(self, climate, lat, lon)
#     self.food = food 


# Examples 2

# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku
    
    def print_sku(self):
        print("The sku is {}".format(self.sku))
    
# Parent class 2
class Garment():
    def __init__(self, section , type):
        self.section = section
        self.type = type
    
    def print_garment(self):
        print("The garment is in section {}, and {}".format(self.section, self.type))

# Child class
class Shirts(Item, Garment):
    # In this initiallization or constructor method, indentify all atributes from both parent classes
    # in addition to the attributes that are specific to the child class
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)
    
    def print_shirts(self):
        print("{} {} on sale !!".format(self.color, self.name))

Blouse = Shirts("0001", 43, "Tops", "Formal Blouse", "Blue")

# Then calling each parent methods
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirts()

