# these are the option to be chosen by the users
def menu():
    print('''
    1. Read a file
    2. Write a file
    3. Encrypt a file
    4. Decrypt a file
''')

def getChoice():
    choice = int(input("Enter your choice: "))
    return choice
