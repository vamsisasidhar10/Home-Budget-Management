class Budget:  # The super class

    # The constructor function for initialising the variables
    def __init__(self):
        self.amount = 0

    def validity(self):  # Function to take care of the invalid cases
        print("Enter a valid option.")


class functions(Budget):
    def Income(self):  # The function to keep track of incomes
        print("Enter the income: ")
        income = int(input())  # The user inputs income amount
        self.amount = self.amount + income

    def Expense(self):  # The function to keep track of expenses
        print("Enter the amount spend: ")
        spend = int(input())
        self.amount = self.amount - spend

    def Balance(self):  # The function to display the current amount
        print("Your current balance is ", self.amount)

    def Decide_Reset(self):  # Function to reset the amount in one go
        print("This command will erase all data. Do you want to continue ?")
        print("Press 1 to continue")  # confirming reset
        reset = int(input())
        if(reset == 1):
            super().__init__()

    def Menu(self):  # Menu:option display
            print("______________Home Budget Management________________\n")
            print("Select an Option:\n1.Income\n2.Expenditure")
            print("3.Balance\n4.Reset Data")


var = 0
object_1 = functions()
object_1 . Menu()
option = int(input())
while(option > 0):
    if(var == 1):
        object_1 . Menu()
        option = int(input())
    var = 1
    if(option == 1):  # option 1 redirecting to income function
        object_1.Income()
        print("Press any key")
        input()
        continue

    elif(option == 2):  # option 2 redirecting to expense function
        object_1.Expense()
        print("Press any key")
        input()
        continue
    elif(option == 3):  # option 3 redirecting to Balance function
        object_1.Balance()
        print("Press any key")
        input()
        continue
    elif(option == 4):  # option 4 redirecting to Reset function
        object_1.Decide_Reset()
        print("Press any key")
        input()
        continue
    else:
        object_1.validity()
        print("Press any key")
        input()
