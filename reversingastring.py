#define a function to reverse a string without using the built-in reverse function or [::-1] slicing

def reversestring(string):
    #initialize the reversed string variable to an empty string
    reversedstring = ""
    #loop through the string in reverse order 
    #first -1 to get the last index of the string
    #then -1 to get the first index of the string
    #then -1 to get the reverse order of the string
    #the range function will start at the last index of the string and end at the first index of the string
    for i in range(len(string) - 1,-1, -1):
        #add each character to the reversed string variable
        reversedstring += string[i]
    #return the reversed string variable
    return reversedstring
#test cases 
if __name__ == "__main__":
    
    print(reversestring("Denley")) #output should be yelned
    print(reversestring("Python")) #output should be nohtyP
    