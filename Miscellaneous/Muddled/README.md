# Muddled (400 points / 43 solves)

I took an OG image of Ryuk and I mixed it or combined it or encoded it I guess using a secret Image file. As a result all I got was this muddled up image of Ryuk. Now, I cant really understand its contents and I feel like I've messed up big time. Can you tell what it is. If not please help me reverse what I've done and retrieve the contents of the secret Image file. I seriously need your help in recovering the secret file. I'm counting on you!

## Overview

Okay, so upon unzipping the file, we get 2 images and seems like one is the output image from XOR'ing 2 images.

The logic is like this:

Since we have the output file and one of the input files, we can get the second input file.

output_image = image_1 ⊕ image_2
output_image ⊕ image_1 = image2

We can make this into a script as well.

```py
from PIL import Image
import numpy as np

image_1 = Image.open('ryuk_og.png')
image_output = Image.open('muddled_up_ryuk.png')

image_1_array = np.array(image_1)
image_output_array = np.array(image_output)

image_2_array = np.bitwise_xor(image_output_array, image_1_array)

image_2 = Image.fromarray(image_2_array)

image_2.save('image_2.png')
```

And, we get image_2 with the flag!

![image_2](https://github.com/user-attachments/assets/22833e24-846d-4aea-836d-3f5dc9753ae4)

`BsidesDehradun{X0Rrr1n6gg_15_Actu4lly_r3v3r51bl3_70a9bfc1e}`
