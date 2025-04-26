#Defining a function to reverse a string without using built-in functions or [::-1]
def reversestring(s):
    # Initialize an empty string to store the reversed string
    reversedstr = ""
    # Loop through the string in its current order
    for char in s:
        #Add each character to the beginning of the reversed string as you move along a string
        # the logic is if a string is "abc" then if you start adding the characters from the beginning
        #it will be "a" then "ba" then "cba"
        reversedstr =char+reversedstr
    return reversedstr
# Test the function
if __name__ == "__main__":
    test_string = "Denley"
    print(test_string)
    print(reversestring(test_string))

    