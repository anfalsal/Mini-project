# In this exercise, I will program a simple calculator that performs the following operations:
# addition, subtraction, multiplication, and division
num1 = float(input("enter the first number: "))
p = input()
num2 = float(input(" enter the second number: "))

def add(x , y):
    return x + y
def sub(x , y):
    return x - y
def mul(x , y):
    return x * y
def div(x , y ):
    return x/y

if p == "+":
    print(add(num1,num2))
elif p == "-":
    print(sub( num1, num2))
elif p == "*":
    print(mul(num1, num2))
elif p == "/":
    print(div(num1, num2))

