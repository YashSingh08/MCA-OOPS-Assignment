# this module helps users to write into a file
def write(filename):
    print("Write to the file: ")
    text = input()
    file = open(filename, "w")
    file.write(text)
    file.close()
    return text
