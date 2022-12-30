import math
import time

def alphabet_position(text):
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    new_text = text.lower()
    for i in new_text:
        if i in dict:
            new_text = new_text.replace(i, dict[i])
    return new_text

def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp

def RSA(p, q, msg):
    n = p*q
    
    start = time.time()
    e = 2
    phi = (p-1)*(q-1)
    
    while (e < phi):
        # e must be co-prime to phi and smaller than phi.
    	if(gcd(e, phi) == 1):
    		break
    	else:
    		e = e+1
    
    # Choosing d such that it satisfies d*e = 1 + k * totient
    k = 2
    d = (1 + (k*phi))/e
    end = time.time()
    t1 = end - start
    
    # Encryption c = (msg ^ e) % n
    start = time.time()
    c = math.fmod(pow(msg, e), n)
    end = time.time()
    t2 = end - start
    
    # Decryption m = (c ^ d) % n
    start = time.time()
    m = math.fmod(pow(c, d), n)
    end = time.time()
    t3 = end - start
    return c, m, t1, t2, t3

msg = ['HI', 'HELLO', 'BYE', 'WHAT', 'A', 'YELLOW', 'TRACKER', 'PENTAGON', 'DECATHALON']
for i in range(len(msg)):
    msg[i] = alphabet_position(msg[i])
    msg[i] = int(msg[i])
for i in msg:
    c, m, t1, t2, t3 = RSA(3, 7, i)
    print('Cipher: '+str(c)+' Dec Plain: '+str(m)+' Key Gen Time: '+str(t1)+' Enc Time: '+str(t2)+' Dec Time: '+str(t3))
