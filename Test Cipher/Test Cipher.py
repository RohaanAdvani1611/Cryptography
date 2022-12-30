import string    
import random

def generate_key(S):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    return ran

def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

if __name__ == '__main__':
    key = generate_key(10)
    f = open('pt.txt', 'r')
    msg = f.read()
    f.close()
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)
    print('Plain Text: ', msg.lower())
    print('Cipher Text: ', encrypted.upper())
    print('Decrypted Plain Text: ', decrypted.lower())
