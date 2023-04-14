'''
User gives a month number and our program tells the number of days in that month.
'''

month_number = int(input("Give a number of a month (1-12):"))

match month_number:
    case 1:
        print("There are 31 days in January")
    case 2:
        print("There are 28 days in February")
    case 3:
        print("There are 31 days in March")
    case 4:
        print("There are 30 days in April")
    case 5:
        print("There are 31 days in May")
    case 6:
        print("There are 30 days in June")
    case 7:
        print("There are 31 days in July")
    case 8:
        print("There are 31 days in August")
    case 9:
        print("There are 30 days in September")
    case 10:
        print("There are 31 days in October")
    case 11:
        print("There are 30 days in November")
    case 12:
        print("There are 31 days in December")
    case _:
        print("You didn't giva a correct number.")