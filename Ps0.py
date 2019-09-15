#A program that accpet 2 number from d user and calculate the power
import math
x = int(input("Enter the first number: "))
y = int(input("Enter the Second number: "))
power = x**y
print(x, "raised to the power of ",y, "is ",power)
print("log(base 2) of",x, "is: ",math.log2(x))