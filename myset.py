# myset = {"hi","bye","hi",1,True,}
# # print(myset)

# # # print(len(myset)) find len of set
# # # print(type(myset))
# # # newmyset = set(("hi",1,1,2,5,5,"hi"))
# # # print(newmyset)

# # # for i in myset:
# # # #     print(i)
# # # # print(11 in myset)
# # # # 1 and true are the same in python 0 and false are the same in python

# # # myset.add("khang")
# # # print(myset)

# # myset1 = {1,2,2,3,3,1}
# # # myset.update(myset1)
# # # print(myset)
# # # can also add using other things like string and list
# # # mylist = [1,51,2,8]
# # # myset.update(mylist)
# # # print(myset)
# # # myset.remove("no")
# # # print(myset)
# # # raises an error when the element is not  there in the set
# # # myset.discard("o")
# # # print(myset)
# # # discard funtion is also used to delete a particular elements and if the element is not present it doesn't do anything

# # # myset.pop()
# # # print(myset)
# # # pop function is used to delete random element from set
# # # set has no order by default, it can store the elements in any order

# # # myset.clear()
# # # print(myset)
# # # clear delete all the elements in the set

# # # del myset
# # # print(myset)

# # # del deletes the whole set from the program so that you cannot access it further
# # # if you try to access it, it shows error

# # myset2 = myset.union(myset)
# # print(myset2)
# # # union function is used to make a new set containing all the elements from both myset and myset1

myset1 = {1,4,5,1,1,2,4,6,7}
myset2 = {3,4,4,5,9,10,3}
myset1.intersection_update(myset2)
print(myset1)
# intersection_update stores all the common elements from set1 and set2