accounts = []  # initialize empty list to store accounts

while True:
    # display menu options
    print("\nMenu:")
    print("1. Enter account info")
    print("2. Display list of accounts")
    print("3. Quit")
    
    # prompt user for menu choice
    choice = input("Enter your choice (1-3): ")
    
    # process user's choice
    if choice == '1':
        # prompt user for account info
        account_number = input("Enter account number: ")
        name = input("Enter name: ")
        balance = float(input("Enter balance: "))
        
        # add account to list
        accounts.append({'account_number': account_number, 'name': name, 'balance': balance})
        print("Account added.")
    elif choice == '2':
        # display list of accounts
        if not accounts:
            print("No accounts found.")
        else:
            print("\nList of accounts:")
            for account in accounts:
                print(f"{account['account_number']}: {account['name']} - {account['balance']}")
    elif choice == '3':
        # quit program
        print("Goodbye.")
        break
    else:
        # invalid menu choice
        print("Invalid choice. Please try again.")
