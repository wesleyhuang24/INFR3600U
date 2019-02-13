#Alexander Yan
#100649393

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def TripleDES():
    backend = default_backend()
    key = os.urandom(16)
    iv = os.urandom(8)
    
    user_input = input('Please enter a message: ')
    
    cipher = Cipher(algorithms.TripleDES(key), modes.OFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    user_input_byt = str.encode(user_input)
    ct = encryptor.update(user_input_byt) + encryptor.finalize()
    
    print('The 3DES key is {}'.format(ct))
    
    decryptor = cipher.decryptor()
    answer = decryptor.update(ct) + decryptor.finalize()
    print('The decrypted message: {}'.format(answer))
    
    a = input('Would you like to know more about 3DES? (yes/no) ')
    if a == 'yes':
        print('Triple DES (Data Encryption Standard), sometimes referred to as 3DES, is a block cipher standardized by NIST. Triple DES has known crypto-analytic flaws, however none of them currently enable a practical attack. Nonetheless, Triple DES is not recommended for new applications because it is incredibly slow; old applications should consider moving away from it.')
        print('   ')
        print('For this 3DES implenebtation, it uses OFB Mode. OFB (Output Feedback) is a mode of operation for block ciphers. It transforms a block cipher into a stream cipher.')
        print('   ')
        print('Becase it is a stream cipher, it does not need padding.')
        print('   ')
        print('iv = initialization_vector (bytes) – Must be random bytes. They do not need to be kept secret and they can be included in a transmitted message. Must be the same number of bytes as the block_size of the cipher. Do not reuse an initialization_vector with a given key.')
        print('   ')
        print('key (bytes) – The secret key. This must be kept secret.')
    elif a == 'no':
            print('That\'s great.')