from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import hashlib
import os

password = b'super_secret_password'
salt = get_random_bytes(16)  # Secure random salt
key = PBKDF2(password, salt, dkLen=16, count=1000000) 

flag = b"{flag}"

padded_flag = pad(flag, AES.block_size)

cipher = AES.new(key, AES.MODE_CBC)

encrypted_flag = cipher.encrypt(padded_flag)

with open("encrypted_flag.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(salt)
    f.write(encrypted_flag)
    print(cipher.iv)
    print(salt)
    print(encrypted_flag)

print("Encrypted flag, IV, and salt written to encrypted_flag.bin")
