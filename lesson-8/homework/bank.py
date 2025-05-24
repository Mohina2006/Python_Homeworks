import random
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
class Bank:
    accounts = {}
    def create_account(self, name, initial_deposit):
        try:
            if initial_deposit < 0:
                raise ValueError("Initial deposit must be non-negative.")

            account_number = random.randint(100000, 999999)
            while account_number in self.accounts:
                account_number = random.randint(100000, 999999)

            new_account = Account(account_number, name, initial_deposit)
            self.accounts[account_number] = new_account

            with open("accounts.txt", "a") as f:
                f.write(f"{account_number},{name},{initial_deposit}\n")

            print(f"Account created successfully! Account Number: {account_number}")

        except Exception as e:
            print(f"Error creating account: {e}")

    def view_account(self, account_number):
        if account_number in self.accounts:
            try:
                account = self.accounts[account_number]
                print(f"Account number: {account.account_number}")
                print(f"Name: {account.name}")
                print(f"Balance: {account.balance}")
            except Exception as e:
                print(f"Unexpected error accessing account: {e}")
        else:
            print("Account number not found, please try again!")
            
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            try:
                if amount < 0:
                    print("Deposit number must be positive")
                    return
                self.accounts[account_number].balance += amount
                print(f"$ {amount} deposited successfully. New balance: ${self.accounts[account_number].balance}")
            except Exception as e:
                print("An error occurred during deposit")
        else:
            print("Account number not found")
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            try:
                account = self.accounts[account_number]
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                    return
                if amount > account.balance:
                    print("Insufficient funds.")
                    return
                account.balance -= amount
                print(f"${amount} withdrawn successfully. Remaining balance: ${account.balance}")
            except Exception as e:
                print(f"An error occurred during withdrawal: {e}")
        else:
            print("Account number not found.")
    def save_to_file(self, filename = "accounts.txt"):
        try:
            with open(filename, "w") as file:
                for acc_num, account in self.accounts.items():
                    line = f"{account.account_number},{account.name},{account.balance}\n"
                    file.write(line)
                print("All accounts have been saved successfully")
        except Exception as e:
            print("Error occurred while saving accounts")
    def load_from_file(self, filename = "accounts.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    acc_num, name, balance = line.strip().split(",")
                    acc_num = int(acc_num)
                    balance = float(balance)
                    self.accounts[acc_num] = Account(acc_num, name, balance)
                print("All accounts loaded successfully")
        except FileNotFoundError:
            print("No existing accounts found — starting fresh.")
        except Exception as e:
            print(f"Error loading accounts: {e}")

def main():
    bank = Bank()
    bank.load_from_file()  # <- fixed

    while True:
        print("\nWelcome to the Bank System")
        print("1. Create an account")
        print("2. View account")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))  # <- fixed
        except ValueError:
            print("Please enter a valid number from 1 to 5.")
            continue

        if choice == 1:
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, initial_deposit)
            except ValueError:
                print("Invalid initial deposit amount")
        elif choice == 2:
            try:
                acc_num = int(input("Enter your account number: "))
                bank.view_account(acc_num)
            except ValueError:
                print("Invalid account number.")
        elif choice == 3:
            try:
                acc_num = int(input("Enter your account number: "))
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(acc_num, amount)
            except ValueError:
                print("Invalid input for account number or deposit amount.")
        elif choice == 4:
            try:
                acc_num = int(input("Enter your account number: "))
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(acc_num, amount)
            except ValueError:
                print("Invalid input for account number or withdrawal amount.")
        elif choice == 5:
            bank.save_to_file()
            print("Thank you for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
if __name__ == "__main__":
    main()