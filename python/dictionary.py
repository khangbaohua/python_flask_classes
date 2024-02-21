mydict = {
    "Name": "Megan", "Age": "10", "score": "95", 94: 52, 12.5: 22.9

}

# #dictionary has no indexs
# #dictionary contains key, value and "megan" is its value
# #keys are uniqe (cannot be repeated)
# #values can be repeated
# #how to access elements in a dictionary 
# print(mydict[12.5])

# mydict["grade"]=3
# print(mydict)

# mydict["score"]=19
# print(mydict)

# # mydict.popitem()
# # print(mydict)

# # print(mydict.keys())

# # print(mydict.values())

# # print(mydict.items())

# # for key in mydict:
# #     print(key)

# # for value in mydict.values():
# #     print(value)

# # for key, value in mydict.items():
# #     print(key, value)

# for key in mydict:
#     print(key,mydict[key])

# # 1. items() used to print all key value pairs in the dictionary
# # 2. keys() used to print all the keys
# # 3. values() used to priny all values
# # 4. pop(key) used to delete a key of choosing and value
# # 5. popitem used to delete last key and value

# # What is a dictionary in programming? holds a key amd value in programming
# # How do you add a new item to a dictionary? mydict["key"]="value"
# # Can a dictionary have two items with the same key? no
# # How do you access the value of a specific key in a dictionary? print(mydict["lala"])
# # What happens if you try to access a key that is not in the dictionary? error
# # How can you check if a key is present in a dictionary? you look in the dictionary
# # What does the pop method do in relation to dictionaries? delete a key pair of choosing
# # How do you update the value of an existing key in a dictionary? mydict.update
# # Can a dictionary have a number as a key? yes
# # How do you remove a key-value pair from a dictionary? pop or popitem

mydict["lala"]="lele"
# print(mydict["lala"])

# print(mydict["no"])


# delete key pair in dictionary

mydict[21]=21
# print(mydict)

# mydict.update()
# print(mydict)


# mydict.pop("lala")
# print(mydict)

list = "Join these words"
print("-".join(list.split()))

# 1. [2,3,4]
# 2. a
# 3. a
# 4. b
# 5. b
# 6. c
# 7. a
# 8. d
# 9. 5