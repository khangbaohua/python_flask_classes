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
count = 0
sum = 0
for i in Mystr:
    if i.isdigit() and int(i)%2==0:
        sum+=int(i)
        count+=1
average = sum/count
print(average)
    
