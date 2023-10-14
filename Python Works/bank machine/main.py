import time

accountA = {
    "account_id": "123456789",
    "password": "1234",
    "account_owner_name": "Nuri Bugra Demir",
    "account_balance": 10000,  # Turkish lira
}
accountB = {
    "account_id": "123456788",
    "password": "1111",
    "account_owner_name": "Deniz Berk Demir",
    "account_balance": 1000,  # Turkish lira
}

account_selection = accountA


while True:

    transaction = input("Select the Transaction You Want to Perform.\n1- Withdraw\n2- Deposit\n0- Quit\n")


    def withdraw_money(account):

        password = input("Please enter your PIN to access your account.\nPIN: ")

        if password == account["password"]:
            print(f"Hello, {account['account_owner_name']}")

            time.sleep(0.5)
            print("Account Balance: ", account["account_balance"])
            time.sleep(0.25)

            amount = int(input("Enter withdrawal amount: "))

            time.sleep(1)

            if amount > account["account_balance"]:
                print("Sorry, your account balance is not enough for this withdraw transaction.")
            elif amount <= account["account_balance"]:
                print("Withdrawal is successful.")
                account['account_balance'] -= amount
                print(f"Your new balance is {account['account_balance']}")
            else:
                print("Something went wrong.")
        elif password != account["password"]:
            print("PIN is wrong, please try again or contact your bank.")
            withdraw_money(account)
        else:
            print("Something went wrong.")


    def deposit_money(account):

        password = input("Please enter your PIN to access your account.\nPIN: ")

        if password == account["password"]:

            print(f"Hello, {account['account_owner_name']}")

            time.sleep(0.5)
            print("Account Balance: ", account["account_balance"])
            time.sleep(0.25)

            amount = int(input("Enter deposit amount: "))

            time.sleep(1)

            account['account_balance'] += amount
            print(f"Deposit is successful.")

            time.sleep(1)

            print(f"Your new balance is {account['account_balance']}")
        elif password != account["password"]:
            print("PIN is wrong, please try again or contact your bank.")
            withdraw_money(account)
        else:
            print("Something went wrong.")


    if transaction == "1":
        withdraw_money(account_selection)
    elif transaction == "2":
        deposit_money(account_selection)
    elif transaction == "0":
        quit()
    else:
        print("Please choose a valid option.")


