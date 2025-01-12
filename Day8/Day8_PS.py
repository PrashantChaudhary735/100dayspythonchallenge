# Functions without inputs
# def greet():
#     user_name = input("What's your name?")
#     print(f"Hello {user_name}!")
#     print("Good Morning!")
#
#
# greet()


# Functions with inputs
# def greet_with_name(name): # "name" is parameter here which is present inside the function
#     print(f"Hello {name}")
#
#
# greet_with_name("Prashant") # 'Prashant' is argument, which is passed to the function


# Function with more than 1 input:
# def greet_with(name, location):
#     print(f"Hello {name}")  # F string in python
#     print("What is it like to be in", location, "?")  # Without f string
#
#
# greet_with("Prashant", "Nowhere")
# Above code is an example of positional arguments, where the arguments are passed in sequence to the parameters used
# in function

# Keyword arguments: Below is the example of keyword argument, pass the parameter name with arguments.
# greet_with(location='Nowhere', name='Prashant')

print(reversed('Hello'))