# Bank Account System 
class Bankaccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit Successful")
    def withdrawal(self,amount):
        if amount>self.balance:
            print("Insufficient Money")
        else:
            self.balance-=amount
            print("Withdrawal successful")  
    def show_balance(self):
        print("Account Holder :",self.name)
        print("Account Balance :",self.balance)

name=input("Enter account holder name:")
account=Bankaccount(name)
while True:
    print("1.Deposit")
    print("2.Withdrawal")
    print("3.Show Balance")
    print("4.Exit")
    choice=input("Enter your choice :")
    if choice=="1":
        amount=int(input("Enter deposit amount"))
        account.deposit(amount)
    elif choice=="2":
        amount=int(input("Enter withdrawal amount:"))
        account.withdrawal(amount)
    elif choice=="3":
        account.show_balance()
    elif choice=="4":
        print("Thank you")
        break   
    else:
        print("Invalid choice")     




