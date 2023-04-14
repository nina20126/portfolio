'''
Bird has features name and amount of eggs. Amount of eggs has to be between 1 and 10.

Migratory has special features: there is attribute named country that is the destination country and month when the migration mainly occurs. 

Country name has to begin with a cap and its length has to be between 5 to 20. Month has to be between 1 and 12.
'''
class Bird:

    def __init__(self, name, eggs):
        self.name = name
        if eggs >= 1 and eggs <= 10:
            self.eggs = eggs
        else: 
            self.eggs = "Egg amount not correct"

    def getInfo(self):
        bird_info = f"Name: {self.name} \nEggs: {self.eggs}"
        return bird_info
    
    def getBirdName(self):
        return self.name
    
    def getEggs(self):
        return self.eggs

    def setBirdName(self, name):
        self.name = name

    def setEggs(self, eggs):
        self.eggs = eggs


class Migratory:

    def __init__(self, country, month):
        if len(country) >= 5 and len(country) <= 20 and country[0].isupper() == True:
            self.country = country
        else: 
            self.country = "Incorrect country"
        if month >= 1 and month <= 12:
            self.month = month
        else:
            self.month = "Month has to be between 1 and 12"

    def getInfoMigratory(self):
        migratory_info = f"Country: {self.country} \nMonth: {self.month}"
        return migratory_info

    def getCountry(self):
        return self.country
    
    def getMonth(self):
        return self.month
    
    def setCountry(self, country):
        self.country = country

    def setMonth(self, month):
        self.month = month

eggs1 = 11
eggs2 = 5

country1 = "test"
country2 = "Test"
country3 = "Spain"
country4 = "Hsjlkhjdfjkhsdfjksdhdjfksjdhflk"
country5 = "Kshrjghrulopahdgtreo"

month1 = 0
month2 = 6
month3 = 22

bird = Bird("Kalle", eggs1)
print(bird.getInfo())

bird = Bird("Matti", eggs2)
print(bird.getInfo())

bird_mig = Migratory(country1, month1)
print(bird_mig.getInfoMigratory())

bird_mig = Migratory(country2, month2)
print(bird_mig.getInfoMigratory())

bird_mig = Migratory(country3, month3)
print(bird_mig.getInfoMigratory())

bird_mig = Migratory(country4, month3)
print(bird_mig.getInfoMigratory())

bird_mig = Migratory(country5, month2)
print(bird_mig.getInfoMigratory())


