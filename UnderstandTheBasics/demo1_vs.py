"""
Learn about variables, data types (integers, floats, strings, booleans), and basic operations (+, -, *, /, //, %, **).
Explore how to print output using the print() function.
Familiarize yourself with basic input using the input() function.
"""

number = int(input("Enter a number: "))

factorial = int(number)

if(number <= 0):
    
    print("Factorial cannot be computed")

else:
    for x in range(1, number):

        factorial = factorial * x

    print("The factorial of your input is: " + str(factorial))