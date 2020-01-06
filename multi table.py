#Jason Polanco
#12/15/19
#A program that will print the multipiclation table for a number the user inputs
# Must be multiplied up to 12

#def main
import math
def main():

    #declare and intialize variables
    uName= ""

    uNum=0

    #display output example
    print("\n*****************************************************")
    print("\nWELCOME TO MY MULTPILCATION TABLE PROGRAM!")
    print("\n*****************************************************")
        

    #prompt user for name
    uName= input("First, enter your name: ")



    #Display purpose of the  program to user
    print("\nHi,",uName,"!","I am going to ask you for a number and show you all the multiples of that number up to 12")



    #Prompt user for a number

    uNum= int(input("\nWhat number would you like to see multiples of: "))

    print("\System Volume Informationn",uNum,"is a great number. Below is your",uNum,"'s multiplication table: ")

    # Selected user number must be used in for loop
    for i in range(13):
        
        multNum=(i *uNum)
        print(uNum,"*",i,"=",multNum)

    #Thank user for using program, and display user selected number
    print("\nThank you",uName,"for using my program. I hope you know your",uNum,"'s now!")

    # Display user number squared and the root of selected number.
    print("\nQuick fun fact- Did you know that you number squared is", pow(uNum,2), "and the square root of", uNum,"is", round(math.sqrt(pow(uNum,2)),2),"!")

main()
