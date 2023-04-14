'''
Take a look at python.org site. Array methods are presented here: https://docs.python.org/3/tutorial/datastructures.html

Give your own examples of using those metods.
'''

import random

shopping_list = []

print("Your fridge is empty and you need to go to a grocery store. Add items to shopping list. When your done, write END.", end='')

def add_to_list():
    while True:
        buy_this = input("Add item to shopping list:")
        shopping_list.append(buy_this)
        if buy_this.lower() == "end":
            shopping_list.remove('end')
            break

add_to_list()

while len(shopping_list) == 0:
    print("\r\nYou must add something to the list!")
    add_to_list()

print("\r\nYour shopping list looks like this:")
print(f"{shopping_list}\r\n")

user_choise1 = input("Are you sure there's all you need? Type ADD if you want to add something to your list.\r\n").lower()

if user_choise1 == "add":
    add_to_list()

print("\nLooks like the list includes all you need and now you're ready to go! But wait a sec.\r\n")

print("It's nice to have things organized so let's edit your list a little. I'll organize the list alphabetically for you.")

shopping_list.sort()
print(f"{shopping_list}\r\n")
print("That's much better! Let's go to the store!\r\n")

print("While you are walking to the store, your phone beeps for a message. It's your cat and he tells that we're running out of cat food! Of course that is now your priority number one so it should be the first item in your shopping list.\r\n")

shopping_list.insert(0, "cat food")
print(f"{shopping_list}\r\n")

def buy_catfood():
    for i in range(catfood):
        shopping_list.insert(1,'cat food')

while True:
    catfood = int(input("It's better to buy more than just one can of cat food, otherwise your cat will be very disappointed. So how many cans you're going to buy moreover?\n"))

    if catfood < 2:
        print("I don't think that's enough! Buy some more.\r\n")
        continue
    elif catfood > 50:
        print("We can't afford to buy that much.")
        continue
    else:
        buy_catfood()
        break

print("\nLet's make sure that it is correct. How many cans of catfood do we have in our list?\r\n")
print(shopping_list)

cans = shopping_list.count('cat food')
print(f"It seems correct! There are {cans} cans of catfood.\r\n")

print("Whoah. I feel like all that cat food is attacking me. Maybe it's better to reverse the list. I'm sure you don'f forget to buy cat food.\r\n")

shopping_list.reverse()
print(f"{shopping_list}\r\n")
print("Much better!\r\n")

print("While walking to the store you remember that you promised to do the grocery shoppings to your mom too!\r\n")

shopping_list_for_mom = []
print("What groceries your mom needs from the store? When your finnished, type END.\r\n")

def shop_for_mom():
    while True:
        for_mom = input("For mom:")
        shopping_list_for_mom.append(for_mom)
        if for_mom.lower() == "end":
            shopping_list_for_mom.remove('end')
            break

shop_for_mom()

while len(shopping_list_for_mom) == 0:
    print("You must add something to the list!\r\n")
    shop_for_mom()

print("There is your moms shopping list:\r\n")
print(f"{shopping_list_for_mom}\r\n")

print("Let's save paper and put these two together! But first it's better to make a copy from your moms shopping list, so you remember what grocesies you should give to her.\r\n")

shopping_list_copy = shopping_list_for_mom.copy()
shopping_list.extend(shopping_list_for_mom)
shopping_list.sort()
shopping_list.reverse()

print(f"So here is the updated and reorganized shopping list: {shopping_list}\r\n")

print("Finally you have reached the grocery store. First let's collect all the cat food and remove them from our list.\r\n")

cat_food = "cat food"

while cat_food in shopping_list:
    shopping_list.remove('cat food')

print("Let's take a look to our list again:\r\n")
print(shopping_list)

item_found = random.choice(shopping_list)

print(f"\r\nHey look! There's {item_found}! Wasn't that in your shopping list?\r\n")

item_index = shopping_list.index(item_found)
print(shopping_list)

print(f"\r\nOh that is number {item_index + 1} in our list!")
print(f"Now that {item_found} is found we can remove it from the list.\r\n")

shopping_list.pop(item_index)

print("So here is our list now:\r\n")
print(shopping_list)

print("\r\n.....\r\n.....\r\n.....\r\n.....\r\n")

print("You have walked through the store several times collecting items from your shopping list. Finally you have found them all! Let's clear the shopping list.\r\n")

shopping_list.clear()

print(f"{shopping_list} So that's what an empty list looks like! What a relief!")
print("But wait a sec! You can't remember which groceries was supposed to give to mom!")
print("Luckily there was this copu of moms shopping list!")
print(shopping_list_copy)