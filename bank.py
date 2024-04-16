class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit funds into the account."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw funds from the account."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Get the current account balance."""
        return self.balance

    def __str__(self):
        """String representation of the account."""
        return f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance:.2f}"

# Example usage:
account1 = BankAccount('123', 'Tanish')
print(account1.deposit(100))  # Output: 100
print(account1.withdraw(50))  # Output: 50
print(account1.get_balance())  # Output: 50
print(account1)  # Output: Account: 123, Name: John Doe, Balance: 50.00