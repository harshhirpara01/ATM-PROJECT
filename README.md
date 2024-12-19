# ATM PROJECT
 ATM Service in python code 


# Author/Developer
Harsh-Hirpara

# description

Features

Account Management : 

Users can create accounts with an account number, PIN, and an initial balance.
PIN can be changed securely.


Authentication : 

Secure login using account number and PIN to access account services.


Banking Operations : 

Check Balance: View the current balance of the account.
Deposit Money: Add funds to the account.
Withdraw Money: Withdraw funds if sufficient balance is available.
Transfer Funds: Transfer money to another account within the system.


Error Handling : 

Ensures valid operations, such as rejecting invalid or excessive withdrawal and transfer amounts.
Provides feedback for invalid authentication attempts.


User-Friendly Interface : 

A simple text-based menu guides the user through various operations.


Database : 

here use the sqlite 3 database to store the date and admin see the all date of user 

# Code Structure
Account Class
Represents a bank account with the following features:

Attributes:
account_number: Unique identifier for the account.
pin: Used for secure authentication.
balance: Tracks the account's funds.
Methods:
check_balance(): Returns the current balance.
deposit(amount): Adds funds to the balance.
withdraw(amount): Deducts funds from the balance.
transfer(amount, target_account): Transfers funds to another account.
change_pin(old_pin, new_pin): Updates the PIN if the old PIN matches.
ATM Class
Simulates an ATM that interacts with multiple accounts:

Attributes:
accounts: A dictionary to store accounts using account_number as the key.
Methods:
add_account(account): Adds an account to the ATM's database.
authenticate(account_number, pin): Validates user credentials.
run(): Runs the ATM system, presenting a menu for user operations.
Demo Data
The system comes with preloaded accounts for testing:
Account 123456 with PIN 1234 and ₹5000 balance.
Account 654321 with PIN 4321 and ₹3000 balance.
Account 100100 with PIN 0000 and ₹3000 balance.


# How to Use
Run the program in a Python environment.
Use the on-screen menu to:
Check balance
Deposit money
Withdraw money
Transfer funds
Change your PIN
Use the preloaded demo accounts or add new accounts by modifying the code.
Example Usage
Deposit: Add ₹1000 to account 123456.
Withdraw: Withdraw ₹500 from account 654321.
Transfer: Transfer ₹1000 from account 123456 to account 654321.
Change PIN: Update PIN for enhanced security.
Developer
Developed by Harsh Hirpara.
