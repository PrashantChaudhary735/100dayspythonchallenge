import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many number would you like in your password?\n"))
# Easy level : Printin the password in the same sequence which the user is passing above.

password = ''
for char in range(1, nr_letters + 1):
    password = password + random.choice(letters)
print(password)

for char in range(1, nr_symbols + 1):
    password = password + random.choice(symbols)
print(password)

for char in range(1, nr_numbers + 1):
    password = password + random.choice(numbers)
print(f'Your password is mentioned below: \n{password}')

# Hard Level
# Using random.shuffle() function to shuffle the above password
# Converted the password string in list to use the shuffle function.
password_list = list(password)
random.shuffle(password_list)
# Converted the password_list to string again
password = ''.join(password_list)
print(f'Your password after shuffle is mentioned below:\n{password}')