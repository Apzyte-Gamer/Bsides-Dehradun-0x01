# Chapter 2: The Cipher of Shadows (400 points / 8 solves)

After locating Kira's trail, L discovers that Kira has encrypted his most sensitive data. A DUMP FILE of Kira's computer is all we got to Investigate, and breaking it is the only way to proceed.

[Challenge link](https://drive.google.com/file/d/1t04PEhH9Osxp8-gheO_o0A4C3T-truM3/view?usp=sharing)

## Overview

Well, theres nothing to really see except that there's a dump file.

## Solve

The first thing in my mind came to dump the hashes. So I did it by using - `python vol.py -f 14MDUMP windows.hashdump`

```bash
Administrator   500     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
Guest           501     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
Sneckey0Day     1000    aad3b435b51404eeaad3b435b51404ee        becedb42ec3c5c7f965255338be4453c
```

Hmmm, interesting. There's this user `Sneckey0Day` with the NTLM hash of `becedb42ec3c5c7f965255338be4453c`. Cracking this gives us the password - `letmein`.

![image](https://github.com/user-attachments/assets/962bd71c-ffae-4b9d-9c1f-72ae809084f5)

Using the phrase `letmein` actually gives us the flag!

`BsidesDehradun{letmein}`
