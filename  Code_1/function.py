amount = 0


def Income():
    print("Enter the income: ")
    income = input()
    amount = amount + income
    print("Press any key")
    getch()
    Menu()


def Expense():
    print("Enter the amount spend: ")
    spend = input()
    amount = amount - spend
    print("Press any key")
    getch()
    Menu()


def Balance():
    print(amount)
    print("Press any key")
    getch()
    Menu()


def Decide_Reset():
    print("This command will erase all data. Do you want to continue ?")
    print("\nPress 0 to return\nPress 1 to reset data")
    reset = input()
    if(reset == 0):
        one = Menu()
    elif(reset == 1):
        amount = 0
    else:
        print("Enter a valid option") Menu()


def Exit():
    print("Are you sure you want to quit ?")
    print("\nPress 0 to return to menu\nPress 1 to quit")
    exit = input()
    if(exit == 0):
        Menu()
    elif(exit == 1):
        exit(0)
    else:
        print("Enter a valid option.") Menu()


def Menu():
    print("Select an Option : \n1.Income\n2.Expenditure")
    print("\n3.Balance\n4.Reset Data\n5.Exit\n")
    option = input()
    if(option == 1):
        Expense()
    elif(option == 2):
        Income()
    elif(option == 3):
        Balance()
    elif(option == 4):
        Decide_Reset()
    elif(option == 5):
        Exit()
    else:
        print("Enter a valid option.") Menu()
Menu()
