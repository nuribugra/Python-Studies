import time

accountA = {
    "name" : "Nuri Buğra Demir",
    "account_id" : "34565462432",
    "balance" : 5000,
}

accountB = {
    "name" : "Deniz Berk Demir",
    "account_id" : "77569598458",
    "balance" : 3000,
}

def withdraw_money(account, amount):
    print(f"Hello, the account name is {account['name']}")
    print(f"Account Id : {account['account_id']}")

    time.sleep(1)

    if (amount > account['balance']):
        print("Sorry, you don't have enough money for this transaction.")
    elif (amount <= account['balance']):
        print("Withdrawal is successful.")
        account['balance'] -= amount
        print(f"Your new balance is {account['balance']}")
    else:
        print("Something went wrong.")

def deposit_money(account, amount):
    print(f"Hello, the account name is {account['name']}")
    print(f"Account Id : {account['account_id']}")

    time.sleep(3)

    account['balance'] += amount
    print(f"Deposit is successful.")

    time.sleep(1)

    print(f"Your new balance is {account['balance']}")

withdraw_money(accountA, 1000000)

deposit_money(accountB, 2000)

print(accountA["balance"])
print(accountB["balance"])