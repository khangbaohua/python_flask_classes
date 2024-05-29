# Task: Code a Number Guessing Game
# Create a Python script for a simple number guessing game. The game should:
# Initialize the Game:
# Import the necessary Python module to generate random numbers.
# Set a random number between 1 and 100 that the player needs to guess.
# Define the maximum number of attempts the player has to guess the number.
# import random
# number = random.randint(1,100)
# max_tries = 5
# attempts = 0
# # Explain the Rules to the Player:
# # Print a welcome message and explain that the player needs to guess a number between 1 and 100.
# print("Welcome to guessing game. You will have to guess a number 1-100 and you have 5 tries. Good luck.")
# Create the Gameplay Loop:
# Use a for loop to give the player a fixed number of guesses.
# Within the loop, prompt the player to enter their guess.
# Check the player's guess using if/else statements:
# If the guess is too low, print "Too low."
# If the guess is too high, print "Too high."
# If the guess is correct, print a congratulatory message and break out of the loop.
# for i in range(max_tries):
#     guess = int(input("Enter guess: "))
#     attempts+=1 
#     if guess==number:
#         print("Congratulations, you guessed it right!")
#         break
#     elif guess>number:
#         print("Too high")
#     elif guess<number:
#         print("Too low")
#     if max_tries==attempts:
#         print("You've used up all your tries")
#         print(f"this was the number, {number}")
#         break

# You are given a list of numbers. Your task is to write a function calculate_median that takes in a list of integers or floating-point numbers and returns the median of the list
# The median is the middle value in a list when the numbers are sorted in ascending order.
# If the list has an even number of elements, the median is the average of the two middle numbers.

# numbers = [1,2,3,1,2,4,11,6,1,1,1,1,1,1,1,1,2,2,2,3,3,8,8]
# def calculate_median(numbers):
#     numbers.sort()
#     print(numbers)
#     lens = len(numbers)
#     ans = 0
#     if lens%2==0:
#         index1 = lens//2
#         index2 = lens//2+1
#         ans = (numbers[index1]+numbers/[index2])//2
#     else:
#         index = lens//2
#         ans = numbers[index]
#     return ans
# ans = calculate_median(numbers)
# print(ans)

# Given a list of integers, write a Python function that finds the second largest number in the list. You must not use any built-in functions like sort() or max(), and ensure your solution can handle lists with duplicates.
# Sample Input:
# [7, 5, 6, 3, 4, 1, 2, 7, 5]
# Expected Output:d
# def max(nums):
#     max = nums[0]
#     for i in nums:
#         if i>max:
#             max = i
#     return max
# num = [7, 5, 6, 3, 4, 1, 2, 7, 5]
# maximum = max(num)


# def second_largest(n):
#     second = 0
#     for i in n:
#         if second<i and i<maximum:
#             second = i
#     return second        
# n = [7, 5, 6, 3, 4, 1, 2, 7, 5]
# second_largest_number = second_largest(n)
# print(second_largest_number)

# You need to take 3 integers as input and  print which one is the greatest among them

