"""

Goal: Create a system that can be used to register for products.

The information that we need to collect is:
- Name
- Price
- Quantity

The system should be able to:
- Register the product using the input function

We can use the following data structure to store the information:
- List of List
[["Laptop", 1000, 2], ["Mouse", 20, 5], ["Keyboard", 50, 3]]

- I want to refactor my code to use a dictionary and store like this:
[
{"name": "Laptop", "price": 1000, "quantity": 2},
{"name": "Mouse", "price": 20, "quantity": 5},
{"name": "Keyboard", "price": 50, "quantity": 3}

]

"""

import json

main_list = []
product_dict = {}

while True:
    # Register the product using the input function
    name = input("Enter the name of the product: ")
    product_dict.update({"name": name})

    # Register the price of the product using the input function
    price = input("Enter the price of the product: ")
    product_dict.update({"price": float(price)})
☺☻
    # Register the quantity of the product using the input function
    quantity = input("Enter the quantity of the product: ")

    # Append the quantity to the product list
    product_dict.update({"quantity": int(quantity)})

    # Append the product list to the main list
    main_list.append(product_dict)

    # Clear the product list
    product_dict = {}

    # Ask the user if they want to add more products
    answer = input("Do you want to add more products? (yes/no): ")

    if answer == "no":
        with open("data/products.json", "w") as file:
            json.dump(main_list, file)
        break


print("The products registered: ", main_list)
