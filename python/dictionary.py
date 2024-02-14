mydict = {
    "Name": "Megan", "Age": "10", "score": "95", 94: 52, 12.5: 22.9

}

#dictionary has no indexs
#dictionary contains key, value and "megan" is its value
#keys are uniqe (cannot be repeated)
#values can be repeated
#how to access elements in a dictionary 
print(mydict[12.5])

mydict["grade"]=3
print(mydict)

mydict["score"]=19
print(mydict)

# mydict.popitem()
# print(mydict)

# print(mydict.keys())

# print(mydict.values())

# print(mydict.items())

# for key in mydict:
#     print(key)

# for value in mydict.values():
#     print(value)

# for key, value in mydict.items():
#     print(key, value)

for key in mydict:
    print(key,mydict[key])

# 1. items() used to print all key value pairs in the dictionary
# 2. keys() used to print all the keys
# 3. values() used to priny all values
# 4. pop(key) used to delete a key of choosing and value
# 5. popitem used to delete last key and value