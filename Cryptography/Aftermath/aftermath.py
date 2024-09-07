from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import os

random.seed(1234)
key = bytes([random.randint(0, 255) for _ in range(16)]) 

flag = b"{flag}"

padded_flag = pad(flag, AES.block_size)

cipher = AES.new(key, AES.MODE_ECB)

encrypted_flag = cipher.encrypt(padded_flag)

print(encrypted_flag)
with open("encrypted_flag.bin", "wb") as f:
    f.write(encrypted_flag)
    

#print("Encrypted flag written to encrypted_flag.bin")
