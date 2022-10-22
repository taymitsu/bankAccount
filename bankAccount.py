

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
    print(f'Amount Withdrawn: ${amount}')
    print(f'NEW ACCOUNT BALANCE: ${self.balance}\n')

  def get_balance(self, balance):
    print(f"Account balance: ${self.balance}\n")
    return self.balance

  def add_interest(self):
    balance+= * decimal 
    
  def print_statement(self):
    print(self.full_name)
    print(f'Account No.: {}')
    print.get_balance()