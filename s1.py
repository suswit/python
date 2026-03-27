class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            print("Account already exists.")
            return
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        self.accounts[acc_no] = BankAccount(acc_no, name, balance)
        print("Account created successfully.")

    def deposit_money(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter amount to deposit: "))
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter amount to withdraw: "))
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account not found.")

    def transfer_money(self):
        from_acc = input("Enter Sender Account Number: ")
        to_acc = input("Enter Receiver Account Number: ")

        if from_acc in self.accounts and to_acc in self.accounts:
            amount = float(input("Enter amount to transfer: "))
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid account details.")

    def check_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            self.accounts[acc_no].display_details()
        else:
            print("Account not found.")


def main():
    bank = Bank()

    while True:
        print("\n===== BANK MENU =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit_money()
        elif choice == '3':
            bank.withdraw_money()
        elif choice == '4':
            bank.transfer_money()
        elif choice == '5':
            bank.check_account()
        elif choice == '6':
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
