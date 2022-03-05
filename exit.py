# this module helps users to exit from the program
def exit():
    print("Do you want to exit? (y/n)")
    choice = input()
    if choice == "y" or choice == "Y":
        return False
    else:
        return True
