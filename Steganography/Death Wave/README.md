# Death Wave (350 points / 7 solves)

This death wave will be the last thing you might ever listen to. We have all heard of the sweet taste of death. But have we ever heard the sweet sound of death?? Hear this and you might. Lets see if you are capable of obtaining a flag from it as part of your final wish. Just a little reward before you depart ought to be nice.

## Overview

They provide us with a file with no extension. Looking at its first few bytes, we can confirm its a `wav` file.

## Solve

The first thing that comes to mind is binwalk and other tools, but nothing seemed to avail. So for the one and only time, I tried to extract the LSB bytes and to my surprise it worked lol.

```bash
└─$ stegolsb wavsteg -r -i challenge\ \(1\).wav -o data_output.txt -n 2 -b 1000000
Files read                     in 0.02s
Recovered 1000000 bytes        in 0.12s
Written output file            in 0.00s
```

```bash
└─$ strings -n 8 data_output.txt                                                  
BsidesDehradun{L5Bs_4r3_4c7u4lly_v3ry_S1gnif1c4nt!!}
!5uu10'Mnn
VtgFutdddc
@3      ()9<oM]
...
...
```

`BsidesDehradun{L5Bs_4r3_4c7u4lly_v3ry_S1gnif1c4nt!!}`
