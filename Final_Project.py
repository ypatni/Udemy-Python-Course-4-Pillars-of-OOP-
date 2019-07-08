from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):
    def __init__(self):
        self.SavingsAccount = {}

    def createAccount(self, name, initialdeposit):
        self.accountnumber = randint(10000, 99999)
        # [key][0] = name, [key][1] = initialdeposit
        self.SavingsAccount[self.accountnumber] = [name, initialdeposit]
        print("Account Number", self.accountnumber)

    def authenticate(self, name, accountnumber):
        if accountnumber in self.SavingsAccount.keys():
            if self.SavingsAccount[accountnumber][0] == name:
                print("Authentification successful")
                self.accountnumber = accountnumber
                return True
            else:
                print("Failure")
                return False

    def withdraw(self, withdrawalamount):
        if withdrawalamount > self.SavingsAccount[self.accountnumber][1]:
            print("Insufficicent Balance")

        else:
            self.SavingsAccount[self.accountnumber][1] -= withdrawalamount
            self.displayBalance

    def deposit(self, depositamount):
        self.SavingsAccount[self.accountnumber][1] += depositamount
        self.displayBalance

    def displayBalance(self):
        print("Balance =", self.SavingsAccount[self.accountnumber][1])


savings_account = SavingsAccount()
while True:
    print("enter 1 to create new account")
    print("Enter 2 to enter existing account")
    print("Enter 3 to leave")
    user_choice = int(input())
    if user_choice is 1:
        print("Enter Name")
        name = input()
        print("Enter Initial Deposit")
        deposit = int(input())
        savings_account.createAccount(name, deposit)
    elif user_choice is 2:
        print("Enter Name")
        name = input()
        print("Enter Account Number")
        account = int(input())
        authenticationstatus = savings_account.authenticate(name, account)
        if authenticationstatus is True:
            while True:
                print("Enter 1 to Withdraw")
                print("Enter 2 to Deposit")
                print("Enter 3 to Display Balance")
                print("Enter 4 to go back")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter Withdrawal Amount")
                    withdraw = int(input())
                    savings_account.withdraw(withdraw)
                elif userChoice is 2:
                    print("Enter Deposit Amount")
                    deposit = int(input())
                    savings_account.deposit(deposit)
                elif userChoice is 3:
                    savings_account.displayBalance()
                elif userChoice is 4:
                    break
    elif user_choice is 3:
        quit()
