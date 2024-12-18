class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"₹{amount} deposited successfully!"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"₹{amount} withdrawn successfully!"
        elif amount > self.balance:
            return "Insufficient balance."
        return "Invalid withdrawal amount."

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            return f"₹{amount} transferred successfully to Account {target_account.account_number}!"
        elif amount > self.balance:
            return "Insufficient balance."
        return "Invalid transfer amount."

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return "PIN changed successfully!"
        return "Incorrect old PIN."

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def run(self):
        print("Welcome to Varacha Bank ATM!")
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Funds")
            print("5. Change PIN")
            print("6. Exit")
            
            choice = input("Choose an option: ")

            if choice == "6":
                print("Thank you for using Varcha Bank ATM!")
                break
            elif choice in {"1", "2", "3", "4", "5"}:
                account_number = input("Enter your account number: ")
                pin = input("Enter your PIN: ")
                account = self.authenticate(account_number, pin)

                if account:
                    if choice == "1":
                        print(f"Your balance is: ₹{account.check_balance()}")
                    elif choice == "2":
                        amount = float(input("Enter amount to deposit: "))
                        print(account.deposit(amount))
                    elif choice == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        print(account.withdraw(amount))
                    elif choice == "4":
                        target_account_number = input("Enter target account number: ")
                        target_account = self.accounts.get(target_account_number)
                        if target_account:
                            amount = float(input("Enter amount to transfer: "))
                            print(account.transfer(amount, target_account))
                        else:
                            print("Target account not found.")
                    elif choice == "5":
                        old_pin = input("Enter your old PIN: ")
                        new_pin = input("Enter your new PIN: ")
                        print(account.change_pin(old_pin, new_pin))
                else:
                    print("Authentication failed. Please try again.")
            else:
                print("Invalid option. Please try again.")

#demo-data
atm = ATM()
atm.add_account(Account("123456", "1234", 5000))
atm.add_account(Account("654321", "4321", 3000))
atm.add_account(Account("100100", "0000", 3000))
atm.run()

#Developer "Harsh-Hirpara"
