import datetime
import json
import random


class Bank:
    # Bank represents the functionalities of the bank account like deposit, withdrawal, transfer funds, balance check
    d = {}

    def __init__(self):
        self.__current_account = None
        self.load()

    def load(self):
        # reads content from json file
        with open('Bank.json', 'r') as f:
            Bank.d = json.load(f)

    def dump(self):
        # writes into json file
        with open('Bank.json', 'w') as f:
            json.dump(Bank.d, f, indent=4)

    def login(self, account, password):
        account = str(account)
        password = str(password)
        if account in self.d:
            if (Bank.d[account]['pass'] == password):
                self.__current_account = account
            else:
                raise ValueError("Invalid password")
        else:
            raise ValueError("Bank details not found")

    def create(self, name, mobile, password):
        name = str(name)
        mobile = str(mobile)
        password = str(password)
        while True:
            account = str(random.randint(100, 1000))
            if account not in Bank.d:
                Bank.d[account] = {'name': name, 'mobile': mobile, 'bal': 0, 'pass': password, 'tran': []}
                self.__current_account = account
                print("Your Bank Number", self.__current_account)
                break
        return self.__current_account

    def withdraw(self, amount):
        if self.__current_account == None:
            raise ValueError("Bank details not found")
        if (Bank.d[self.__current_account]['bal'] < amount):
            raise ValueError("Insufficient Balance")
        else:
            Bank.d[self.__current_account]['bal'] -= amount
            Bank.d[self.__current_account]['tran'].append(
                f"{datetime.datetime.now()} withdraw {amount},balance = {Bank.d[self.__current_account]['bal']}")
        self.dump()

    def deposit(self, amount):
        if self.__current_account == None:
            raise ValueError("Bank details not found")
        Bank.d[self.__current_account]['bal'] += amount
        Bank.d[self.__current_account]['tran'].append(
            f"{datetime.datetime.now()} deposit {amount},balance = {Bank.d[self.__current_account]['bal']}")
        self.dump()

    def balance(self):
        if self.__current_account == None:
            raise ValueError("Bank details not found")
        print("Your Bank Balance is:", Bank.d[self.__current_account]['bal'])

    def transfer(self, account2, amount):
        if self.__current_account == None:
            raise ValueError("Bank details not found")
        account2 = str(account2)
        if account2 in Bank.d:
            if (Bank.d[self.__current_account]['bal'] < amount):
                raise ValueError("Insufficient Balance")
            else:
                Bank.d[self.__current_account]['bal'] -= amount
                Bank.d[account2]['bal'] += amount
                Bank.d[self.__current_account]['tran'].append(
                    f"{datetime.datetime.now()} transfer to {Bank.d[account2]['name']}, {amount},balance = {Bank.d[self.__current_account]['bal']}")
                Bank.d[account2]['tran'].append(
                    f"{datetime.datetime.now()} received from {Bank.d[self.__current_account]['name']}, {amount},balance = {Bank.d[self.__current_account]['bal']}")

                print("Funds Transferred")
        else:
            raise ValueError("Recipient not found")
        self.dump()

    def remove(self):
        if self.__current_account == None:
            raise ValueError("Bank details not found")
        Bank.d.pop(self.__current_account)
        self.__current_account = None
        self.dump()

    def transactions(self):
        if self.__current_account == None:
            raise ValueError("Bank details not found")
        k = Bank.d[self.__current_account]['tran']
        for i in reversed(k):
            print(i)


a = Bank()
b = Bank()
a.create("SAI", 98, 'a')
a.deposit(10000)
a.withdraw(500)
b_id = b.create("SAM", 87, 'b')
b.deposit(500)
a.transactions()
a.transfer(b_id, 500)
