#greatest of three numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a > b and a > c:
    print("The greatest number is:", a)
elif b > a and b > c:
    print("The greatest number is:", b)
elif c > a and c > b:
    print("The greatest number is:", c)
else:
    print("All numbers are equal.")
