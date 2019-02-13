#Jason Pinto 
#100592099
#X509 certifcate 

from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join

def X509():
    
    certificateimg = "X509 Certificate.crt" #this is the certificate file
    key = "X509 Key.key" #this is the key file
    
    def create_certificate(cert_dir):
    
        if not exists(join(cert_dir, certificateimg)) \
                or not exists(join(cert_dir, key)):
    
            # create a key pair
            k = crypto.PKey()
            k.generate_key(crypto.TYPE_RSA, 1024)
    
            # create a self-signed cert
            cert = crypto.X509()
            cert.get_subject().C = input("Please enter your Country's 2-letter abbreviation: ")
            cert.get_subject().ST = input("Please enter your Province: ")
            cert.get_subject().L = input("Please enter your City: ")
            cert.get_subject().O = input("Please enter your Organization: ")
            cert.get_subject().OU = input("Please enter your Organizational Unit, if unknown enter 'na': ")
            cert.get_subject().CN = input("Please enter the Creator/Common Name: ")
    
            cert.set_serial_number(1000)
            cert.gmtime_adj_notBefore(0) #get current date/time
            cert.gmtime_adj_notAfter(10*365*24*60*60) #set expiry to 10 years for current time
            cert.set_issuer(cert.get_subject()) #set the issuers of the certificate
            cert.set_pubkey(k) #set the public key
            cert.sign(k, 'sha256') # sign using sha256 can be changed to sha1 if desired
    
            open(join(cert_dir, certificateimg), "wb").write(
                crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
            open(join(cert_dir, key), "wb").write(
                crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    
    create_certificate(".") # create if successful
    
    print("")
    print("Congratulations! You have successfully created a self-signed X.509 Certificate.")
    print("")
    print("Using the information the user has provided, this program successfully created a self signed certificate by creating a certificate file, creating a key file, combining the user provided info, getting the current date, setting the file to expire 10 years from the current date, setting the issuer of the file, setting the public key, and signed using sha256. Both the certificate and key files were then written to the users directory.")
    while True:
        i = input("Would you like to see a more indepth breakdown?: (y/n) :")
        if i == "y": 
            print("")
            print("BREAKDOWN: An instance of generating a key pair is done first using 1024-bit RSA. key pair k = crypto.PKey() k.generate_key(crypto.TYPE_RSA, 1024).") 
            print("The input from the user is then used in the generation of the X509 certificate. The serial number of the certificate is then set to 1000 and will increment when a new one is renewed/generated. cert.set_serial_number(1000).") 
            print("The current date is retrieved with this snippet of code. cert.gmtime_adj_notBefore(0).")
            print("The expiry time of the certificate is set with the same code as the current time, but it uses math to calculate the expiry in 10 years from the date of creation. cert.gmtime_adj_notAfter(10*365*24*60*60).")
            print("Then the issuer/creator of the certificate gets set. cert.set_issuer(cert.get_subject()).")
            print("The public key is also set at this time. cert.set_pubkey(k) And signed with sha256. cert.set_pubkey(k).")
            print("Everything is then written to the certificate file and the key file using this code. open(join(cert_dir, certificateimg), 'wb'). write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert)) open(join(cert_dir, key), 'wb').write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k)).")
            print("The certificate is created at this point and placed in the directory where this .py file is saved.")
            break
        elif i == "n":
            break
        else:
            print("")
            print("Enter either y/n")
    
