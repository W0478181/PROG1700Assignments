import sys

tries = 0

customers = {
    1: {"firstname": "Alice", "lastname": "Byers", "contact": "123-456-7890", "orders": []},
    2: {"firstname": "Bob", "lastname": "Rhynolds", "contact": "098-765-4321", "orders": []}
}

while True:
    print("Order and Customer Management System Menu:")
    user_input = input("""
        1. Add Customer
        2. Place Order
        3. Generate Customer Report
        4. Generate All Customer Reports
        5. Exit
        :""")

    if user_input.isdigit():
        user_input = int(user_input)

        if user_input == 1:
            print('one')

        elif user_input == 2:
            print('two')

        elif user_input == 3:
            while tries < 3:
                search_cust_id = int(input("Enter Customer ID to find customer info: "))

                if search_cust_id in customers:
                    print(f'\nCustomer ID: {search_cust_id}')
                    for key, value in customers[search_cust_id].items():
                        print(f'{key}: {value}')
                    break
                else:
                    print(f'Customer ID {search_cust_id} was not found.')
                    tries += 1
                    continue
            if tries == 3:
                print("Too many failed attempts. Please try again.")
                sys.exit()

        elif user_input == 4:
            for cust_id, cust_info in customers.items():
                print('\nCustomer ID:', cust_id)
                for key, value in cust_info.items():
                    print(f'{key}: {value}')

        elif user_input == 5:
            print('Thank You, Goodbye')
            sys.exit()

        else:
            print("Invalid input. Please enter a number between 1 and 5.")
            break
    else:
        print("Invalid input. Please enter a number.")
