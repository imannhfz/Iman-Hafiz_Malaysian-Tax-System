from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

filename = "tax_records.csv"
registered_users = {}

def line():
    print("------------------------------------------------------")

while True:
    print("\n")
    line()
    print("                 MALAYSIAN TAX SYSTEM")
    line()
    print("1. Register")
    print("2. Login")
    print("3. View Tax Records")
    print("4. Exit")
    line()

    choice = input("Enter choice (1-4): ")
    print()

    if choice == "1":
        line()
        print("                USER REGISTRATION")
        line()

        user_id = input("Create a new User ID: ")
        ic = input("Enter your IC Number (12 digits): ")

        registered_users[user_id] = ic

        print("\n Registration successful! Please proceed to login.")
        line()

    elif choice == "2":
        line()
        print("                       LOGIN")
        line()

        user_id = input("Enter User ID: ")

        if user_id not in registered_users:
            print("\n User not registered!")
            line()
        else:
            ic = registered_users[user_id]

            password = input("Enter password (last 4 digits of IC): ")

            if verify_user(ic, password):
                print("\n Login successful!")
                line()

                income = float(input("Enter Annual Income (RM): "))
                relief = float(input("Enter Total Tax Relief (RM): "))

                tax = calculate_tax(income, relief)

                print("\n=================== TAX SUMMARY ===================")
                print("Chargeable Income  : RM", round(income - relief, 2))
                print("Tax Relief         : RM", round(relief, 2))
                print("Tax Payable        : RM", round(tax, 2))
                print("====================================================\n")

                data = {
                    "IC_Number": ic,
                    "Income": income,
                    "Tax_Relief": relief,
                    "Tax_Payable": tax
                }

                save_to_csv(data, filename)
                print(" Tax record saved successfully!")
                line()

            else:
                print("\n Incorrect password!")
                line()

    elif choice == "3":
        line()
        print("                  SAVED TAX RECORDS")
        line()

        df = read_from_csv(filename)

        if df is not None:
            print(df)
        else:
            print("No records found.")

        line()

    elif choice == "4":
        print("\nThank you for using the Malaysian Tax System!")
        line()
        break
    else:
        print("\n Invalid choice! Please select 1–4.")
        line()