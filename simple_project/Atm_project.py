class Atm:
    a=50
    def __init__(self):
        self.pin = ""
        self.blance = 0
        self.menu()
    def menu(self):
        user_input = input('''                 
         Hello,how would you like to proceed
         1.Enter 1 to create  pin
         2.Enter 2 to deposit
         3.Enter 3 to withdraw
         4.Enter 4 to cheak blance
         5.Enter 5 to exit
         ''')
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.diposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.cheak_blance()
        else:
            print("bye")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print('Pin set successsfully')
        self.menu()

    def diposit(self):
        pins = input("Enter your pin")
        if pins == self.pin:
            amount = int(input("Enter the Amount"))
            self.blance = self.blance+amount
            print("Diposit successsfully")
        else:
            print('invalid pin')
        self.menu()

    def withdraw(self):
        pins = input("Enter your pin")
        if pins == self.pin:
            amount = int(input("Enter the  Amount"))
            if amount < self.blance:
                self.blance = self.blance-amount
                print("withdraw successsfully")
            else:
                print('insufficient funds')
        else:
            print('invalid pin')
        self.menu()

    def cheak_blance(self):
        pins = input("Enter your pin")
        if pins == self.pin:
            print(self.blance)
        else:
            print('invalid pin')
        self.menu()


sib = Atm()   
