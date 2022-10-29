import random


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.statiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.statiety >= 100:
                self.statiety = 100
                return
            self.statiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.statiety -= 4

    def shopping(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I  bought a fuel')
            self.money -= 50
            self.car.fuel += 50
        elif manage == 'food':
            print('Bought food')
            self.money -= 25
            self.home.food += 25
        elif manage == 'delicacies':
            print('You are Happy!!')
            self.gladness += 10
            self.statiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today is the {day} of {self.name}'s live"
        print(f'{day:=^50}', '\n')
        humans_indexes = self.name + "'s indexes"
        print(f'{humans_indexes:^50}', '\n')
        print(f'Money = {self.money}')
        print(f'Statiety = {self.statiety}')
        print(f'Gladness = {self.gladness}')
        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}', '\n')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')
        car_indexes = f"{self.car.brand} car indexes"
        print(f'{car_indexes:^50}', '\n')
        print(f'Fuel = {self.car.fuel}')
        print(f'Strenght = {self.car.strenght}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        if self.statiety < 0:
            print('Dead......')
            return False
        if self.money < 0:
            print('Bankrupt')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return
        if self.home == None:
            print('Settled in the Home')
            self.get_home()
        if self.car == None:
            self.get_car()
            print(f'I want a car {self.car.brand}')
        if self.job == None:
            self.get_job()
            print(f"I do't have a job, I'm going to work as {self.job.job} salary {self.job.salary}")
        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.statiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\n So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strenght']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1
            return True
        else:
            print('the car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['gladness_less']


brand_of_car = {'BMW': {'fuel': 100, 'strenght': 100, 'consumption': 6},
                'Lada': {'fuel': 50, 'strenght': 40, 'consumption': 10},
                'Volvo': {'fuel': 70, 'strenght': 150, 'consumption': 8},
                'Ferrari': {'fuel': 80, 'strenght': 120, 'consumption': 14}}
job_list = {'Java developer': {'salary': 50, 'gladness_less': 10},
            'Python developer': {'salary': 40, 'gladness_less': 15},
            'C++ developer': {'salary': 55, 'gladness_less': 25},
            'Java developer': {'salary': 70, 'gladness_less': 1}}

nick = Human(name='Nick')
for day in range(1, 8):
    if nick.live(day) == False:
        break
