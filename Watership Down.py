import random
class Animal:
    def __init__(self, age, frailty, gender):
        self.age = age
        self.frailty = frailty
        self.gender = gender
class Rabbits(Animal):
    RabbitHealth = 100
    def Days(self):
        self.age = self.age + 1
        print(self.age)
        if self.age > 366:
            self.frailty = self.frailty+ 1
        else:
            self.frailty = self.frailty + 0
        if self.frailty == 50:
            Disease = random.randint(1,5)
            if Disease == 1 or Disease == 3 or Disease == 5:
                RabbitHealth = 0
                DeadRabbits.append(Rabbits)
            elif Disease == 2 or Disease == 4:
                RabbitHealth = 80
        self.Food()

    def Food(self):
        RabbitFood = 150
        #RabbitFood = input("Please Enter the amount of Food: ")
        DaysWithoutFood = 0
        if Animal.frailty < 50:
            RabbitFood = random.randint(50,100)
        elif Animal.frailty < 50:
            RabbitFood = random.randint(0, 20)
            if RabbitFood == 0:
                Animal.frailty = Animal.frailty + 1
                DaysWithoutFood = DaysWithoutFood + 1
            elif DaysWithoutFood == 3:
                RabbitHealth = 0
                DeadRabbits.append(Rabbits)
            elif DaysWithoutFood == 1 or DaysWithoutFood == 2:
                Animal.frailty = Animal.frailty + 1

    def WeeklyReport(self):
        print(AliveRabbits)
        print(RabbitFood)
        print(DeadRabbits)
        print(PregnantRabbits)
        print(BabyRabbits)

    def Breeding(self):
        if Animal.frailty > 50:
            Breed = random.randint(75,100)
            if Breed >= 80:
                Pregnancy = random.randint(90,100)
                PregnantRabbits.append(Rabbits)
                if Animal.age == Animal.age + 30:
                    BabyRabbits = random.randint(4,12)
                    BabyRabbits.apppend(Rabbits)
                else:
                    DeadRabbits.append(Rabbits)
            else:
                RabbitHealth = 0
        else:
            pass
BabyRabbits = []
AliveRabbits = [Rabbits(1,0,"M"), Rabbits(1,0,"F")]
DeadRabbits = []
PregnantRabbits = []
AliveRabbits[0].Days()
#Rabbits.WeeklyReport()

for rabbit in AliveRabbits:
    rabbit.Days()









