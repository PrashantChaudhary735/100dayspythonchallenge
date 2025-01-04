# Day3: Treasure island project
print("Welcome to the treasure island")
print("Your mission is to find the treasure.")

user_input = input("You're at cross road. Where do you want to go? \n\t Type 'left' or 'right'. ")
if user_input.lower() == 'right':
    print("Oh! Unfortunately, you are hit by a truck. Game Over!")
else:
    if user_input.lower() == 'left':
        user_input = input("You came to a lake. Do you want to 'swim' or 'wait'.")
        if user_input.lower() == 'wait':
            user_input = input("You have seen three doors 'Red', 'Blue' and 'Yellow. Which door you want to choose? ")
            if user_input.lower() == 'yellow':
                print("You have found the Treasure. You Win!")
            elif user_input.lower() == 'blue':
                print("You have find a lion inside the blue room. Game Over!")
            else:
                print("You have find a door which is fired. Game Over!")
        elif user_input.lower() == 'swim':
            print("You are eaten by a crocodile. Game Over!")


