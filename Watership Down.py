import random
class Animal:
    def __init__(self, age, frailty, gender):
        self.age = age
        self.frailty = frailty
        self.gender = gender
class Rabbits(Animal):
    RabbitHealth = 100
    def Days(self):
        Animal.age = Animal.age + 1
        print(Animal.age)
        if Animal.age > 366:
            Animal.frailty = Animal.frailty+ 1
        else:
            Animal.frailty = Animal.frailty + 0
        if Animal.frailty == 50:
            Disease = random.randint(1,5)
            if Disease == 1 or Disease == 3 or Disease == 5:
                RabbitHealth = 0
            elif Disease == 2 or Disease == 4:
                RabbitHealth = 80
rabbits = [Rabbits(1,0,"M"), Rabbits(1,0,"F")]



