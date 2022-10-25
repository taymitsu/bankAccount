#2
class BankAccount():
  def __init__(self, full_name, account_number, balance=0):
    self.full_name = full_name
    self.account_number = account_number
    self.balance = balance 
#4
  def deposit(self, amount): 
    self.balance += amount
    print(f'Amount deposited: ${amount}')
    print(f'NEW ACCOUNT BALANCE: {self.balance}\n')

  def withdrawal(self, amount):
    self.balance -= amount
    if self.balance < 0:
      print("Cannot complete transaction: Insufficient funds")
      print("$10 overdraft fee has been applied to the account.\n")
      self.balance -= 10
    else:
      print(f'Amount Withdrawn: ${amount}')
      print(f'NEW ACCOUNT BALANCE: ${self.balance}\n')

  def get_balance(self):
    print(f"Account balance: ${self.balance}\n")
    return self.balance

  def add_interest(self):
    self.balance += self.balance * 0.00083 

  def print_statement(self):
    print(self.full_name)
    print(f'Account No.: {self.account_number}')
    self.get_balance()

#6
mitchellAccount = BankAccount("Mitchell", "03141592")
mitchellAccount.deposit(400000)
mitchellAccount.print_statement()
mitchellAccount.add_interest()
mitchellAccount.print_statement()
mitchellAccount.withdrawal(150)
mitchellAccount.print_statement()
