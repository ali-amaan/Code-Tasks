from bankaccount import BankAccount

def main():
    # Initialize variables
    # Set to store unique account numbers
    # Flags for maintaining states
    accounts = set()    
    current_account = None
    is_signed_in = False
    is_bank_open = True

    while is_bank_open:
        print("\nWelcome to the Bank!")
        if not is_signed_in:
            print("\nWhat would you like to do?")
            print("1. Create new bank account")
            print("2. Sign in to existing account") 
            print("3. Close the bank")
            choice = input("Enter choice (1/2/3): ")
            
            if choice == "1":
                # Get account details from user
                account_holder = input("Enter account holder's full name: ")
                initial_balance = float(input("Enter initial deposit amount: "))
                account = BankAccount(account_holder, initial_balance)
                accounts.add(account)
                current_account = account
                is_signed_in = True

                print("\nCongratulation! Account created and signed in. Note: Keep your account number safe to reaccess your account.")
                print(account.get_account_info())
                
            elif choice == "2":
                account_number = int(input("Enter account number: "))
                for acc in accounts:
                    if acc.account_number == account_number:
                        current_account = acc
                        is_signed_in = True
                        print("\nSigned in successfully!")
                        print(current_account.get_account_info())
                        break
                if not is_signed_in:
                    print("\nAccount not found!")
                    
            elif choice == "3":
                print("\nThank you for using our bank. Goodbye!")
                is_bank_open = False

        # The case when the user is signed in   
        else:
            print("\nWhat would you like to do?")
            print("1. Deposit money")
            print("2. Withdraw money")
            print("3. Sign out")
            choice = input("Enter choice (1/2/3): ")
            
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                current_account.deposit(amount)
                print(f"Current Balance: {current_account.get_balance():.2f}")
                
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                current_account.withdraw(amount)
                print(f"Current Balance: {current_account.get_balance():.2f}")
                
            elif choice == "3":
                print("\nSigned out successfully!")
                is_signed_in = False
                current_account = None

if __name__ == "__main__":
    main()