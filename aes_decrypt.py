import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

with open("encrypted.bin", "rb") as f:
    nonce = f.read(8)
    ciphertext = f.read()
print(ciphertext.hex())

aes_key = pad(input("Key? \n").encode(), 16)
print(aes_key)
##aes_key = b'\xa5\xdb#*\xe5\xd0\xf0p\x01\xf8\xfa\x91\xf5\xa1\x9e3'
cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
message = cipher.decrypt(ciphertext)
print("Message:", message.decode())



