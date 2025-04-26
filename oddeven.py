#checks whether a number is odd or even
def odd_even(num):
    #check if the number is even
    if num % 2 == 0:
        return "Even"
    #if the number is not even then it is odd
    else:
        return "Odd"
#test cases
if __name__ == "__main__":
    #test cases
    print(odd_even(135790)) #output should be Even
    print(odd_even(246801)) #output should be Odd
   