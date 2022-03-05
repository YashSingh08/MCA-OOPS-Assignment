# this module helps user to encrypt the data which is already in the file
def encrypt(filename):
    file = open(filename, "r")
    text = file.read()
    encryption = ("")
    for bit in range(len(text)):
        if ord(text[bit]) >= 97 and ord(text[bit]) <= 122:
            encryption += chr(97+25-(ord(text[bit])-97))
        elif ord(text[bit]) >= 65 and ord(text[bit]) <= 87:
            encryption += chr(ord(text[bit])+3)
        elif ord(text[bit]) >= 65 and ord(text[bit]) <= 87:
            encryption += chr(ord(text[bit])+3)
        elif ord(text[bit]) >= 48 and ord(text[bit]) <= 57:
            encryption += chr(48+9-(ord(text[bit])-48))
        else:
            pass
    file.close()
    file = open(filename, "w")
    file.write(encryption)
    file.close()
