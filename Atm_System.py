"""
    **Functions**
    1. Menue
        All menue feature
    2. Create pin
        a) create pin/condition check for strong pass.
        b) greating and successful statement.
    3. Reset pin
        a) check for previous passd.
        b) taking another pass and save it.
    4. Withdrawl
        a) check for previous pass.
        b) take a amount to withdrawl.
        c) less the amount given from stored.
    5. Deposit 
        a) check for previous pass.
        b) taking amount to add in stored amount.
        c) show total amount.
    6. Check Balance
        a) check for previous pass.
        b) show the total amount.

"""

class AtmSys:

    def __init__(self):
        self.password = ""
        self.amount = 0
        self.menu()

    def c_balance(self):
        if self.password == "":
            print("Somting went Wrong. Try agin!")
            return 
        pasw = input("Enter the password: ")
        if pasw != self.password:
            print("--Wrong password--[TRY Again..]")
            return
        print("[Balance: ",self.amount,"]")
        
    def deposit(self):
        if self.password == "":
            print("Somting went Wrong. Try agin!")
            return 
        pasw = input("Enter the password: ")
        if pasw != self.password:
            print("--Wrong password--[TRY Again..]")
            return
        taker = int(input("Enter the amount here: "))
        if taker <= 0:
            print("Invalid amount!")
        else:
            self.amount += taker
            print(f"Now your total amount is {self.amount}")
        
    def withdrawal(self):
        if self.password == "":
            print("Somting went Wrong. Try agin!")
            return
        pasw = input("Enter the password: ")
        if pasw != self.password:
            print("--Wrong password--[TRY Again..]")
            return
        give = int(input("Enter the amount to withdrawl: "))
        if give > self.amount:
            print("Balance is low.")
        else:
            self.amount -= give
            print("Now your balance is ",self.amount)
        
    def createpin(self):
        print("**Password must be 6 digit and strong!**")
        self.password = input("Enter the password here: ")
        while len(self.password) != 6:
            print("Password not satisfiy above condition!")
            self.password = input("Enter the password here: ")
        print(f"Password created successfuly![xxxx{self.password[4:6]}]")
        
    def resetpin(self):
        if self.password == "":
            print("Somting went Wrong. Try agin!")
            return 
        pasw = input("Enter the password: ")
        if pasw != self.password:
            print("--Wrong password--[TRY Again..]")
            return
        new_pass = input("Enter the new password: ")
        self.password = new_pass
        print("Pin reset successfuly!")
        

    def menu(self):
        while True:
            print("="*20,"ATM","="*20)
            print("""|                                           |
|   (1) Check Balance       (2) Deposit     |
|                                           | 
|                                           |
|   (3) Withdrawl           (4) Create Pin  |
|                                           |
|                                           |
|   (5) Reset Pin           (6) Exit.       |
|                                           |""")
            print("="*45)

            try:
                opt = int(input("Enter the query: "))
                match opt:
                    case 1: self.c_balance()
                    case 2: self.deposit()
                    case 3: self.withdrawal()
                    case 4: self.createpin()
                    case 5: self.resetpin()
                    case 6: 
                        print("Thank You Sir for using us!")
                        return
            except:
                print("Invalid input!")
                    

    
ankit = AtmSys()