
#from random import randint
#account_number randomly generated

#2 & #3
class BankAccount():
  def __init__(self, full_name, account_number, balance=0):
    self.full_name = full_name
    self.account_number = account_number
    self.balance = balance 
#4
  def deposit(self, amount): 
    self.balance += amount
    print(f'Amount deposited: ${amount}')
    print(f'NEW ACCOUNT BALANCE: ${self.balance}\n')

  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount
      print(f'Amount Withdrawn: ${amount}')
      print(f'NEW ACCOUNT BALANCE: ${self.balance}\n')
    else:
      print("Cannot complete transaction: Insufficient funds")
      print("$10 overdraft fee has been applied to the account.\n")
      print(f'NEW ACCOUNT BALANCE: ${self.balance - 10}')

  def get_balance(self):
    print(f"Account balance: ${self.balance}\n")
    return self.balance

  def add_interest(self):
    self.balance += self.balance * 0.00083 
    print(f'Account balance after interest applied: {self.balance}')

  def print_statement(self):
    print(self.full_name)
    print(f'Account No.: {self.account_number}')
    self.get_balance()

#6
mitchellAccount = BankAccount("Mitchell", "03141592")
mitchellAccount.print_statement()
mitchellAccount.deposit(40)
#mitchellAccount.add_interest()
#mitchellAccount.print_statement()
mitchellAccount.withdraw(150)
#mitchellAccount.print_statement()
