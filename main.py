import sqlite3


class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    @staticmethod
    def initialize_database():
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()

        # Create accounts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_number TEXT PRIMARY KEY,
                pin TEXT NOT NULL,
                balance REAL DEFAULT 0
            )
        """)

        # Create transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT NOT NULL,
                transaction_type TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(account_number) REFERENCES accounts(account_number)
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def fetch_account(account_number):
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
        row = cursor.fetchone()
        conn.close()
        return Account(*row) if row else None

    def save(self):
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO accounts (account_number, pin, balance)
            VALUES (?, ?, ?)
        """, (self.account_number, self.pin, self.balance))
        conn.commit()
        conn.close()

    def log_transaction(self, transaction_type, amount):
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (account_number, transaction_type, amount)
            VALUES (?, ?, ?)
        """, (self.account_number, transaction_type, amount))
        conn.commit()
        conn.close()

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save()
            self.log_transaction("Deposit", amount)
            return f"₹{amount} deposited successfully!"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save()
            self.log_transaction("Withdrawal", amount)
            return f"₹{amount} withdrawn successfully!"
        elif amount > self.balance:
            return "Insufficient balance."
        return "Invalid withdrawal amount."

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.save()
            target_account.save()
            self.log_transaction("Transfer Out", amount)
            target_account.log_transaction("Transfer In", amount)
            return f"₹{amount} transferred successfully to Account {target_account.account_number}!"
        elif amount > self.balance:
            return "Insufficient balance."
        return "Invalid transfer amount."

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            self.save()
            return "PIN changed successfully!"
        return "Incorrect old PIN."


class ATM:
    def __init__(self):
        Account.initialize_database()

    def authenticate(self, account_number, pin):
        account = Account.fetch_account(account_number)
        if account and account.pin == pin:
            return account
        return None

    def create_account(self):
        print("\n--- Create New Account ---")
        account_number = input("Enter a new account number: ")

        # Check if the account already exists
        existing_account = Account.fetch_account(account_number)
        if existing_account:
            print("Account number already exists. Please try a different one.")
            return

        # Set PIN and validate
        pin = input("Set your 4-digit PIN: ")
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN. Please enter a 4-digit number.")
            return

        # Validate initial deposit amount
        try:
            initial_deposit = float(input("Enter initial deposit amount: "))
            if initial_deposit < 0:
                print("Deposit amount cannot be negative.")
                return
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return

        # Create and save new account to the database
        new_account = Account(account_number, pin, initial_deposit)
        new_account.save()

        print(f"Account created successfully! Your account number is {account_number}.")

    def run(self):
        print("Welcome to Varacha Bank ATM!")
        while True:
            print("\nATM Menu:")
            print("1. Create New Account")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transfer Funds")
            print("6. Change PIN")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "7":
                print("Thank you for using Varacha Bank ATM!")
                break
            elif choice == "1":
                self.create_account()
            elif choice in {"2", "3", "4", "5", "6"}:
                account_number = input("Enter your account number: ")
                pin = input("Enter your PIN: ")
                account = self.authenticate(account_number, pin)

                if account:
                    if choice == "2":
                        print(f"Your balance is: ₹{account.check_balance()}")
                    elif choice == "3":
                        amount = float(input("Enter amount to deposit: "))
                        print(account.deposit(amount))
                    elif choice == "4":
                        amount = float(input("Enter amount to withdraw: "))
                        print(account.withdraw(amount))
                    elif choice == "5":
                        target_account_number = input("Enter target account number: ")
                        target_account = Account.fetch_account(target_account_number)
                        if target_account:
                            amount = float(input("Enter amount to transfer: "))
                            print(account.transfer(amount, target_account))
                        else:
                            print("Target account not found.")
                    elif choice == "6":
                        old_pin = input("Enter your old PIN: ")
                        new_pin = input("Enter your new PIN: ")
                        print(account.change_pin(old_pin, new_pin))
                else:
                    print("Authentication failed. Please try again.")
            else:
                print("Invalid option. Please try again.")


# Initialize and run the ATM
atm = ATM()
atm.run()
