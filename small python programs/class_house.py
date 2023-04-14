'''
House with 3 Rooms (note: composition)

Put min 2 attributes to all classes.

Then methods that are needed

Remember relationships between classes
'''

class House:
    def __init__(self, type, color, location, kitchen, living_room, all_bedrooms):
        self.type = type # block, terraced house, bungalow, detached house, duplex....
        self.color = color
        self.location = location
        self.kitchen = kitchen
        self.living_room = living_room
        self.all_bedrooms = all_bedrooms

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def get_location(self):
        return self.location
    
    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

    def set_location(self, location):
        self.location = location

    def house_info(self):
        house_info = f"This {self.color} house is {self.type} and it's located in {self.location}"
        return house_info
    
    def renovate_room(self, room):
        room = input("Which room you want to renovate?")
        return f"{room} is now under renovation!"
    
class Kitchen:
    def __init__(self, area, curtain_color):
        self.area = area
        self.curtain_color = curtain_color

    def get_area(self):
        return self.area
    
    def get_curtain_color(self):
        return self.curtain_color

    def set_area(self, area):
        self.area = area
    
    def set_curtain_color(self, curtain_color):
        self.curtain_color = curtain_color   
    
    def kitchen_info(self):
        kitchen_info = f"Kitchen area is {self.area} squares. There are {self.curtain_color} curtains on the window."
        return kitchen_info
    
    def fill_fridge(self):
        groceries = []
        while True:
            user_input = input("Add something to fridge (type end to finish):")
            groceries.append(user_input)
            if user_input.lower() == "end":
                groceries.remove('end')
                break
        print(f"Your fridge is now filled with: {groceries}")


class Living_room:
    def __init__(self, area, tv_on):
        self.area = area
        self.tv_on = tv_on

        if self.tv_on == True:
            self.tv_on = f"TV is on and everybody are watching new episode of Emmerdale!"
        else:
            self.tv_on = f"TV is off."

    def get_area(self):
        return self.area
    
    def get_tv(self):
        return self.tv_on

    def set_area(self, area):
        self.area = area
 
    def set_tv(self, tv_on):
        self.tv_on = tv_on
     
    def living_room_info(self):
        living_room_info = f"The living room area is {self.area} squares. {self.tv_on}"
        return living_room_info
    
    def calculate_seats(self):
        sofa = int(input("How many sofas do you have? "))
        kitchen_chair = int(input("How many chairs do you have in kitchen? "))
        balcony_chair = int(input("How many chairs do you have in balcony? "))
        floor_seats = 3
        seats = sofa * 3 + kitchen_chair + balcony_chair + floor_seats
        print(f"You can arrange a party for {seats} people!") 


class Bedroom:
    def __init__(self, area, beds_for, wallpaper):
        self.area = area
        self.beds_for = beds_for
        self.wallpaper = wallpaper

    def __repr__(self):
        return f"Area: {self.area} squares. Beds for {self.beds_for} person(s) Wallpaper: {self.wallpaper}"

    def gat_area(self):
        return self.area
    
    def get_beds(self):
        return self.beds_for
    
    def get_wallpaper(self):
        return self.wallpaper
    
    def set_area(self, area):
        self.area = area
    
    def set_beds(self, beds_for):
        self.beds_for = beds_for

    def set_wallpaper(self, wallpaper):
        self.wallpaper = wallpaper

    def bedroom_info(self):
        bedroom_info = f"Bedroom area is {self.area} squares. There are beds for {self.beds_for} people and walls are decorated with {self.wallpaper} wallpaper."
        return bedroom_info
    
    def change_wallpaper(self):
        wallpaper = input("Describe your new wallpaper: \n")
        print(f"Changing wallpaper......\nWallpaper changed! Your {wallpaper} looks great!") 
        

class Collection_Of_Bedrooms(Bedroom):
    def __init__(self):
        self.bedrooms = []

    def add_bedroom(self, new_bedroom):
        self.bedrooms.append(new_bedroom)

    def print_all_bedrooms(self):
        for i in range(0, len(self.bedrooms)):
            print(self.bedrooms[i])

    def print_one_bedroom_info(self, index):
        print(self.bedrooms[index])

    
# MAIN PROGRAM #

house1 = House("bungalow", "red", "Hattuvaara", Kitchen(12, "black"), Living_room(20, True), Collection_Of_Bedrooms())

all_bedrooms = Collection_Of_Bedrooms()

bedroom1 = Bedroom(15, 2, "flovers")
bedroom2 = Bedroom(22, 3, "Mickey Mouse")
bedroom3 = Bedroom(10, 1, "White")

house1.all_bedrooms.add_bedroom(bedroom1)
house1.all_bedrooms.add_bedroom(bedroom2)
house1.all_bedrooms.add_bedroom(bedroom3)

print("You see a interesting-looking house over the hill and decide to take a closer look at it. You walk towards the house and see a sign in the yard. 'ON SALE', it says.")
print(f"{house1.house_info()}. Why not? You decide to take a closer look.")
print(f"You walk in and first you want to see the kitchen. After all, the kitchen is the heart of a house, right?")
print(f"{house1.kitchen.kitchen_info()}")
print(f"{house1.living_room.living_room_info()}")
print("I wonder how big party I could arrange in this house, if I need a seat for everyone?")
house1.living_room.calculate_seats()
print("That sounds great! I want to buy this house!")
print(f"I'd like to change the bedroom wallpaper though! I don't like this {bedroom1.wallpaper} -wallpaper at all!")
bedroom1.change_wallpaper()
print("Let's go to the kitchen!")
house1.kitchen.fill_fridge()
print(f"What a nice {house1.kitchen.curtain_color} curtains there is in window!")
house1.kitchen.set_curtain_color("pink")
print(f"Look how it is changing color! It's {house1.kitchen.curtain_color} now!")
print("And here is all bedrooms: ")
print(house1.all_bedrooms.print_all_bedrooms())
print("Printing info from one bedroom")
print(house1.all_bedrooms.print_one_bedroom_info(1))