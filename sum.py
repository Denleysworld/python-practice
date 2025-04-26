#define the function for counting the number of elements in a list
# and the sum of the elements in the list
def count(lst):
    #initialize the count variable to 0
    count = 0
    #loop through the list and increment the count variable
    for i in lst:
        #instead of adding the element to itself we are adding 1 to the count variable
        count += 1
    #return the count variable
    return count
#define the function for summing the elements in a list
def sum(lst):
    #initialize the sum variable to 0
    sum = 0
    #loop through the list and add each element to the sum variable
    for i in lst:
        #we are adding the element to the sum variable
        sum += i
    #return the sum variable
    return sum
#test cases
if __name__ == "__main__":
    lst = [1, 2, 3, 4, "Denley"]
    lst2 = [1, 2, 3, 4, 5]
    print("The number of elements in the list is: ", count(lst))#output should be 5
    print("The sum of the elements in the list is: ", sum(lst2)) #output should be 15
    
#Wasnt sure if we were supposed to the the total number of elements in the list or the sum of the elements in the list
# so I did both because in case a list had strings or other data types
