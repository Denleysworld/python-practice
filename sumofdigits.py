#define a function to calculate the sum of the digits of a number
def sumofdigits(n):
    #initialize the sum variable to 0
    sum = 0
    #loop through the digits of the number
    for digit in str(n):
        #add the digit to the sum variable
        sum += int(digit)
    #return the sum variable
    return sum
#test cases
if __name__ == "__main__":

    print("The sum of the digits of 12345 is", sumofdigits(1234567890)) #output should be 45
    print("The sum of the digits of 987654321 is", sumofdigits(987654321)) #output should be 45
    print("The sum of the digits of 0 is", sumofdigits(0)) #output should be 0