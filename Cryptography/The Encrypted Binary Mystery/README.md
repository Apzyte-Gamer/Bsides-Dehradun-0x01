# The Encrypted Binary Mystery (400 points / 26 solves)

Welcome to the Encrypted Binary Mystery challenge! In this intriguing task, you'll dive into a world of binary codes and compression techniques to uncover a hidden secret. Your mission is to decode the binary array, decompress the hidden data, and reveal the ultimate flag.

## Overview

This challenge gives a binary array that needs to be decoded and decompressed to reveal a hidden flag. The array consists of binary strings in the form of `0b` prefixed binary values. The goal is to convert these binary values, remove unnecessary characters, and use zlib decompression to extract the final flag.

## Solve

Understanding the Input:
The provided binary array is a sequence of strings in the form of `['0b01111000', '0b10011100', ...]`. Each string represents an 8-bit binary value prefixed with 0b.

Here's the process broken down:

1) Load the binary data into CyberChef by copying the array into the input.
2) Use the Find/Replace function to remove the `0b` prefix from each binary value.
3) Similarly, replace the commas (`,`) with an empty string.
4) Remove the single quotes (`'`) by repeating the Find/Replace step for them.
5) Convert the remaining binary sequence to ASCII using the From Binary function.
6) Apply zlib decompression with the Zlib Inflate function to reveal the hidden flag.

![image](https://github.com/user-attachments/assets/cb88b428-8bb7-4c9f-88f6-75e976573767)

`BsidesDehradun{564987632415678976543456789}`
