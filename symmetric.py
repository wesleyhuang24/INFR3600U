# Wesley Huang
# 100547950
# Symmetric Encryption in Python


#import to make paading work
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def AES():
    #the messeage that will be encrypted with AES
    test = (input("Enter plaintext: "))
    a = test
    #test = "a super duper secret message"
    test = test.encode()
    
    #if lenght of message is not 16 use padder
    if (len(test) % 16 != 0):
        padder = padding.PKCS7(128).padder()
        padded = padder.update(test)
        padded
        padded += padder.finalize()
    
    else: 
        padded = test
    
    print("your plaintext before encryption: ", a)
    #AES encryption  
    backend = default_backend()
    key = os.urandom(32)
    iv = os.urandom(16)
    print("Your key is: " + str(key))
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded) + encryptor.finalize()
    print("encrypted message: " + str(ct))
    decryptor = cipher.decryptor()
    ct = decryptor.update(ct) + decryptor.finalize()
    
    #if length of message is not 16 use the unpadder
    if (len(test) != 16):
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded)
        data
        data += unpadder.finalize()
        print("the decrypted message: ", data)
    
    #if not print 
    else:
       print("the decrypted message: ",ct)
    
    print("AES is an encryption a symmetric block cipher developed by the national institute of standards and technology(NIST) is the successor to DES. ")
    x = (int(input("For more information about AES enter 1: ")))
    if (x == 1):
        y=3 #abitrary y to start loop
        while not(y== 0 or y== 1):
            y = (int(input("Enter 0 for information about encryption and 1 for decryption: ")))
            if (y == 0):
                print("To encrypt AES, it will take plaintext and a key which run through the algorithm and output a ciphertext. AES takes the plaintext and splits it into 128 bit blocks. Each block is then XOR’d together with an expanded key that has the same bits as the block. The block is then run through N number of rounds depending on key size. Each round has four transformations (substitutions, transposition, mixColumns and XOR with key) excluding the final round which only has substitution, transposition and XOR. Substitution uses a S-box to perform a byte-to-byte substitution of the block. The transposition step shifts the bytes in each row by a certain offset. The mixColumns function takes four bytes as input and outputs new four bytes. The final step XOR is where the block is XOR’d and the output is then run through these steps for N number of times expect the final round does substitution, transposition and XOR. After the block is finished this process will be repeated until all blocks are finished.")
                n = int(input("Would you like to restart? Enter 0 for No or 1 for Yes"))
                if(n == 1):
                    y = 2
                    continue
                else:
                    break
            elif (y == 1):
                print("Decrypting AES is not the same as encrypting. To decrypt the ciphertext we will be using the same key but in the rounds instead of substitutions, transposition and mixColumns we will be using inverse substitutions, transposition and mixColumns. Inverse substitution affects the contents of the bytes but doesn’t alter the byte sequence and doesn’t depend on it perform the transformation. Inverse transposition affects the sequence of bytes but not the byte content and doesn’t depend on it to perform its transformation. So the ciphertext is entered the key is XOR’d in then we start the rounds. Each round will four transformations inverse substitution, transposition, mixColumns and XOR. Then at the final round only three transformations inverse substitution, transposition and XOR is carried out and the plaintext will be outputted. It will repeat this process until the whole plaintext is completed. ")
                n = int(input("Would you like to restart? Enter 0 for No or 1 for Yes: "))
                if(n == 1):
                    y = 2
                    continue
                else:
                    break
            else:
                print("Invalid input, please re-enter 0 or 1")
                
        