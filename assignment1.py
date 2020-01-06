#Jason Polanco
#aissgnment1.py
#9/21/19
# This program will display multiplication table for a number user inputs.
# Declare and initialize variables

def main():
    #intialize variables
    fName = ""
    enterNum = 0
    numSquar = 0
    sqRoot = 0
    total = 0
    totalSum = 0
    
    
    #import math module
    import math
    #Welcoming user to program
    
    #print asterisks above and below the welcome statement.
    
    print("**************************************************************")
    print("WELCOME TO THE WORLD'S GREATEST MULTPILCATION TABLE PROGRAM!")
    print("**************************************************************")

    # explain to user that this multpilcation program multiply up to 12.
    print("This program will only multiply up to 12")
    print()
    
    #prompt user for their name.
    Fname = input("May kindly have your name?:\n")

    #Display a message with their username and ask for a number
    print("Hello",Fname, "In the next line I will ask you for a number")
    
    #Accepting user input, stores the value
    enterNum = int(input("Please enter a number:\n"))
    
    #process the loop for multpilcation table, and prints the table
    for i in range(1, 13):
        total = (enterNum * i)
        totalSum += (enterNum * i) # equivalent to:  total = total + (enterNum * i)
        
        print(enterNum, "*", i, "=", total)
        print("so far, total sum is: ", totalSum)

    # Display message thanking user, you hope they know their multpilcation tables.
    print("\nThank you", fName,"for using my program I hope you know your",enterNum,"'s now")

    #calculations
    numSquar =  enterNum**2
    sqRoot = math.sqrt(numSquar)

    #Display a message, quick fun fact, displaying their respective number sqared and squared rooted.
    print("Quick fun fact- Did you know that your number squared is",numSquar," and the square root of that number is", sqRoot)



main()
              
    





    
