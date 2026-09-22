from calculator import  add,subtract,multiply,divide

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation=input("Enter a Operation to perform,1:add,2:subtract,3:multiply,4:divide: ")


if operation == '1':
    print("Addition: ", add(num1,num2))
elif operation == '2':  
    print("Subtraction: ", subtract(num1,num2))
elif operation == '3':
    print("Multiplication: ", multiply(num1,num2))
elif operation == '4':
    print("Division: ", divide(num1,num2))
else:
    print("Invalid operation selected.")
