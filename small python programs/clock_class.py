'''
Create class Clock and it's subclass AlarmClock. Test clocks in main. There has to be ticking and alarming methods...
'''

class Clock:

    def __init__(self, clock_type, material, color, price):
        self.clock_type = clock_type #wristwatch, wall clock, grandfather clock, radio, cockoo clock, ...
        self.material = material #wood, plastic, silver, gold ....
        self.color = color
        self.price = price

    def getAll(self):
        clock_info = f"CLOCK INFO:\nClock type: {self.clock_type} \nMaterial: {self.material} \nColor: {self.color} \nPrice: {self.price}€"
        return clock_info
    
    def getType(self):
        return self.clock_type
    
    def getMaterial(self):
        return self.material
    
    def getColor(self):
        return self.color
    
    def getPrice(self):
        return self.price
    
    def setType(self, clock_type):
        self.clock_type = clock_type

    def setMaterial(self, material):
        self.material = material

    def setColor(self, color):
        self.color = color

    def setPrice(self, price):
        self.price = price

    def ticking(self):
        print("tic, tac, tic, tac.....")

class AlarmClock(Clock):
    
    def __init__(self, manufacturer, origin):
        self.manufacturer = manufacturer
        self.origin = origin

    def getAlarmInfo(self):
        info = f"ALARM INFO:\nManufacturer: {self.manufacturer} \nOrigin: {self.origin}"
        return info

    def getManufacturer(self):
        return self.manufacturer
    
    def getRingTone(self):
        return self.origin
    
    def setManufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def setRingTone(self, origin):
        self.origin = origin

    def alarming(self):
        print("RRRRRRRRIIIIIIINNGGGGGGGGG!!!!!!!!!!!")

my_clock = Clock("wall clock", "plastic", "blue", 14.99)
my_clock.ticking()
print(my_clock.getAll())

my_alarm = AlarmClock("Gallet & Co.", "Swiss")
print(my_alarm.getAlarmInfo())
my_alarm.alarming()
my_alarm.setPrice(900)
print(f"Price: {my_alarm.getPrice()}")
my_alarm.setMaterial("steel")
my_alarm.setColor("black")
print(f"Material: {my_alarm.getMaterial()}, \nColor: {my_alarm.getColor()}")
