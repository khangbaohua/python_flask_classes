# # def = define
# def greeting(name):
#     print("hello", name); 
# # name is a parameter
# greeting("fred")
# # "fred" is an argument
# def shows the definition of function
# greeting("fred")-> functin call
# def num(start, end):
#     for i in range(start,end):
#         print(i)
# num(5,100)            

# def greet(name, food):
#     print("hello", name)
#     print("do you want have", food)
#     print("lets go to the supermarket")
# greet("fred","chicken") 

# def num(a,b,c):
#     print(a+b+c)
#     print(a-b-c)
#     print(a*b*c)
#     print(a/b/c)
#     print(a%b%c)
# num(1,2,3)

# def num(a):
#     for i in range(1,11):
#         print(a*i)
# num(3)


# def num(a,b):
#     if a<b:
#       print(b)
#     if a>b:
#       print(a)
#     if a==b:
#       print("both are equal")
# num(5,5)

# def num(a,b,c):
#     if a>b and a>c:
#         print(a)
#     if b>a and b>c:
#         print(b)
#     if c>a and c>b:
#         print(c)
#     if a==c==b:
#         print("all are equal")
# num(1,2,3)

# def string(a):
#     print(a[0])
#     print(a[-1])
# string("i am tired")

# mylist = [1,5,2,4,7,8,6,7,7,7,7,7,7,7]
# def num(a):
#     count = 0
#     for i in a:
#         if i==7:
#             count +=1
#     print(count)
# num(mylist)

# mystring = "i am uper cool"
# def num(a):
#     if a[5]=="s":
#         print("yes")
#     else:
#         print("no")
# num(mystring)

# mystring = "i"
# def string(a):
#     if len(a)>6 or len(a)==6:
#         print("yes")
#     if len(a)<6:
#         print("no")
# string(mystring)

# mylist = ["john","bob","jimmy","xaviers","abigail","steven"]
# def list(a):
#     for i in mylist:
#         if len(i)<6:
#             print("Happy diwali",i)
# list(mylist)

# mylist = [21.1,23.8,65.5,98.5]
# def num(a):
#     for i in a:
#         if type(i)==float:
#             print(int(i))
# num(mylist)

mylist = [1,5,2,4,7,8]
def num(a):
    sum=0
    for i in a:
        if i%3==2:
            sum+=i
    print(sum)
num(mylist)