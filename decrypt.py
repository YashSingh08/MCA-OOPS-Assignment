# this module helps user to decrypt the data which is encrypted already in the file
def decrypt(filename):
    file = open(filename, "r")
    text = file.read()
    decryption = ("")
    for bit in range(len(text)):
        if ord(text[bit]) >= 97 and ord(text[bit]) <= 122:
            decryption += chr(97+25-(ord(text[bit])-97))
        elif ord(text[bit]) >= 68 and ord(text[bit]) <= 90:
            decryption += chr(ord(text[bit])-3)
        elif ord(text[bit]) >= 65 and ord(text[bit]) <= 67:
            decryption += chr(88+(ord(text[bit])-65))
        elif ord(text[bit]) >= 48 and ord(text[bit]) <= 57:
            decryption += chr(48+9-(ord(text[bit])-48))
        else:
            pass
    file.close()
    file = open(filename, "w")
    file.write(decryption)
    file.close()
