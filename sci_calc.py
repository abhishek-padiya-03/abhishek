#FOR OPERATORS ENTER THE FOLLOWING

#you can use upper or lower case for operations    
#   +     for addition
#   -     for subtraction
#   /     for division
#   *     for multiplication
#   ^     for power
#   r     for root
#   %     for modulus
#   pie   for Pie
#   e     for E
#   sin   for sin (trig)
#   cos   for cos (trig)
#   tan   for tan (trig)
#   !     for factorial 
#   ln    for ln (natural log)

import math
firstNumber = float(input())
op = input().lower()
secondNumber = float(input())

if op == "+":
    print (firstNumber, "+", secondNumber, "=", firstNumber + secondNumber )
elif op == "-": 
    print (firstNumber, "-", secondNumber, "=", firstNumber - secondNumber )
elif op == "*":
    print (firstNumber, "*", secondNumber, "=", firstNumber * secondNumber )
elif op == "/":
    print (firstNumber, "/", secondNumber, "=", firstNumber / secondNumber )
elif op == "^":
    print (firstNumber, "^", secondNumber, "=", firstNumber ** secondNumber )
elif op == "r":
    print (firstNumber, "root", secondNumber, "=", secondNumber ** (1 / firstNumber) )
elif op == "%":
    print (firstNumber, "%", secondNumber, "=", firstNumber % secondNumber )
#factorial
elif op == "!":
    theNumber = firstNumber = secondNumber 
    secondNumber = 1
    while firstNumber > 1:
        secondNumber *= firstNumber 
        firstNumber = firstNumber - 1  
    print ("n!(", theNumber, ")=", secondNumber )
elif op == "sin":
    print ("sin(", secondNumber, ")=", math.sin(secondNumber ))
elif op == "cos":
    print ("cos(", secondNumber, ")=", math.cos
    (secondNumber ))
elif op == "tan":
    print ("tan(", secondNumber, ")=", math.tan(secondNumber ))
elif op == "pie" or op == "pi":
    print ("Pie =", math.pi)
elif op == "e":
    print = ("E =", math.e)
elif op == "ln":
    print ("ln(", secondNumber , ")= ", math.log(secondNumber))
else:
    print ("incorrect operator")
