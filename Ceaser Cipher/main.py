def ceaser_encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if (char.isupper()): result += chr((ord(char) + s - 65) % 26 + 65)
            else: result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result
    
def ceaser_decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if (char.isupper()): result += chr((ord(char) - s - 65) % 26 + 65)
            else: result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result
    
if __name__ == '__main__':
    f = open('pt.txt', 'r')
    text = f.read()
    f.close()
    sh = 3
    enc = ceaser_encrypt(text, sh)
    print('ENC: ', enc)
    dec = ceaser_decrypt(enc, sh)
    print('DEC: ',dec)