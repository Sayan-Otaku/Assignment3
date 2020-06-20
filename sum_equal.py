num1=float(input("Enter the value of num1: - "))
num2=float(input("Enter the value of num2: - "))
s=num1+num2
if s>5:
    print("Sum of {} and {} is greater than 5".format(num1,num2))
elif s<5:
    print("Sum of {} and {} is less than 5".format(num1,num2))
else:
    print("Sum of {} and {} is equal than 5".format(num1,num2))
    
