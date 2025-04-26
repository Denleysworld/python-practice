#define a function to calculate the factorial of a number recursively
def factorial(n):
    #check if the number is less than 0 because factorial is not defined for negative numbers
    if n < 0:
        return "Invalid input"
    #check if the number is 0 or 1 because factorial of 0 and 1 is 1
    elif n == 0 or n == 1:
        return 1
    #if the number is greater than 1 then call the function recursively
    else:
        return n * factorial(n - 1)
#test cases
if __name__ == "__main__":
    #test cases
    print("The factorial of 5 is ", factorial(5)) #output should be 120
    print("The factorial of 0 is ", factorial(0)) #output should be 1
    print("The factorial of -5 is ", factorial(-5)) #output should be Invalid input
