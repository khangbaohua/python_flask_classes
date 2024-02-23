# m = "Hello, young coder!"
# print(m)

# num1 = 5
# num2 = 7
# sum = num1+num2
# if sum%2==0:
#     print("even")
# else:
#     print("odd")


# a = int(input("What is your age: "))
# print(f"Wow, {a} year old! Keep up the coding spirit!")

# for i in range(1,11):
#     print(7*i)

# for i in range(10,0,-1):
#     print(i)

# name = "khang"
# for i in name:
#     print(i)
# sum = 0
# for i in range(1,21):
#     if i%2==0:
#         sum+=i
# print(sum)

list = ["orange", "red", "blue", "maroon"]
list.append("green")
list.remove("red")
print(list)

# Create a simple calculator program that takes two numbers and an operator (+, -, *, /) as input from the user. Perform the corresponding operation and print the result. Ensure to handle division by zero.

def calculator(a,b,operator):
    if operator=="+":
        c=a+b
    elif operator=="-":
        c=a-b
    elif operator=="*":
        c=a*b
    elif operator=="%":
        c=a%b
    elif operator=="/":
        c=a/b
    elif operator=="//":
        c=a//b
    return c