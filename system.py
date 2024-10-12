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

"""

main_list = []
product_list = []

while True:
    # Register the product using the input function
    name = input("Enter the name of the product: ")
    product_list.append(name)

    # Register the price of the product using the input function
    price = input("Enter the price of the product: ")
    product_list.append(price)

    # Register the quantity of the product using the input function
    quantity = input("Enter the quantity of the product: ")

    # Append the quantity to the product list
    product_list.append(quantity)

    # Append the product list to the main list
    main_list.append(product_list)

    # Clear the product list
    product_list = []

    # Ask the user if they want to add more products
    answer = input("Do you want to add more products? (yes/no): ")

    if answer == "no":
        break


print("The products registered: ", main_list)
