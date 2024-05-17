# Task: Code a Number Guessing Game
# Create a Python script for a simple number guessing game. The game should:
# Initialize the Game:
# Import the necessary Python module to generate random numbers.
# Set a random number between 1 and 100 that the player needs to guess.
# Define the maximum number of attempts the player has to guess the number.
import random
number = random.randint(1,100)
max_tries = 5
attempts = 0
# Explain the Rules to the Player:
# Print a welcome message and explain that the player needs to guess a number between 1 and 100.
print("Welcome to guessing game. You will have to guess a number 1-100 and you have 5 tries. Good luck.")
# Create the Gameplay Loop:
# Use a for loop to give the player a fixed number of guesses.
# Within the loop, prompt the player to enter their guess.
# Check the player's guess using if/else statements:
# If the guess is too low, print "Too low."
# If the guess is too high, print "Too high."
# If the guess is correct, print a congratulatory message and break out of the loop.
for i in range(max_tries):
    guess = int(input("Enter guess: "))
    attempts+=1 
    if guess==number:
        print("Congratulations, you guessed it right!")
        break
    elif guess>number:
        print("Too high")
    elif guess<number:
        print("Too low")
    if max_tries==attempts:
        print("You've used up all your tries")
        print(f"this was the number, {number}")
        break