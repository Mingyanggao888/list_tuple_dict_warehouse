current_balance = 0

stock = {
    "product_name":{
        "quantity": 0,
        "unit_price":0}
}

history = []

while True:

    print("""
    Hello, Please enter any of the following command to start:
    - 'balance': To change current balance
    - 'sale': To record a sale (Product name, quantity, price)
    - 'purchase': To record a purchase (Product name, quantity, price)
    - 'account': To check the current account balance.
    - 'list': To check the total inventory in the warehouse (Product name, quantity, price)
    - 'warehouse': To check a product name and its status in the warehouse.
    - 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range. 
    - 'end': To exit the program""")


    command = input("\nEnter command: ")

    if command == "balance":
         account_change = float(input("Enter the amount to add the account balance or negative number to subtract from the account: "))
         current_balance += account_change
         change = "The account added: " + "$" + str(account_change) + ". Current balance of the account is $" + str(current_balance) + "."
         history.append(change)

    elif command == "sale":

         name_sale = input("Name of sold product: ")
         quantity_sale = int(input("Quantity sold: "))
         price_sale = float(input("Price of sold product: "))

         if name_sale in stock:

             if stock[name_sale]["quantity"] >= quantity_sale :
                 stock[name_sale]["quantity"] -= quantity_sale

                 current_balance += (price_sale * quantity_sale)
                 # Add record of change to history list
                 change = "Sales:" + str(quantity_sale ) + " unit of " + name_sale + ". $" + str(
                     quantity_sale * price_sale) + " amount was increased."
                 history.append(change)
             else:
                 print(f"Insufficient quantity for sales. ")

         else:
             print(f"The item {name_sale} is not available.")



    elif command == "purchase":

         name_purchase = input("Name of purchased product: ")
         quantity_purchase = int(input("Quantity of purchased product: "))
         price_purchase = float(input("Unit price of purchased product: "))


         if (price_purchase * quantity_purchase) > current_balance:
             print("There's no sufficient balance to make the purchase.")
             continue


         if name_purchase in stock:
             stock[name_purchase]["quantity"] += quantity_purchase

             current_balance -= (price_purchase * quantity_purchase)

         else:
             stock[name_purchase] = {
                 "quantity":  quantity_purchase,
                 "unit_price": price_purchase
             }

         change = "Purchase: " + str(quantity_purchase) + " unit of " + name_purchase + ". $" + str(quantity_purchase * price_purchase) + " was spent."
         history.append(change)

    elif command == "account":
         print(f"The current balance of the account is ${current_balance}.")

    elif command == "list":

         print("Product name | Quantity |  Unit price")
         print("----------------------------------------")

         for product, info in stock.items():
             quantity = info["quantity"]
             unit_price = info["unit_price"]
             print(f"{product:<12} | {quantity:>12} | {unit_price:>12}")

    elif command == "warehouse":
         search_name = input("Please enter a product name to search: ")
         if search_name in stock:
             quantity = stock[search_name]["quantity"]
             price = stock[search_name]["unit_price"]
             print(f""" Search result for product {search_name}:
                      Quantity: {quantity}
                      Unit price: {unit_price}
                      """)
         else:
             print(f"{search_name} cannot be found on the warehouse record.")

    elif command == "review":
         n_history = len(history)
         print(f"{n_history} operation(s) recorded on history. Please enter a from and to value to filter the result.\n")

         start = input("Please enter a from value: ")
         end = input("Please enter a to value: ")

         if start == "" and end == "":

             print("******** Operation history ********")
             print("----------------------------------------")

             for i in history:
                 print(i)
         elif start == "" and end != "":
             end = int(end)
             filter_history = history[:end]

             print("********  Operation history ********")
             print("----------------------------------------")

             for i in filter_history:
                 print(i)
         elif start != "" and end == "":
             start = int(start)
             filter_history = history[start - 1:]

             print("++++++++++ Operation history ++++++++++")
             print("----------------------------------------")
             for i in filter_history:
                 print(i)
         else:
             start = int(start)
             end = int(end)

             filter_history= history[start - 1:end]

             print("++++++++++ Operation history ++++++++++")
             print("----------------------------------------")
             for i in filter_history:
                 print(i)



    elif command == "end":

         print("Thank you! Ending program now...See you soon!")
         break
    else:
         print("Invalid command. Please enter another command.")