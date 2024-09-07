# Dynamic Quick Response (500 points / 14 solves)

Is it pronounced GIF orJIF??? Ah anyways... Here is a nice litte GIF of a QR code. Bet you've never seen that before. A Quick Response code that is dynamically changing and not static? A QR in the form of a GIF?? Sounds weird doesn't it? However lets test your mettle and find out what you can uncover from this Challenge. We wish you all the best!!

Flag Format: BsidesDehradun{long_hex_value}

## Overview

Looking at the gif, we notice that there are many QR codes in different frames.
To decode all of them, I used this script:

```py
from PIL import Image
from pyzbar.pyzbar import decode

gif = Image.open("challenge.gif")
for frame_number in range(gif.n_frames):
    gif.seek(frame_number)
    gif_frame = gif.copy()
    decoded_objects = decode(gif_frame)
    for obj in decoded_objects:
        print(f"Frame {frame_number}: {obj.data.decode('utf-8')}")
```

The output is:

```
Frame 0: [5Mz,14]
Frame 1: [MzOW,4]
Frame 2: [Dk0Z,11]
Frame 3: [YzdiZmRm,1]
Frame 4: [JlNDRlNzY,5]
Frame 5: [NzFh,0]
Frame 6: [xMTQ1,8]
Frame 7: [MjUxMz,2]
Frame 8: [kwM,15]
Frame 9: [M2M,7]
Frame 10: [hM,10]
Frame 11: [5YTQ4,6]
Frame 12: [TZjNWU,13]
Frame 13: [mZiO,12]
Frame 14: [TVjM2R,16]
Frame 15: [YyMT,3]
Frame 16: [MDg0OWF,9]
Frame 17: [jOA,17]
```

Okay, so this seems like that these little collections of words are in order. We can arrange them accordingly like this:

```py
fragments = [
    ("NzFh", 0),
    ("YzdiZmRm", 1),
    ("MjUxMz", 2),
    ("YyMT", 3),
    ("MzOW", 4),
    ("JlNDRlNzY", 5),
    ("5YTQ4", 6),
    ("M2M", 7),
    ("xMTQ1", 8),
    ("MDg0OWF", 9),
    ("Dk0Z", 11),
    ("hM", 10),
    ("TZjNWU", 13),
    ("mZiO", 12),
    ("TVjM2R", 16),
    ("5Mz", 14),
    ("kwM", 15),
    ("jOA", 17),
]

sorted_fragments = sorted(fragments, key=lambda x: x[1])
combined_data = ''.join(fragment[0] for fragment in sorted_fragments)

print("Combined Data:", combined_data)
```

Now that we have our combined data `NzFhYzdiZmRmMjUxMzYyMTMzOWJlNDRlNzY5YTQ4M2MxMTQ1MDg0OWFhMDk0ZmZiOTZjNWU5MzkwMTVjM2RjOA`, we can convert from Base64 to ASCII:

![image](https://github.com/user-attachments/assets/e226b810-1085-438f-a8c8-93710f9686ef)

And wrapping it in the format gives us the flag!

`BsidesDehradun{71ac7bfdf2513621339be44e769a483c11450849aa094ffb96c5e939015c3dc8}`
