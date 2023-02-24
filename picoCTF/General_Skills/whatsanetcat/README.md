# Challenge: [what's a net cat](https://play.picoctf.org/practice/challenge/34)
100 Points
# Description
Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 25103 to get the flag?
# Solution
Generally, don't have many works to do in this challenge. Just use nc command with some elements like host and port that provided. When connecting successfully, get the flag.

```sh
nc jupiter.challenges.picoctf.org 25103
```

The flag is: picoCTF{**********}