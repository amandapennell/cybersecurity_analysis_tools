# PART 1: CRYPTOGRAPHY
# For this part, you are required to use Python to perform some cryptography operations. 
# Use the cryptographic objects from Week 7 to help with encryption/decryption.

# 1.1 Install necessary cryptographic modules

# pycryptodome installed using pip install pycryptodome
# import necessary modules

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256, MD5
import base64

# create AESCrypto class for AES encryption/decryption

class AESCrypto:
    def md5_hash(self, text): # MD5 hash function
        h = MD5.new()
        h.update(text.encode())
        return h.hexdigest()

    def __init__(self, key): # constructor
        self.key = self.md5_hash(key) # md5 hash of the key; key size is 128 bits 

    def decrypt(self, enctext): # decryption function
        enctext = base64.b64decode(enctext)
        iv = enctext[:16] # initialization vector
        crypto = AES.new(self.key.encode(), AES.MODE_CBC, iv)      
        unpad = lambda s: s[:-ord(s[-1:])] # unpad the blocks before decryption
        return unpad(crypto.decrypt(enctext[16:]))

# 2.2 Verify the hashes of the supplied part 1 files with their hashes (part1.sha256)

def calculate_hash(file_name): # calculate the hash of the file
    hash_object = SHA256.new() # create hash object with SHA256
    with open(file_name, 'rb') as file: # open file in read binary mode
        while True:
            data = file.read()
            if not data:
                break
            hash_object.update(data) # update the hash object with the data
    return hash_object

def verify_hash(file_name, expected_hash): # verify the hash of the file
    calculated_hash = calculate_hash(file_name).hexdigest()
    return calculated_hash == expected_hash # return true if calculated == expected

def expected_hashes_read(file_name): # read expected_hashes from file
    expected_hashes = {} # create dictionary to store expected_hashes
    with open(file_name, 'r') as file:
        for line in file: # iterate through lines in file
            parts = line.strip().split() # split line into parts 
            if len(parts) == 2:
                file_name, hash_value = parts # assign parts to file_name and hash_value
                expected_hashes[file_name] = hash_value # add parts to dictionary
    return expected_hashes


expected_hashes = expected_hashes_read ('part1.sha256') # read expected values from part1.sha256


for file_name, expected_hash in expected_hashes.items(): # verify hashes using dictionary
    if verify_hash(file_name, expected_hash):
        print(f"Hash for {file_name} successfully verified.") # print if hash is verified
    else:
        print(f"Hash verification for {file_name} failed.") # print if hash isn't verified

# 1.3 Decrypt the encrypted text file using AES-128

aes = AESCrypto('sfhaCS2023') # create AESCrypto object with supplied key
with open('part1.txt.enc', 'rb') as encrypted_file:
    encrypted_text = encrypted_file.read() # read encrypted text from file
    decrypted_text = aes.decrypt(encrypted_text)

print("Decrypted Text:") # print decrypted text
print(decrypted_text.decode()) 

# 1.4: Verify plaintext using the provided signature and public key

with open('publickey.pem', 'rb') as key_file: # read public key from file
    public_key = RSA.import_key(key_file.read()) # import public key with RSA

with open('part1.txt.sig', 'rb') as signature_file: # read signature from file
    signature = signature_file.read()

hash_object = SHA256.new() # create hash object with SHA256
hash_object.update(decrypted_text) # update hash object with decrypted text

try: # verify signature using public key
    PKCS1_PSS.new(public_key).verify(hash_object, signature)
    print("Signature successfully verified. This file is authentic.") # print if signature verification is successful
except (ValueError, TypeError): #
    print("Signature verification failed. This file may be compromised.") # print if signature verification fails