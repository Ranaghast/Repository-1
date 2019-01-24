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
        print("Days: ",self.age)
        if self.age > 366:
            self.frailty = self.frailty+ 1
        else:
            self.frailty = self.frailty + 0
        if self.frailty == 50:
            Disease = random.randint(1,5)
            if Disease == 1 or Disease == 3 or Disease == 5:
                RabbitHealth = 0
                DeadRabbits.append(AliveRabbits[i])
            elif Disease == 2 or Disease == 4:
                RabbitHealth = 80
        self.Food()

    def Food(self):
        RabbitFoodFound = random.randint(1, 200)
        print("Rabbit Food: ",RabbitFoodFound)
        #RabbitFood = input("Please Enter the amount of Food: ")
        DaysWithoutFood = 0
        if self.frailty < 50:
            RabbitFood = random.randint(50,100)
        elif self.frailty < 50:
            RabbitFood = random.randint(0, 20)
            if RabbitFood == 0:
                self.frailty = self.frailty + 1
                DaysWithoutFood = DaysWithoutFood + 1
                print("Days without food: ", DaysWithoutFood)
            elif DaysWithoutFood == 3:
                print("Days without food: ", DaysWithoutFood)
                RabbitHealth = 0
                print("Rabbit Health", RabbitHealth)
                DeadRabbits.append(AliveRabbits[i])
            elif DaysWithoutFood == 1 or DaysWithoutFood == 2:
                Animal.frailty = Animal.frailty + 1
        self.Breeding()


    def Breeding(self):
        if self.frailty > 50:
            Breed = random.randint(75,100)
            if Breed >= 80:
                Pregnancy = random.randint(90,100)
                PregnantRabbits.append(Rabbits)
                if self.age == self.age + 30:
                    BabyRabbits = random.randint(4,12)
                    BabyRabbits.apppend(AliveRabbits[i])
                else:
                    DeadRabbits.append(AliveRabbits[i])
            else:
                RabbitHealth = 0
        else:
            pass
        rabbit.Days()
        #print(AliveRabbits)
        #print(DeadRabbits)
        #print(PregnantRabbits)
        #print(BabyRabbits)

BabyRabbits = []
AliveRabbits = [Rabbits(0,0,"M"), Rabbits(0,5,"F"), Rabbits(0,2,"M"), Rabbits(0,49,"M"), Rabbits(0,20,"F"), Rabbits(0,0,"F")]
DeadRabbits = []
PregnantRabbits = []
i = 0
for rabbit in AliveRabbits:
    rabbit.Days()
    i = i + 1











