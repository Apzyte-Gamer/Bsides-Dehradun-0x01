# DeadlyClue (700 points / 19 solves)

Uncover the clue, just like solving the mystery. Just as a detective pieces together fragments of evidence to unravel a complex case

## Overview

In this challenge, a Python program that uses AES encryption in Counter (CTR) mode encrypts two pieces of data: a known plaintext message and the flag stored in a file. Our goal is to retrieve the flag, given the ciphertext for both the test message and the flag.

CTR mode turns block ciphers into stream ciphers, meaning that if the same key and counter are reused, it can lead to vulnerabilities where we can exploit the relationship between the ciphertexts of different plaintexts.

## Encryption

The given program uses Python’s pycryptodome library to implement AES encryption in CTR mode.

1) Key Generation: The program generates a random 16-byte AES key using os.urandom(16).
2) AES-CTR Encryption: It uses AES in CTR mode with a 128-bit counter. AES-CTR mode functions as a stream cipher, where each block of plaintext is XORed with the AES-encrypted counter value.
3) Encryption Process:
   
   a) The plaintext (test) is encrypted first, producing a hex-encoded ciphertext.
   
   b) The flag (flag.txt contents) is read from a file and also encrypted using the same key and counter. This is the core vulnerability in the program.

## Solve

Given the ciphertext for both the test message (which we know the plaintext for) and the flag, we can XOR the two ciphertexts together. This eliminates the key stream and gives us the XOR of the two plaintexts. Then, by XORing this result with the known plaintext, we can recover the flag.

1) Extract the Ciphertexts: We have two ciphertexts: one for the known plaintext (test) and one for the flag. Both are hex-encoded, so we convert them back to bytes.
2) XOR the Ciphertexts: Since both plaintexts were encrypted with the same key and counter, XORing the two ciphertexts cancels out the key stream and gives us the XOR of the two plaintexts.
3) XOR with Known Plaintext: We know the plaintext for the test message, so by XORing the result from step 2 with the test message, we can recover the flag.

```py
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

ciphertext_test_hex = "78fe7d83a561cb2e1f350e35c4436ddecdacf25813b2677ad879409209b527be7ab9e9027b3563dbc0951c1188301273d5bcc23bfbde011144a19cf0e6063589e786c70857374674e142e8584f38b5d1b1a21dd347b14d30195c4441de2b63f51b41e398fd17e1669b9ba0f71a242dd5786c262adb288a4cb0fa71f7781b51978df99301289ea15035bfab9e067cfec0ad4c5b"
ciphertext_test = bytes.fromhex(ciphertext_test_hex)

ciphertext_flag_hex = "74e23495a975e73f57280971c15f7fe39daaa32741ae5638d17c078a0e831fe42eade04035372cd3"
ciphertext_flag = bytes.fromhex(ciphertext_flag_hex)

plaintext_test = b"No right of private conversation was enumerated in the Constituation. I don't suppose it occurred to anyone at the time that it could be prevented."

xor_result = xor_bytes(ciphertext_test, ciphertext_flag)

recovered_flag_part = xor_bytes(xor_result, plaintext_test[:len(xor_result)])
print(recovered_flag_part)
```

`BsidesDehradun{K1r4_1s_4lw4ys_W4tch1ng!}`
