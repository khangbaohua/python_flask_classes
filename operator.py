# arithematic operator
# +,-,*,/,%,**,//

# print(5+3)
# print(5-3)
# print(5*3)
# print(5/3)
# print(5%3)
# print(5**3)
# print(5//3)

# + i addition
# - is subtraction
# * is multiplication
# / is division
# % returns remainder modulo operator
# ** is exponent
# // integer devision which mean the answer never decimal

# assignment operator
# =,+=,-+,/=,%=,**=,//=
# x=3
# print(x)
# x+=2
# print(x)
# x-=1
# print(x)
# x*=3
# print(x)
# x/=4
# print(x)
# x%=7
# print(x)
# x**=2
# print(x)
# x//=3
# print(x)

# conditional/relational operator
# x = 3 
# if x == 0:
#     print("equal")
# elif x >= 4:
#     print("greater or equal")
# elif x > 4:
#     print("greater")
# else:
#     print("default")
# these are relation operator and used in conditional statements

# logical operator
# if 4 > 6 and not(8 > 5):
#     print("one")
# elif not(4 > 5) or not(5 == 5):
#     print("two")
# else:
#     print("none")
# and, or, mot are logical operator and used in conditional statements

# membership operator
# mylist = ["apple", "mango", "banana"]
# print("apple" in mylist)
# mylist2 = ["burger","python","list"]
# mylist3 = ["print","orange","red"]
# mylist4 = ["list4","hands","type"]
# print("burger"in mylist2)
# print("python" in mylist2)
# print("list" in mylist2)
# print("print" not in mylist3)
# print("orange" in mylist3)
# print("red"not in mylist3)
# print("list4" in mylist4)
# print("hands" in mylist2)
# print("type" not in mylist4)
# print("cheese" in mylist2)

# identity operator
# num = 24.0
# num1 = 24
# print(num is num1)
# num = 24
# num1 = "24"
# print(num is not num1)
# num = 35
# num1 = 35.0
# num2 = "35"
# print(num==num1)
# print(num is not num1)
# print(num==num2)
# print(num is not num2)
# print(num1==num2)
# print(num1 is not num2)
# == compares the value of the character
# is compares where the variables are stored in the memory
# is not compares
# bitwise operator
# decimal number to binary number
# decimal number is the number made up of ten digits
# (0,1,2,3,4,5,6,7,8,9)
# binary number only consists of 1 and 0
# 100 = 2^6 2^5 2^2 = 1100100
# 25 = 2^4 2^3 2^0 = 11001
# 36 = 2^5 2^2 = 100100
# 32 = 2^6 = 1000000
# 128 = 2^7 = 10000000
# 11 = 2^3 2^2 2^0 = 1101
# 31 = 2^4 2^3 2^2 2^1 2^0 = 11111
# 27 = 2^4 2^3 2^2 2^1 = 11110

# binary to decimal
# 111 = 2^0*1+2^1*1+2^2*1 = 13
# 001 = 2^0*1 = 1
# 011 = 2^0*1+2^1*1= 5
# 010 = 4
# 011111 = 1+4+8+16+32 = 61
# 1111011 = 1+4+0+16+32+64 = 117
# 010101 = 1+0+8+0+32 = 41
# 100001 = 1+64 = 65

# bitwise operators
# &, |, ~, <<, >>
# print(1&2)
# print(10&5)
# 1. 5&6 = 100 = 4
# 2. 7&12 = 100 = 4
# 3. 11&4 = 0 = 0
# 4. 3&3 = 11 = 3
# 5. 6&8 = 0 = 0
# 6. 16&4 = 100 = 5
# 7. 10&100 = 10 = 2
# print(5&6)
# print(7&12)
# print(11&4)
# print(3&3)
# print(6&8)
# print(16&4)
# print(10&100)

# 1. 5|6 = 111 = 7
# 2. 7|12 = 1111 = 15
# 3. 11|4 = 1111 = 15
# 4. 3|3 = 11 = 3
# 5. 6|8 = 1110 = 14
# 6. 16|4 10100 = 20
# 7. 10|100 = 1101110 = 110

# print(5|6)
# print(7|12)
# print(11|4)
# print(3|3)
# print(6|8)
# print(16|4)
# print(10|100)

# 1. ~5 = 010 = 2
# 2. ~4 = 011 = 3
# 3. ~10 = 0101 = 5
# 4. ~11 = 0100 = 4
# 5. ~17 = 01110 = 14
# 6. ~14 = 0001 = 1
# 7. ~8 = 0111 = 7
# 8. ~9 = 0110 = 6
# 9. ~7 = 000 = 0
# 10. ~18 = 01101 = 13 

# print(~5)
# print(~4)
# print(~10)
# print(~11)
# print(~17)
# print(~14)
# print(~8)
# print(~9)
# print(~7)
# print(~18)

# left shift operator <<
# 4<<2 10000 = 16
# 3<<1 110 = 6
# 5<<3 101000 = 40
# 2<<4 100000 = 32
# 7<<2 11100 = 28
# 8<<1 10000 = 16
# 16<<1 100000 = 32
# print(4<<2)
# print(3<<1)
# print(5<<3)
# print(2<<4)
# print(7<<2)
# print(8<<1)
# print(16<<1)

# right shift operator >>
# 18>>4 1 = 1
# 7>>2 1 = 1
# 17>>3 10 = 2
# 24>>3 11 = 3
# 19>>1 1001 = 9
# 20>>4 =  = 0
# 2>>4 = = 0
# 23>>6 = 0
# print(18>>4)
# print(7>>2)
# print(17>>3)
# print(24>>3)
# print(19>>1)
# print(20>>5)
# print(2>>4)
# print(23>>6)
