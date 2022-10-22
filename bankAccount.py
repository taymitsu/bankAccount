

class BankAccount():
  def __init__(self, full_name, account_number, balance=0):
    self.full_name = full_name
    self.account_number = account_number
    self.balance = balance 

  def deposit(self, amount): 
    self.amount += amount
    print(f'Amount deposited: ${amount}')
    print(f'NEW ACCOUNT BALANCE: {self.balance}\n')

  def withdrawal(self, amount):
    self.withdrawal -= amount
    if self.balance < 0:
      print("Cannot complete transaction: Insufficient funds")
      print("$10 overdraft fee has been applied to the account.\n")
      self.balance -= 10
    else:
      print(f'Amount Withdrawn: ${amount}')
      print(f'NEW ACCOUNT BALANCE: ${self.balance}\n')

  def get_balance(self, balance):
    print(f"Account balance: ${self.balance}\n")
    return self.balance

  def add_interest(self):
    self.balance += self.balance * 0.00083 

  def print_statement(self):
    print(self.full_name)
    print(f'Account No.: {self.account_number}')
    print.get_balance()