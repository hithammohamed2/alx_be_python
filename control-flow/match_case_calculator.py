num1 = int(input("Enter the fist number:"))
num2 = int(input("Enter the second number:"))
operation = str(input("Choose the operation (+, -, *, /):"))
if operation == "+":
    print(num1 + num2 )
    
elif operation == "-":
    print(num1 - num2 )
    
elif operation == "*":
    print(num1 * num2 )
    
elif operation == "/":
    if num2 != 0:
      print(num1 / num2 )
    else:
        print("cannot divide by zero!")
    
else:
    print("invalid input")
    exit


      
