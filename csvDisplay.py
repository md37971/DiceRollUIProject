import csv
import os
from matplotlib import pyplot as plt
"""
Author: Michael Delgado
github.com/md37971

*Description*
Python file to display CSV using madplotlib library.
"""

#METHODS
def viewDirectory(folderName):
    os.chdir(os.getcwd() + "\\src\\fileDirectories\\" + folderName)
    arr = os.listdir()

    print("\nThe following files are in the directory, select the CSV file you want to open.")
    for i in range(len(arr)):
        print(str(i + 1) + ": " + arr[i])
    
    userInput = input("Enter the CSV file to open or type 'back*' to back: (DON'T INCLUDE .CSV TAG) ")
    if(userInput != "back*"):
        readData(userInput)
    else:
        os.chdir('..\\..\\..')
        openUsers()

def openUsers():
    try:
        userInput = ""
        bool = False
        with open('src/logininfo/loginCredentials.txt','r') as txt_file:
            csv_reader = csv.reader(txt_file)
            while(userInput.lower() != "back*" and not bool):
                print("The following users have their own folders:")
                for line in csv_reader:
                    print(line[0].split(":")[0])
                txt_file.seek(0)
                print("GUEST")

                userInput = input("\nEnter the user you're opening or 'back*' to go back: ")
                if(userInput.lower() == "back*"): break
                if(userInput.upper() != "GUEST"):
                    for line in csv_reader:
                        if(userInput.lower() == line[0].split(":")[0]):
                            bool = True
                            viewDirectory(userInput)
                    if(not bool):
                        print("\nUser doesn't exist, please try again...")
                elif(userInput.upper() == "GUEST"):
                    viewDirectory("GUEST_USER")
                txt_file.seek(0)
    except FileNotFoundError:
        print("UNABLE TO OPEN USERS BECAUSE CREDENTIALS FILE DOESN'T EXIST.")
    except:
        print("AN ERROR HAS OCCURED.")

def readData(fileLocation):
    arr = [0 for i in range(0,16)] #FOR PLOTTING
    try:
        with open(fileLocation + '.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            names = csv_file.readline().split(",")

            print("\n")
            for line in csv_reader:
                for col in range(0,16):
                    print(line[col], end = " ")
                    arr[col] += int(line[col])  
                print()


        print("\nTHE ARRAY")
        for i in arr:
            print(i, end=" ")
        print()
            
        plt.bar(names,arr)
        plt.plot()
        plt.xlabel("Indexes of Sum of Dices")
        plt.ylabel("Frequency")
        plt.title("Results Table For: " + fileLocation+".csv")
        plt.show()
        os.chdir('..\\..\\..')
    except FileNotFoundError:
        print("THERE WAS AN ERROR OBTAINING THE FILE...")
        os.chdir('..\\..\\..')
    except ValueError:
        print("THIS FILE IS NOT VALID FOR GRAPHING.")
        os.chdir('..\\..\\..')
    except:
        print("AN ERROR OCCURED.")
        os.chdir('..\\..\\..')


#MAIN PROGRAM
userInput = ""

print("**************************")
print("****CSV DISPLAY READER****")
print("**************************\n")
print("Developed by Michael Delgado")
print("Github Link: github.com/md37971")
print("Separate python program that is an add-on to Dice Roll GUI in java.\n")

while(userInput.lower() != "exit"):
    if(userInput.lower() == "exit"): break
    openUsers()
    userInput = input("Press 'EXIT' to exit the program or any key to continue: ")
    print("\n")