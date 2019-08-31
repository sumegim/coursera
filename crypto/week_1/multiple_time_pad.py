import sys
import random

MSGS =  ["secret", "secret2"]

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def encrypt(key, msg):
    c = strxor(key, msg)
    print (c.encode('hex'))
    return c

def main():
    key = "qwert"
    ciphertexts = [encrypt(key, msg) for msg in MSGS]
    print(ciphertexts)

main()
