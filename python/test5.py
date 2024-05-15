# Q. You are given a string, you need to print all the words from it which has
# length more than or equals to 5 

# mystr = "Hello world I am the string"
# word = mystr.split()
# for i in word:
#     if  len(i) >= 5:
#         print(i)

# Q. You are given a string, you need to print all the words from it which has
# length more than or equals to 5 and starts with a character "a" 
# mystr = "Hello world I am the string you were talking about"
# word = mystr.split()
# for i in word:
#     if  len(i) >= 5 and i.startswith("a"):
#         print(i)

# Q. You are given a string, containing numbers and characters both. Can you print only all the numbers from it.
# mystr = "343982743894hello823worldyou areksdksd 45 6 amazing"
# for i in mystr:
#     if i.isdigit():
#         numbers+=i
# print(numbers)

# Q1. You are given a string, containing numbers and characters both. Can you print only all the alphabets from it.
# letters = ""
# for i in mystr:    
#     if i.isalpha():
#         print(i)
# Q2. You are given a string, containing words. Can you print words starts with "a" and ends with "e"

# word = mystr.split()
# for i in word:    
#     if i.startswith("a") and i.endswith("e"):
#         print(i)

# You are given a string containing numbers and alphabets and you need to print all the even numbers from it

# numbers = ""
# for i in mystr:
#     if i.isdigit():
#         if int(i)%2==0:
#             numbers+=i
# print(numbers)

# You are given a string containing numbers and alphabets and you need to print all the numbers which are divisible by 2 and 3 both
# for letter in mystr:
#     if letter.isalpha():
#         print(letter)
# for num in mystr:
#     if num.isdigit():
#         if int(num)%2==0 and int(num)%3==0:
#             print(num)

# You are given a string containing numbers and alphabets and you need to print the words which have even length
# word = Mystr.split()
# for i in word:
#     if len(i)%2==0:
#         print(i)

# You are given a string containing alphabets and you need to print all the words which has middle character as “k”.
# word = Mystr.split()
# for i in word:
#     if i[len(i)//2]=='k':
#         print(i)







# You are given a string containing alphabets and you need to make a new string containing the words
# which have even length in uppercase and With odd length in lowercase
# Mystr = "Hello I am the string you were talking about"
# word = Mystr.split()
# new_sentence = ""
# for i in word:
#     if len(i)%2==0:
#         new_sentence+=i.upper()
#     else:
#         new_sentence+=i.lower()
# print(new_sentence)

# You are given a list containing words you need to make a string out of those words from the list which have length more than more than 5

# Mylist = ["apple","mango","pear","blueberry","banana"]
# string = ""
# for i in Mylist:
#     if len(i)>5:
#         string+=i
# print(string)

# You are given a list containing words you need to make a string out of those words from the list which have lengths divisible by 3
# Mylist = ["apple","mango","pear","blueberry","banana"]
# string = ""
# for i in Mylist:
#     if len(i)%3==0:
#         string+=i
# print(i)

# You are given a string which contains numbers and alphabets. I want the sum of all the numbers which are even
Mystr = "Hello 42587896591978439785445"
# sum = 0
# for i in Mystr:
#     if i.isdigit() and int(i)%2==0:
#         sum+=int(i)
# print(sum)

# You are given a string which contains numbers and alphabets. I want the average of all the numbers which are even
# count = 0
# sum = 0
# for i in Mystr:
#     if i.isdigit() and int(i)%2==0:
#         sum+=int(i)
#         count+=1
# average = sum/count
# print(average)
    
# Print Even Numbers:Write a program that uses a for loop to print all even numbers from 2 to 20.
# for i in range(2,21):
#     if i%2==0:
#         print(i)

# Print Odd Numbers:
# Use a for loop to print all odd numbers from 1 to 19.
# for i in range(1,20):
#     if i%2!=0:
#         print(i)

# Print Numbers in Reverse:
# Write a program that uses a for loop to print numbers from 10 to 1 in reverse order.
# for i in reversed(range(1,11)):
#     print(i)
# or 
# for i in range(11,0,-1):
#     print(i)

# Count By Fives:
# Use a for loop to print numbers from 5 to 50, counting by fives

# for i in range(5,51,5):
#     print(i)

# Write a program that uses a for loop to print numbers from -1 to -10.
# for i in range(-1,-11,-1):
#     print(i)

# Double and Print Numbers:
# Write a program that doubles numbers from 1 to 10 and prints each result using a for loop.

# for i in range(1,11,):
#     double = i*2
#     print(double)

# Print the First 10 Multiples of a Given Number:
# Ask the user for a number and use a for loop to print the first 10 multiples of that number.

# number = int(input("Enter a number: "))
# print(number)
# for i in range(1,11):
#     print(number * i)

# Countdown with a Twist:
# Write a program that uses a for loop to print a countdown from 20 to 1, but only print the numbers that are divisible by 3.

# for i in range(20,0,-1):
#     if i%3==0:
#         print(i)

# Print the First 10 Square Numbers:
# Use a for loop to print the squares of the numbers from 1 to 10 (i.e., 1, 4, 9, ..., 100).
# for i in range(1,11):
#     squared = i**2
#     print(squared)

# List Indexes:
# Given a list of colors (e.g., ["red", "blue", "green"]), use a for loop to print each color and its corresponding index in the list.
# list = ["red","blue","green"]
# for i in range(len(list)):
#     print("i:", i, "color:",list[i])

# Print Each Character:
# Write a program that uses a for loop to print each character of a given string one by one.
# string =   "askdkjsdhkladh"
# for i in string:
#     print(i)

# Count Specific Character:
# Ask the user for a string and a character, then use a for loop to count how many times that character appears in the string.
# string = input("Enter string: ")
# char = input("enter char: ")
# count = 0
# for i in string:
#     if char == i:
#         count+=1
# print(count)

# Reverse a String:
# Write a program that uses a for loop to reverse a string and print the reversed version.

# string = "looc"
# string2 = ""
# for i in range(len(string)-1,-1,-1):
#     string2 += string[i]
# print(string2)

# Print Characters at Even Indices:
# Write a program that prints characters located at even indices in a given string using a for loop.
# string = "super cool"
# evenletters = ""
# for i in range(len(string)):
#     if i%2==0:
#         evenletters+=string[i]
# print(evenletters)
# Capitalize Each Word:
# Use a for loop to go through a string and capitalize the first letter of each word. Assume the words are separated by spaces.
strin = "amazing banana holder"
upper = ""
for i in strin.split():
    upper+=i.capitalize()
print(upper)