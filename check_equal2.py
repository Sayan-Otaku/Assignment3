num1=float(input("Enter the value of num1: - "))
num2=float(input("Enter the value of num2: - "))
num3=float(input("Enter the value of num3: - "))
if num1==num2==num3:
    print("All the numbers are equal")
elif num1==num2 or num1==num3 or num2==num3:
    print("2 numbers are equal")
else:
    print("None of the numbers are equal")
