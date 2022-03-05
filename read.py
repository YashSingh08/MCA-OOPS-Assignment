# this module helps user to read a file
def read(filename):
    file = open(filename, "r")
    data = file.read()
    print(data)
    file.close()
    return data
