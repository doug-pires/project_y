# Naming functions: snake_case
# Parameters names: snake_case, without abbreviations
# Docstrings: use """triple double quotes"""
# Single Responsibility Principle: a function should do only what is is supposed to do. If you need to add something to the function, create a new one.
# ( BONUS ) SOLID Principles: Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, Dependency Inversion Principle


# Bad function


def greeting(n):
    print(f"Hello, {n}!")


# Good function


def say_hello_to(name):
    """This function greets the user by their name.

    Args:
        name (str): The name of the user.
    """
    message = f"Hello, {name}!"
    print(message)
    return message


# Multiple responsabilities
def say_hello_to_and_save_the_file(name):
    print(f"Hello, {name}!")
    with open("greetings.txt", "a") as file:
        file.write(f"Hello, {name}!\n")


def save_the_file(text):
    with open("greetings.txt", "a") as file:
        file.write(f"{text}\n")


message = say_hello_to("Maria")
save_the_file(message)
