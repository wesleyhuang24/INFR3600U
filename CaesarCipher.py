#Jinesh Shrirasa 
#100557027
# Caesar Cipher

def CaesarCipher():
    MAX_KEY_SIZE = 26
    
     
    def getMode():
    
         while True:
    
             print('Do you wish to encrypt or decrypt a message?')
    
             mode = input().lower()
    
             if mode in 'encrypt e decrypt d'.split():
    
                 return mode
    
             else:
    
                 print('Enter either "encrypt" or "e" or "decrypt" or "d".')
    
        
    def getMessage():
        
        print('Enter your message:')
        
        return input()
        
        
        
    def getKey():
        
        key = 0
        
        while True:
        
                 print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        
                 key = int(input())
        
                 if (key >= 1 and key <= MAX_KEY_SIZE):
        
                     return key
        
        
        
    def getTranslatedMessage(mode, message, key):
        
        if mode[0] == 'd':
        
            key = -key
        
        translated = ''
        
        
        
        for symbol in message:
        
            if symbol.isalpha():
        
                num = ord(symbol)
        
                num += key
        
        
        
                if symbol.isupper():
        
                    if num > ord('Z'):
        
                        num -= 26
        
                    elif num < ord('A'):
        
                        num += 26
        
                elif symbol.islower():
        
                    if num > ord('z'):
        
                        num -= 26
        
                    elif num < ord('a'):
        
                        num += 26
        
        
        
                translated += chr(num)
        
            else:
        
                translated += symbol
        
        return translated
        
        
        
    mode = getMode()
    
    message = getMessage()
    
    if mode[0] != 'b':
        key = getKey()
    print('Your translated text is:')
    
    if mode[0] != 'b':
    
        print(getTranslatedMessage(mode, message, key))
    
    else:
    
        for key in range(1, MAX_KEY_SIZE + 1):
    
            print(key, getTranslatedMessage('decrypt', message, key))
            
    print("Using the information the user has provided, this program has encrypted or decrypted the message by using the given key value using the Caesar Cipher alogrithm. It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on")        
    
    while True:
        i = input("Would you like to see a more indepth breakdown?: (y/n) :")
        if i == "y": 
            print("The algorithm is named after Julius Caesar, who used this as a form to communicate with his generals.")
            print("This algorithm is one of the earliest known ciphers, this requires the key in order for the message to be ecrypted and decrypted.") 
            print("The key gives the value for the message to be decrypted. For Example, if we use key 1 to encrypt 'abc' then we shift 1 to the right of the alphabet, which returns 'bcd'.") 
            print("Decrypting the same message 'abc' by using the key value as 1 would give us 'zab'.")
            print("This algorithm is easy to break as if we try all 26 possibilities we can find the message that has been encrypted, this is know as using brute force ")
            break
        elif i == "n":
            break
        else:
            print("")
            print("Enter either y/n")       
            