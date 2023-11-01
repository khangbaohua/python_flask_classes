# 2) 23.5 45
# 3) True "khang"
# 4) 92, 23.5
# string
# every character has index
# print(mystring[0:12])
# print(mystring[2:12])
# print(mystring[-21:-11])
# print(mystring[2:-11])
# print(mystring[-21:12])
# print(mystring[-4:-20:-3])
# print(mystring[19:3:-3])
# print(mystring[19:-20:-3])
# print(mystring[-4:3:-3])
# print(mystring[0:19:2])
# print(mystring[-23:-4:2])
# print(mystring[0:-4:2])
# print(mystring[-23:19:2])
# print(mystring[10:23:2])
# print(mystring[-13::2])
# print(mystring[:])
# if you put nothing as end index, it would by default include everything till the end
# if you put nothing as start index, it would by default be 0 
# 

mystring = "stringnotesforpython1.2"
# string functions
# print(mystring.capitalize())
print(mystring.count(" "))
# print(mystring.index("noods"))
# print(mystring.endswith("string notes for python"))
# print(mystring.isalnum())
# mystring = "%i am@khang"
# for i in mystring:
    # if i.isalnum():
#         print(i,end=":")

# print(mystring.find("noods"))
# find and index both returns lowest index of the substring but index returns value error and find returns -1 when substring is not foun

# print(mystring.find("n"))
# for i in mystring:
#     if i.find("n"):
#         print(i)
# print(mystring.index())
# for i in mystring:
    # if i.index()

# # print(mystring.isalnum())
# if mystring.isalnum():
#     print("true")
# else:
#     print("false")

mystring = "user12345"
print(mystring.isdigit())

# print(mystring.isalpha())

print(mystring.isnumeric())
# superscript is when number is above or below the number like a exponent
# The isdigit() method accepts only decimals, subscripits, and supersscripts. the isnumeric( finction supports digits, vulgar, fractions,
# subscripts, superscripts, roman numeral, and currency numerators