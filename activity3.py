# function to calculate factorial
def factorial(n):
    if n == 0 or n == 1: #base case: 0! and 1! are booth 1
        return 1
    else:
        return n * factorial(n-1) # recursive call
    
# input from user
num = int(input("Enter a number: "))

# check if the number is negative
if num < 0:
    print("factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")