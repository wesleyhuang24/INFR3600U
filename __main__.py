# Wesley Huang
# 100547950
#Jason Pinto 
#100592099
#Jinesh Shrirasa 
#100557027
#Alexander Yan
#100649393
import symmetric
import SHA512
import X509
import TripleDES
import CaesarCipher

if __name__ == "__main__":
    while (True):
        print("1. 3DES encryption")
        print("2. AES encryption")
        print("3. SHA512")
        print("4. X509 certification")
        print("5. Caesar Cipher")
        print("0. Exit")
        x = int(input("Enter the numbmer corresponding task: "))
        if (x == 1):
            TripleDES.TripleDES()
        elif (x == 2):
            symmetric.AES()
        elif (x == 3):
            SHA512.SHA512()
        elif (x == 4):
            X509.X509()
        elif (x == 5):
            CaesarCipher.CaesarCipher()
        elif (x == 0):
            break
    