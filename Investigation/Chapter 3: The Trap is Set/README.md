# Chapter 3: The Trap is Set (200 points / 4 solves)

Gaining access to Kira’s computer wasn’t enough. To capture more critical information, L secretly deploys a spy program on Kira's system. It is able to give L the current state of Kira’s computer for him to analyze it. L suspects that Kira hid a crucial stuff somewhere in the.

## Overview

This time, we get a pcapng file, interesting.

## Solve

Opening the pcapng file, we can see that the website `pastebin.com` is being opened. When we filter the packets based on the protocol, and go to the FTP protocols, we see that the user `sneckey0day` is trying to login with the password `letmein`.

![image](https://github.com/user-attachments/assets/1961dd6f-a2a7-4428-a4a6-63f343cf16ba)
![image](https://github.com/user-attachments/assets/e0ee7448-b723-4199-8ad0-056b1593aea5)

Trying to login with these credentials obviously doesnt work but we do have the user `sneckey0day` in pastebin (https://pastebin.com/u/sneckey0day). Opening his profile, we get a file named `
L_Message_For_U`. There, we find our flag!

`BsidesDehradun{Y0U_UnH1D3_7h3_S3cr37}`
