import cryptography
from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#file = open('key.key', 'wb')
#file.write(key) # The key is type bytes still
#file.close()# it will create a file and store a key which is generated to keep safe
#file = open('key.key', 'rb')
#key = file.read() # The key will be type bytes
#file.close()
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass

   
def encry_decry():
    while True:
        
        a=input("Would you like to (E)ncrtpt or (D)ecrypt?: ")
        if a=="E":
            input_file = input("enter the file: ")
            output_file = 'encrypted'+input_file

            with open(input_file, 'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
            os.remove(input_file)

            with open(output_file, 'wb') as f:
                f.write(encrypted)
            print("Done")
            break
        elif a=="D":

            input_file = input("enter the encrypted file: ")
            output_file = input_file[9:]

            with open(input_file, 'rb') as f:
                data = f.read()
    
            fernet = Fernet(key)
            encrypted = fernet.decrypt(data)
            os.remove(input_file)

            with open(output_file, 'wb') as f:
                f.write(encrypted)
            print("Done")
            break
        else:
            print("please choose E or D")
            continue
        


            
        

password_provided = getpass("Enter the password: ") # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
  
if __name__ == '__main__':
    encry_decry()
    


    
