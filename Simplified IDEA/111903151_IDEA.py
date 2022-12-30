def generateRoundKeys(ck):
    rk = []
    for i in ck:
        rk.append(i)
    while len(rk) < 28:
        ck = ''.join(ck)
        ck = (ck*3)[len(ck)-4:2*len(ck)-4]
        ck = [(ck[i:i+4]) for i in range(0, len(ck), 4)]
        for i in ck:
            rk.append(i)
    rk = rk[:28]
    return rk

def decimalToBinary(n):
    return bin(n).replace("0b","")
    
def binaryToDecimal(n):
    return int(n,2)

def encRound(pt, rk):
    for i in range(len(pt)):
        pt[i] = binaryToDecimal(pt[i])
    for i in range(len(rk)):
        rk[i] = binaryToDecimal(rk[i])
    a = (pt[0] * rk[0]) % 17
    b = (pt[1] + rk[1]) % 16
    c = (pt[2] + rk[2]) % 16
    d = (pt[3] * rk[3]) % 17
    e = a ^ c
    f = b ^ d
    g = (e * rk[4]) % 17
    h = (f + g) % 16
    i = (h * rk[5]) % 17
    j = (i + g) % 16
    k = decimalToBinary(a ^ i)
    l = decimalToBinary(c ^ i)
    m = decimalToBinary(b ^ j)
    n = decimalToBinary(d ^ j)
    ct = [str(k),str(l),str(m),str(n)]
    for i in range(len(ct)):
        while(len(ct[i]) != 4):
            ct[i] = '0' + ct[i]
    return ct

def encLastRound(pt, rk):
    for i in range(len(pt)):
        pt[i] = binaryToDecimal(pt[i])
    for i in range(len(rk)):
        rk[i] = binaryToDecimal(rk[i])
    a = (pt[0] * rk[0]) % 17
    b = (pt[1] + rk[1]) % 16
    c = (pt[2] + rk[2]) % 16
    d = (pt[3] * rk[3]) % 17
    e = decimalToBinary(a)
    f = decimalToBinary(b)
    g = decimalToBinary(c)
    h = decimalToBinary(d)
    ct = [str(e),str(f),str(g),str(h)]
    for i in range(len(ct)):
        while(len(ct[i]) != 4):
            ct[i] = '0' + ct[i]
    return ct
    
def encrypt(inp, rk):
    x = 0
    r = 1
    for i in range(4):
        temp = []
        print('Round ' + str(r) + ' Input: ', inp)
        print('Round ' + str(r) + ' Key: ', rk[x:x+6])
        inp = encRound(inp, rk[x:x+6])
        print('Round ' + str(r) + ' Output: ', inp)
        print()
        if r != 4:
            tmp = inp[1]
            inp[1] = inp[2]
            inp[2] = tmp
        x += 6
        r += 1
    print('Round 4.5 Input: ', inp)
    print('Round 4.5 Key: ', rk[x:x+4])
    inp = encLastRound(inp, rk[x:x+4])
    print('Round 4.5 Output: ', inp)
    cipher = ''.join(inp)
    print()
    print('Cipher text: ', cipher)

p = '1001101100001010'
print('Plaintext: ', p)
print()
k = '10001111000111100101101000111100'
pt = [(p[i:i+4]) for i in range(0, len(p), 4)]
ck = [(k[i:i+4]) for i in range(0, len(k), 4)]
rk = generateRoundKeys(ck)
encrypt(pt, rk)