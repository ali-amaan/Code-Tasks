import random

class BankAccount:
    # provide a constructor to initialize the account number, account holder name, and initial balance.
    def __init__(self, account_holder_name, initial_balance=0.0):
        # account_number: A unique identifier for the account (integer).
        self.account_number = random.randint(10000000, 99999999)

        # account_holder_name: Name of the account holder (string).
        self.account_holder_name = account_holder_name

        # balance: The current balance in the account (float).
        self.balance = initial_balance

    def get_account_number(self):
        return self.account_number

    def regenerate_account_number(self, accounts):
        # keeps regenerating new account numbers until we find one that isn't used (is unique)
        while True:
            new_number = random.randint(10000000, 99999999)
            if new_number not in accounts:
                self.account_number = new_number
                break
            else:
                print("Loading your account. Kindly wait a second...")

    # deposit(amount): Add a specified amount to the balance.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount:.2f}")
        else:
            print("Invalid deposit amount.")

    # withdraw(amount): Subtract a specified amount from the balance (if sufficient funds are available).
    # ensure that the withdraw method only allows withdrawal if the balance is sufficient.
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount:.2f}")
        else:
            print("Error: Insufficient funds or invalid withdrawal amount. Try again.")

    # get_balance(): Return the current balance of the account.
    def get_balance(self):
        return self.balance

    # get_account_info(): Return a string summarizing the account details (account number, account holder name, and balance).
    def get_account_info(self):
        return (f"Account Holder: {self.account_holder_name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: {self.balance:.2f}")

