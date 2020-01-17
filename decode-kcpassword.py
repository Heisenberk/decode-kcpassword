#!/usr/bin/python3

import struct
import sys

# Function to decrypt the kcpassword
def decrypt_kcpassword():
    key = [125, 137, 82, 35, 210, 188, 221, 234, 163, 185, 31]
    length = len(key)
    f = open(sys.argv[1], "rb")
    byte = list(f.read())
    f.close()
    
    end = False
    kcpassword = []
    for i in range(len(byte)):
        if byte[i]^key[i%length] == 0 :
            end = True

        if end == False :
            kcpassword.append(str(chr(byte[i]^key[i%length])))
            
    print(''.join(map(str,kcpassword)))

# Function main
def main():
    if len(sys.argv) < 2 :
        print('usage : ./decode-kcpassword.py KCPASSWORD_PATH')
        exit()
    decrypt_kcpassword()

# Call to main
if __name__ == '__main__':
    main()


