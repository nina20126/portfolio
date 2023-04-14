'''
Account manager with menu: User can make deposits, Do withdrawal and Check the balance
'''

print("ACCOUNT MANAGER \n")

pin = "0000"
saldo = 100.00
user_quit = False
pin_try = 0

while (True and user_quit != True):
    user_pin = input("PIN: ")
    pin_try = pin_try + 1

    if user_pin == "0000":
        print("WELCOME!")
        print(f"Current saldo: {saldo} €")

        while (True):
            answer = input("Type D to make a deposit\nType W to make a withdrawal\nType S to view current saldo.\nType Q to quit the program\n")
            answer = answer.upper()

            if answer == "D":
                while(True):
                    deposit = float(input("Type deposit amount:"))
                    saldo = saldo + deposit
                    print(f"Current saldo: {saldo} €")
                    user_continue = input("Do you want to make another deposit? Type Y to continue.\n")
                    user_continue = user_continue.upper()
                    if user_continue == "Y":
                        continue
                    else:
                        break

            elif answer == "W":
                while(True):
                    withdrawal = float(input("Type withdrawal amount:"))
                    
                    if withdrawal > saldo:
                        print(f"Can't withdraw that much. Your current saldo is {saldo} €.")
                        user_continue2 = input("Continue? Y/N\n")
                        user_continue2 = user_continue2.upper()
                        if user_continue2 == "Y":
                            continue
                        else:
                            break
                    
                    saldo = saldo - withdrawal
                    print(f"Current saldo: {saldo} €")
                    user_continue = input("Do you want to make another withdrawal? Type Y to continue.\n")
                    user_continue = user_continue.upper()
                    if user_continue == "Y":
                        continue
                    else:
                        break
            
            elif answer == "S":
                print(f"Current saldo: {saldo} €")
                continue

            elif answer == "Q":
                user_quit = True
                break
                
            else:
                print("Command not recognized. Try again.")
                continue

    else:
        print("PIN is not correct!")
        
        if pin_try == 1:
            print(f"You can try 3 times: {pin_try} ")
            continue

        if pin_try == 2:
            print(f"You can try 3 times: {pin_try} ")
            continue

        if pin_try == 3:
            print("This was your third try! Bye!")
            break
