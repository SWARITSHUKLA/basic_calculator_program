#simple calculator
a = float(input("Enter the first number: "))
operator = input("Enter an operator +,-,*,/,:")
b = float(input("Enter the second number:"))
if operator == "+":
    print(f"The value of {a}+{b} is:",a+b)
elif operator == "-":
    print(f"The value of {a}-{b} is:", a-b)
elif operator == "*": 
    print(f"The value of {a}*{b} is:",a*b)
elif operator == "/":
    print(f"The value of {a}/{b} is:",a/b)
else:
    print(f"The operator \"{operator}\" is not valid!!")