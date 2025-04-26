#define a functtion calculate the factorial of a number
def factorial(n):
    #initialize the factorial variable to 1
    factorial = 1
    #loop through the range of numbers from 1 to n+1
    for i in range(1, n + 1):
        #multiply the factorial variable by the current number
        factorial *= i
    #return the factorial variable
    return factorial
#test cases
if __name__ == "__main__":
    #test cases
    print("The factorial of 5 is: ", factorial(5)) #output should be 120


  