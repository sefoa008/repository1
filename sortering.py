"""
liste = [5, 7, 4, 6, 9, 8]
liste.sort()

print(liste)
"""
"""
liste2 = [3, 1, 8, 5, 9]
lengde = len(liste2)

for i in range(lengde):
    for j in range(0, lengde - i - 1):
        if liste2[j] > liste2[j + 1]:
            liste2[j], liste2[j + 1] = liste2[j + 1], liste2[j]
                
 
print("Sortert liste:")
for i in range(len(liste2)):
    print(liste2[i])

"""

def bubbleSort( theSeq ):   #Defines a function bubbleSort that accepts a parameter theSeq. The code does not output anything.
    n = len( theSeq )   #Gets the length of the array and assigns the value to a variable n. The code does not output anything

    for i in range( n - 1 ) :   #Starts a for loop that runs the bubble sort algorithm (n – 1) times. This is the outer loop. The code does not output anything
        flag = 0    #Defines a flag variable that will be used to determine if a swap has occurred or not. This is for optimization purposes. The code does not output anything

        for j in range(n - 1) : #Starts the inner loop that compares all the values in the list from the first to the last one. The code does not output anything.
            
            if theSeq[j] > theSeq[j + 1] :  #Uses the if statement to check if the value on the left-hand side is greater than the one on the immediate right side. The code does not output anything.
                tmp = theSeq[j] #Assigns the value of theSeq[j] to a temporal variable tmp if the condition evaluates to true. The code does not output anything
                theSeq[j] = theSeq[j + 1]   #The value of theSeq[j + 1] is assigned to the position of theSeq[j]. The code does not output anything
                theSeq[j + 1] = tmp #The value of the variable tmp is assigned to position theSeq[j + 1]. The code does not output anything
                flag = 1   #The flag variable is assigned the value 1 to indicate that a swap has taken place. The code does not output anything


        if flag == 0:   #Uses an if statement to check if the value of the variable flag is 0. The code does not output anything
            break   #If the value is 0, then we call the break statement that steps out of the inner loop.

    return theSeq   #Returns the value of theSeq after it has been sorted. The code outputs the sorted list.

el = [21,6,9,33,3]  #Defines a variable el that contains a list of random numbers. The code does not output anything.

result = bubbleSort(el) #Assigns the value of the function bubbleSort to a variable result.

print (result)  #Prints the value of the variable result.

"""

theSeq = [21,6,9,33,3]  #Defines a variable el that contains a list of random numbers. The code does not output anything.
n = len( theSeq )   #Gets the length of the array and assigns the value to a variable n. The code does not output anything
#def bubbleSort( theSeq ):   #Defines a function bubbleSort that accepts a parameter theSeq. The code does not output anything.


for i in range( n - 1 ) :   #Starts a for loop that runs the bubble sort algorithm (n – 1) times. This is the outer loop. The code does not output anything
    flag = 0    #Defines a flag variable that will be used to determine if a swap has occurred or not. This is for optimization purposes. The code does not output anything

    for j in range(n - 1) : #Starts the inner loop that compares all the values in the list from the first to the last one. The code does not output anything.
        
        if theSeq[j] > theSeq[j + 1] :  #Uses the if statement to check if the value on the left-hand side is greater than the one on the immediate right side. The code does not output anything.
            tmp = theSeq[j] #Assigns the value of theSeq[j] to a temporal variable tmp if the condition evaluates to true. The code does not output anything
            theSeq[j] = theSeq[j + 1]   #The value of theSeq[j + 1] is assigned to the position of theSeq[j]. The code does not output anything
            theSeq[j + 1] = tmp #The value of the variable tmp is assigned to position theSeq[j + 1]. The code does not output anything
            flag = 1   #The flag variable is assigned the value 1 to indicate that a swap has taken place. The code does not output anything


        if flag == 0:   #Uses an if statement to check if the value of the variable flag is 0. The code does not output anything
            break   #If the value is 0, then we call the break statement that steps out of the inner loop.

    #return theSeq   #Returns the value of theSeq after it has been sorted. The code outputs the sorted list.



#result = bubbleSort(theSeq) #Assigns the value of the function bubbleSort to a variable result.

print (theSeq)  #Prints the value of the variable result.

"""