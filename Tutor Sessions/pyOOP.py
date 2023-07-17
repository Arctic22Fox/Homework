class Account:
    numcreated = 0 # Class attribute to keep track of the number of Account instances created

    def __init__(self, initialAmt):
        self.balance = initialAmt # Instance variable to store the account balance
        Account.numcreated += 1 # Increment the numcreated attribute by 1 for each new Account instance

    def deposit(self, amt):
        self.balance += amt  # Add the deposited amount to the account balance
        return

    def withdraw(self, amt):
        self.balance -= amt # Subtract the withdrawn amount from the account balance
        return

    def getbalance(self):
        return self.balance # Return the current balance of the account