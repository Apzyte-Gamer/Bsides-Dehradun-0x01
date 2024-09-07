# Breakup (550 points / 4 solves)

Misa and L ..being the couple that they are.. are breaking up again. Misa says she needs some space and its just all too much. To lighten the mood, L asks her: "Why do you always need space? How about tabs for a change?' ..Jeez what a computer geek! Anyways sorry guyz this is just really a poor joke but not that it matters to you anyways. Your goal is to obtain the flags and solve the challenges so just deal with the bad joke in this one just like I have and just like how you've dealt with all the other descriptions. Thanks :)

## Overview

Okay, so this challenge kinda gave me an L. First of all, I opened up the file in sublime text to find whitespaces. I then used stegsnow in hopes for finding the flag since theres whitespaces....

```bash
└─$ stegsnow -C the_breakup.txt                                                   
ys0ostdEnssd    endsds0tndsseEatsdFpsdbsyhsnw
```

After seeing this, I thought "okay so maybe we have to use a password" (`stegsnow -p <password> -C the_breakup.txt`). So then, I spent the next 30 mins trying to bruteforce every password combination I could make with the words given in the txt file, but it was actually a rabbit hole.

What we actually had to do was replace the spaces with `1` and tabs with `0`. Then we have to remove everything except `0`'s and `1`'s, and we get this:

`010000100111001101101001011001000110010101110011010001000110010101101000011100100110000101100100011101010110111001111011010110010100111101110101010111110110111000110011001100110110010001011111010100110111000000110100011000110011001101011111001101000110111001100100010111110011000101011111011011100011001100110011011001000101111101110100001101000110001000110101010111110110110001101111011011000101111100110011011000110110010000110000011001100011010101100010011001100110010101111101`

```py
with open("the_breakup.txt", "r") as file:
    content = file.read()

binary_representation = content.replace(' ', '1').replace('\t', '0')

binary_cleaned = ''.join([char for char in binary_representation if char in ['0', '1']])

print(binary_cleaned)
```

And then, uponing decoding from Binary to ASCII, we get the flag!

`BsidesDehradun{YOu_n33d_Sp4c3_4nd_1_n33d_t4b5_lol_3cd0f5bfe}`
