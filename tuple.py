# mytuble = (1,2,3,"banana","tree")
# print(mytuble[2])

# # mytuble[2]=9
# print(mytuble)

# # mylist2 = [1,2,3,"banana","tree"]
# # # print(mytuble[2])

# # mylist2[2]=9
# # print(mylist2)

# # can change value of a list but not tuple
# # list is mutable and tuble is immutable
# print(len(mytuble))#use to find len for tuple

# mytuple = ("cheese")
# print(type(mytuple))

# mytuple2 = (1,)
# print(type(myt3uple2))
# a single element tuple is not a tuple until it has a comma after the value

# mylist = [3,2,4,"banana","cheese",7,8]
# print(type(mylist))

# mytuple = tuple(mylist)
# print(type(mytuple))
# tuple()is a constructor that is used to convert a data type to tuple
# both negative and positive indexing work for tuple also
# list slicing also works in tuples
# all operators work the same way with tuples as in list
# for loop in tuples work the same way as with list
# append function is not in tuple because we cannot add value in tuple append, is not function
# append , insert function is not there in tuples as we cannot add a value in tuples.
# remove, pop functions do not work in tuples as we cannot delete a value from tuple.
# del mytuple[2] doesn't work in tuple as we cannot delete a value from tuple.
# we need to come back on a topic(packing and unpacking of tuples)

mytuple = (7,5,4,True,"tree","fruit",8)
# for i in mytuple:
#     print(i)

print(mytuple[2:4])