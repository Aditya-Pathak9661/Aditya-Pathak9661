#make a name , email, or password formate in python--
name = input("enter your name: ")
email = input("enter E-mail: ")
password = input("create password: ")

if name == " ":
    print("please enter your name;")
else:
    if "@" not in email:
        print("please enter a valid E-mail;")
    else:
        if len(password)<= 8:
            print("make a strong password (<= 8).")
        else:
            print("login succesfully")
    
#guessing a number(game) --

import random

# Generate a random number
number_to_guess = random.randint(1, 100)
attempts = 0

print("Guess the number (between 1 and 100)!")

while True:
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break