class BankAccount:
    def __init__(self):
        self._checking = 0.0
        self._savings = 0.0
    
    def set_checking(self, amount):
        if amount >= 0:
            self._checking = amount
        else:
            print("Cannot set negative balance")
    
    def set_savings(self, amount):
        if amount >= 0:
            self._savings = amount
        else:
            print("Cannot set negative balance")
    
    def get_checking(self):
        return self._checking
    
    def get_savings(self):
        return self._savings
    
    def deposit(self, account_type, amount):
        if amount > 0:
            if account_type == 'checking':
                self._checking += amount
            elif account_type == 'savings':
                self._savings += amount
    
    def withdraw(self, account_type, amount):
        if account_type == 'checking' and amount <= self._checking:
            self._checking -= amount
            print(self.get_checking())
        elif account_type == 'savings' and amount <= self._savings:
            self._savings -= amount
            print(self.get_savings())
        else:
            print("Insufficient funds")


# Initialize an object of the BankAccount class
my_account = BankAccount()
# Set values using setters
my_account.set_checking(523.48)
my_account.set_savings(386.15)
# Get values using getters
print(my_account.get_checking())
print(my_account.get_savings())
my_account.withdraw("savings",200)
my_account.withdraw("checking", 2000)

