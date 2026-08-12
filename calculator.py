num1 = int(input("Enter a first number: "))

operator = input("Enter operator(+, -, *, /):")
num2 = int(input("Enter a second number: "))

# operator = input("Enter operator(+, -, *, /):")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2!=0:
     result = num1 / num2
    else:
       result = "Cannot divided by zero"
else:
   result = "Invalid operator"

print("Result:", result)