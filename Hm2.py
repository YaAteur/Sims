class Cat:
    height = 30

    def __init__(self, height='30 cm', name='Tusik', color='black', years='3 years', bestfood='best food for this cat is fish'):
        self.name = name
        self.height = height
        self.color = color
        self.years = years
        self.bestfood = bestfood

    def printer(self):
        print(self.height)

cat = Cat()
print(cat.name)
cat.printer()
print(cat.color)
print(cat.years)
print(cat.bestfood)
