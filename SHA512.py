# Wesley Huang
# 100547950
#SHA 512

def SHA512():
    data = (input("Enter plaintext: "))
    print("Plaintext: " + str(data))
    data = data.encode()
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
    digest.update(data)
    x =digest.finalize()
    print("The hash value is: " + str(x))
    y = (int(input("For information about SHA 512 enter 1: ")))
    if (y == 1):
        print("The message is padded so that the length is equal to 896(mod 1024), even if the message is already the desired length. The padding consists of a 1 followed by the necessary number of 0 bits. Then the length of the original message(without padding) is appended to the end of the message as a 128 bit block. The block is treated as an unsigned 128-bit integer with the most significant byte first. This gives a message that has a length that is a multiple of 1024 bits (N*1024). Then a 512-bit hash buffer is initialized to hold intermediate and final results of the hash. The buffer is represented as eight 64-bit registers(a,b,c,d,e,f,g,h) that hold the following values: \n")
        print("a = 6A09E667F3BCC908 		e = 510E527FADE682D1")
        print("b = BB67AE8584CAA73B	 	f = 9B05688C2B3E6C1F")
        print("c = 3C6EF372FE94F82B 		g = 1F83D9ABFB41BD6B")
        print("d = A54FF53A5F1D36F1 		h = 5BE0CD19137E2179 \n")
        print("the buffers are stored in big-endian format which is the most significant byte of a word in the leftmost byte position. The message is proccesed in 1024-bit blocks with the algorithm containing 80 rounds. Each round takes a 512-bit buffer value, a-h, and has a value of the intermediate hash value H(i-1). Each round uses a 64-bit value W which is derived from the current 1024-bit block that is being procesed. Each round makes use of a constant K that indicates one of the 80 rounds. After all the 1024-bit blocks have been processed, a 512-bit message digest is outputted")