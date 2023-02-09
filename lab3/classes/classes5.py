class BankAccount:
    def __init__(self,owner,balance):
        self.owner= owner
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to the account of {self.owner}.")
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from the account of {self.owner}.")
name = input()
a = int(input()) #100
dep = int(input())
wd = int(input())
wd2 = int(input())
acct1 = BankAccount(name, a)
print(acct1)

acct1.deposit(dep) #50
acct1.withdraw(wd) #75
acct1.withdraw(wd2) #500
