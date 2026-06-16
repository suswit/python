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



# # import tkinter
# # m=tkinter .Tk()
# # '''
# # widgets are added here 
# # '''
# # m.mainloop()

# # import tkinter as tk

# # main=tk.Tk(className="emi calculator")
# # main.geometry("600x600")

# # label1=tk.Label(main,text="python")
# # txt1=tk.Entry(main)
# # btn1=tk.Button(main,text="submit")

# # label1.grid(row=0,column=0)
# # txt1.grid(row=0,column=1)
# # btn1.grid(row=1,column=1)

# # main.mainloop()

# # def my_function():
# #     '''Demonstrate triple double quotes
# #     docstrings and does nothing really.'''

# #     return None

# # print("Using_Doc_:")
# # print(my_function.__doc__)

# # print("Using help:")
# # help(my_function)

# # def cube(y):
# #     return y*y*y

# # lambda_cube = lambda y: y*y*y

# # # using function defined
# # # using def keyword
# # print ("Using function defined with 'def' keyword,cube:",cube(5))

# # # using the lambda function
# # print("Using lambda function, cube:",lambda_cube(5))

# # def add(y):
# #     return y+y+y

# # lambda_cube = lambda y: y+y+y

# # # using function defined
# # # using def keyword
# # print ("Using function defined with 'def' keyword,cube:",add(5))

# # # using the lambda function
# # print("Using lambda function, cube:",lambda_cube(5))

# # mytuple = ("alpha","beta","gamma")
# # myit = iter(mytuple)

# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# # print(next(myit))


# import tkinter as tk
# main=tk.Tk(className="student id card")
# main.configure(bg="black")
# main.geometry("1000x1000")

# label1=tk.Label(main,text="CHRISTIANO RONALDO").grid(row=0,column=0)
# txt1=tk.Entry(main).grid(row=0,column=1)  

# label1=tk.Label(main,text="LIONEL MESSI").grid(row=1,column=0)
# txt1=tk.Entry(main).grid(row=1,column=1)  


# label=tk.Label(main,text="NEYMAR JR").grid(row=2,column=0)
# txt1=tk.Entry(main).grid(row=2,column=1)

# label=tk.Label(main,text="IBRAHIMOVIC").grid(row=3,column=0)
# txt1=tk.Entry(main).grid(row=3,column=1)

# label=tk.Label(main,text="PAUL POGBA").grid(row=4,column=0)
# txt1=tk.Entry(main).grid(row=4,column=1)

# label=tk.Label(main,text="PELE").grid(row=5,column=0)
# txt1=tk.Entry(main).grid(row=5,column=1)

# label=tk.Label(main,text="MBAPPE").grid(row=6,column=0)
# txt1=tk.Entry(main).grid(row=6,column=1)

# label=tk.Label(main,text="JOO_7").grid(row=7,column=0)
# txt1=tk.Entry(main).grid(row=6,column=1)




# main.mainloop()


