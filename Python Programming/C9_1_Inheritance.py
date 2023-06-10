class Person:
    def __init__(self, firstname, lastname, health, status):
        #initialize attributes to be used in/available for all
        #class methods in this class, and for class objects created
        #by this class

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion ==2:
            print("{} is sad right now".format(self.firstname))
    
    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health == 75:
            print("{} feels kinda tired".format(self.firstname))
        elif self.health == 50:
            print("{} feels unwell".format(self.firstname))
        elif self.health == 40:
            print("{} needs go to doctor".format(self.firstname))
        else:
            print("{} must be unconscious".format(self.firstname))
    
Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)
    

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()


# Inheritance
# Using the attributes and methods from one class in another class

# class Person ():
#     def __init__(self, firstname, lastname, health, status)
# class Enemy(Person):
#     def __init__(self, weapon, firstname, lastname, health, status)

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print(other.health)
    
    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and too weak".format(other.firstname))
    
    def steal(self, other):
        print("hahahah, {}, i have ur stuff".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy("rock", "Alex", "Wayne", 75, status = False)
Alex.hurt(Maria)
