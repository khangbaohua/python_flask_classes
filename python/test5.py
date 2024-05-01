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
mystr = "343982743894hello823worldyou areksdksd 45 6 amazing"
# numbers = ""
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

word = mystr.split()
for i in word:    
    if i.startswith("a") and i.endswith("e"):
        print(i)