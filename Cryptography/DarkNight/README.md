# DarkNight (400 points / 31 solves)

Sealed by PBKDF2's relentless iterations, the secret hides in darkness. Will you defy death and decrypt its final secret? one of the secret is super_secret_password

## Overview

The challenge revolves around decrypting an AES-encrypted flag stored in a binary file (`encrypted_flag.bin`). The encryption key is derived using PBKDF2 from the password `super_secret_password` with a randomly generated salt. AES-CBC mode is used for the encryption, requiring an IV for decryption. We have to reverse the encryption process by using the provided password to retrieve the flag.

## Generation

In the script, the following steps occur:

- Key Derivation: The key for AES encryption is generated using PBKDF2 with the password `super_secret_password`, a random 16-byte salt, and 1,000,000 iterations.
- AES Encryption: The flag is padded to fit the AES block size and then encrypted using AES in CBC mode. A random initialization vector (IV) is used for the encryption.
- File Write: The IV, salt, and encrypted flag are written to `encrypted_flag.bin`.

## Solve

  To solve the challenge:

1) Extract IV, Salt, and Ciphertext: The first 16 bytes of the binary file are the IV, the next 16 bytes are the salt, and the remaining bytes are the encrypted flag.
2) Key Regeneration: Using PBKDF2 with the extracted salt, password, and the same parameters (1,000,000 iterations, 16-byte key), the encryption key is regenerated.
3) AES Decryption: Using the extracted IV and regenerated key, the encrypted flag is decrypted using AES in CBC mode, and the padding is removed to reveal the original flag.

```py
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad

password = b'super_secret_password'

with open("Darknight.bin", "rb") as f:
    iv = f.read(16) 
    salt = f.read(16)
    encrypted_flag = f.read()

key = PBKDF2(password, salt, dkLen=16, count=1000000)
cipher = AES.new(key, AES.MODE_CBC, iv)

decrypted_flag = unpad(cipher.decrypt(encrypted_flag), AES.block_size)

print(decrypted_flag.decode())
```

`BsidesDehradun{PBKDF2_S4lt3d_AES_CBC_1s_S3cur3!}`
