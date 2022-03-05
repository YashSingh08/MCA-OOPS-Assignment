# importing the modules for each features
import menu 
import read
import write
import encrypt
import decrypt
import exit

# errorHandler() function will be execute if user entered a wrong input
def errorHandler():
    return "Invalid input !!!\nChoose again ."

# main program starts from here with users input for the filename
print("Enter the filename: ")
filename = input()

# it checks the condition if program is entering in the loop
condition = True
while(condition):
    menu.menu()
    choice = menu.getChoice() # getChoice() function get called from the menu module
    if choice == 1:
        read.read(filename) # read() function get called from the read module to read a file
        condition = exit.exit() # exit() function asks whether user want to exit or not

    # if user choose to exit then the program gets terminated otherwise it restarts the loop

    elif choice == 2:
        write.write(filename) # write() function get called from the write module to write in the file
        condition = exit.exit()
    elif choice == 3:
        encrypt.encrypt(filename) # encrypt() function from encrypt module encrypts the file
        condition = exit.exit()
    elif choice == 4:
        decrypt.decrypt(filename) # decrypt() function from decrypt module does decrypts to the file
        condition = exit.exit()
    else:
        print(errorHandler()) # if user choose any other option from the menu then errorHandler() function executes
