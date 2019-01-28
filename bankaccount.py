class Account:

  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposit of {amount} accepted.")

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      print(f"Withdrawal of {amount} accepted.")
    else:
      print("Funds unavailable!")

  def __str__(self):
    return f"Account owner: {self.owner}\nAccount balance: {self.balance}"


acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(75)
print(acct1.balance)
acct1.withdraw(500)
print(acct1.balance)

