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
def viewDirectory(folderName): #Opens folder directory and list csv contents.
    os.chdir(os.getcwd() + "\\src\\fileDirectories\\" + folderName)
    temp = os.listdir()
    arr = []

    for i in temp: #Filters array to .csv files.
        if(i[len(i)- 4:len(i)] == ".csv"):
            arr.append(i)

    if(arr): #Shows file contents if there is at least a file in a directory, otherwise go back.
        print("\nThe following CSV files are in "+ folderName + "'s directory, select the CSV file you want to open.")
        for i in range(len(arr)):
            print(str(i + 1) + ": " + arr[i])
        userInput = input("\nEnter the CSV file to open or type 'back*' to back: (DON'T INCLUDE .CSV TAG) ")
    else:
        print("\nERROR: There is nothing in "+ folderName +"'s directory, returning to previous page...")
        userInput = "back*"

    if(userInput != "back*"):
        readData(userInput,folderName)
    else:
        os.chdir('..\\..\\..')
        openUsers()

def openUsers(): #Lists users from user credentials text file for user to select to open and creates users folder if it doesn't exist yet.
    try:
        userInput = ""
        with open('src/logininfo/loginCredentials.txt','r') as txt_file:
            csv_reader = csv.reader(txt_file)
            while(userInput.lower() != "back*"):
                print("==========================\nThe following users have their own folders. (USERS ARE CASE-SENSITIVE!)")
                print("*GUEST*") #Checks if the guest folder exists.
                os.chdir(os.getcwd() + "\\src\\fileDirectories")
                if(not os.path.exists(os.getcwd()+ "\\GUEST_USER")):
                    os.makedirs(os.getcwd() + "\\GUEST_USER")
                os.chdir('..\\..')
                
                for line in csv_reader:
                    username = line[0].split(":")[0]
                    print(username) #Splits string to only have username.
                    os.chdir(os.getcwd() + "\\src\\fileDirectories")
                    if(not os.path.exists(os.getcwd() + "\\" +username)): #Creates user folder if it doesn't exists.
                        os.makedirs(os.getcwd() + "\\" +username)         
                    os.chdir('..\\..')
                txt_file.seek(0)

                userInput = input("\nEnter the user you're opening or type 'back*' to go back: ")
                if(userInput.lower() == "back*"): 
                    return
                elif(userInput.upper() != "GUEST"):
                    for line in csv_reader:
                        if(userInput == line[0].split(":")[0]):
                            return viewDirectory(userInput)
                    print("\nERROR: User doesn't exist, please try again...")
                elif(userInput.upper() == "GUEST"): 
                    return viewDirectory("GUEST_USER")
                txt_file.seek(0)
    except FileNotFoundError:
        print("ERROR: UNABLE TO OPEN USERS BECAUSE CREDENTIALS FILE OR FOLDER DOESN'T EXIST.")
        openUsers()    
    except:
        print("ERROR: AN ERROR HAS OCCURRED.")
        openUsers()

def readData(fileLocation,folderName = ""): #Reads CSV files and show a bar graph.
    arr = [0 for i in range(0,16)] #FOR PLOTTING
    try:
        with open(fileLocation + '.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            names = csv_file.readline().split(",")

            print("\n-="+fileLocation+".csv CONTENTS=-")
            for line in csv_reader:
                for col in range(0,16):
                    print(line[col], end = " ")
                    arr[col] += int(line[col])  
                print()

        print("\n-=SUM OF RESULTS=-")
        for i in arr:
            print(i, end="  ")
        print()
    
        plt.bar(names,arr)
        plt.plot()
        plt.xlabel("Indexes of Sum of Dices")
        plt.ylabel("Frequency")
        plt.title("Results Table For: " + fileLocation+".csv")
        plt.show()
        os.chdir('..\\..\\..')
        viewDirectory(folderName)
    except FileNotFoundError:
        print("\nERROR: CSV FILE DOESN'T EXIST.")
        os.chdir('..\\..\\..')
        viewDirectory(folderName)
    except ValueError:
        print("\nERROR: THIS FILE IS NOT VALID FOR GRAPHING.")
        os.chdir('..\\..\\..')
        viewDirectory(folderName)
    except:
        print("\nERROR: AN ERROR OCCURED.")
        os.chdir('..\\..\\..')
        viewDirectory(folderName)


#MAIN PROGRAM
userInput = ""
print("**************************")
print("****CSV DISPLAY READER****")
print("**************************\n")
print("Developed by Michael Delgado")
print("Github Link: github.com/md37971")
print("Separate Python program that is an add-on to the DiceRollGUI project in java.\n")
print("WARNING: DO NOT MODIFY THE FILE LOCATION OF THIS PYTHON FILE. THIS WILL RESULT IN FILE ERRORS!")

while(userInput.lower() != "exit"):
    if(userInput.lower() == "exit"): break
    openUsers()
    userInput = input("Press 'EXIT' to exit the program or any key to continue: ")