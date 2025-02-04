class Person:

    def __init__(self, fCol):
        #instance variables
        #the DATA of the PERSON
        self.favColor = fCol
        self.favAnimal = "tiger"
        self.height = 70

    def sleep(self):
        # sleeping increases your height by a small amount 
        self.height += 1

    def eat(self, food):
        print("I ate a", food)

    def walkTo(self, place):
        print("I walked to", place)

pers1 = Person("blue")
print(pers1.favColor)
pers1.sleep()
print(pers1.height)

pers2 = Person("red")
print(pers2.favColor)
print(pers2.height)