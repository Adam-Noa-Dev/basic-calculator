
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter second Number:"))
operation = input("Enter the mathematical operator:")

if(operation) == "+" :
    result = num1 + num2
elif(operation) == "-" :
    result = num1 - num2
elif(operation) == "*" :
    result = num1 * num2
elif(operation) == "/" :
    result = num1/num2
else:
    
  print(" ERROR:Mathematical Operator Not Found")

print(result)
