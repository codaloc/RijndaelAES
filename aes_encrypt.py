from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

input_type = input("custom text in encrypt? (y/N)")
if input_type == ("y" or "Y"):
    data = input("data? \n").encode()
else:
    data = 'secret data to transmit'.encode()

key_type = input("custom key? (y/N)")
if key_type == ("y" or "Y"):
    aes_key = pad(input("key ? \n").encode(),16)
else:
    aes_key = get_random_bytes(16)
    print(f"Random key: {aes_key}")

cipher = AES.new(aes_key, AES.MODE_CTR)
ciphertext = cipher.encrypt(data)

with open("encrypted.bin", "wb") as f:
    f.write(cipher.nonce)
    f.write(ciphertext)