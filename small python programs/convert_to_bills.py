'''
Convert euros to 5, 10, 20, 50, 100, 200, 500 euros bill
'''

euros_to_convert = int(input("Euros:"))

user_input = euros_to_convert

total_500 = 0
total_200 = 0
total_100 = 0
total_50 = 0
total_20 = 0
total_10 = 0
total_5 = 0

while (euros_to_convert >= 500):
    total_500 = total_500 + 1
    euros_to_convert = euros_to_convert - 500
if total_500 > 0:
    print(f"{euros_to_convert} euros left to convert. Amount of 500€ bills: {total_500}")

while (euros_to_convert >= 200):
    total_200 = total_200 + 1
    euros_to_convert = euros_to_convert - 200
if total_200 > 0:
    print(f"{euros_to_convert} euros left to convert. Amount of 200€ bills: {total_200}")

while (euros_to_convert >= 100):
    total_100 = total_100 + 1
    euros_to_convert = euros_to_convert - 100
if total_100 > 0:
    print(f"{euros_to_convert} euros left to convert. Amount of 100€ bills: {total_100}")

while (euros_to_convert >= 50):
    total_50 = total_50 + 1
    euros_to_convert = euros_to_convert - 50
if total_50 > 0:
    print(f"{euros_to_convert} euros left to convert. Amount of 50€ bills: {total_50}")

while (euros_to_convert >= 20):
    total_20 = total_20 + 1
    euros_to_convert = euros_to_convert - 20
if total_20 > 0:
    print(f"{euros_to_convert} euros left to convert. Amount of 20€ bills: {total_20}")

while (euros_to_convert >= 10):
    total_10 = total_10 + 1
    euros_to_convert = euros_to_convert - 10
if total_10 > 0:
    print(f"{euros_to_convert} euros left to convert. Amount of 10€ bills: {total_10}")

while (euros_to_convert >= 5):
    total_5 = total_5 + 1
    euros_to_convert = euros_to_convert - 5
if total_5 > 0:
    print(f"{euros_to_convert} euros left to convert. Amount of 5€ bills: {total_5}")

bills = (total_500 * 500) + (total_200 * 200) + (total_100 * 100) + (total_50 * 50) + (total_20 * 20) + (total_10 * 10) + (total_5 * 5) 

coins = user_input - bills
print(f"Coins left: {coins} €")


# TEACHERS EXAMPLE

money = int(input('Enter amount of euros you have: '))
# first check amount of 500 bills
bill_500 = money // 500
# extra_money variable is the money left after we have taken the bills out.
# example we have 900 then we get one 500 bill and extra money is 400 and so on.
extra_money = money % 500
bill_200 = extra_money // 200
extra_money = extra_money % 200
bill_100 = extra_money // 100
extra_money = extra_money % 100
bill_50 = extra_money // 50
extra_money = extra_money % 50
bill_20 = extra_money // 20
extra_money = extra_money % 20
bill_10 = extra_money // 10
extra_money = extra_money % 10
bill_5 = extra_money // 5

print(f'{money} in euro bills is {bill_500} 500bills, {bill_200} 200bills, {bill_100} 100bills, {bill_50} 50bills, {bill_20} 20bills, {bill_10}')