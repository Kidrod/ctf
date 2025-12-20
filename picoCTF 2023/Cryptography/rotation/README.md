# Challenge: [rotation](https://play.picoctf.org/practice/challenge/373)
5 Points
# Description
You will find the flag after decrypting this file
# Solution
This challenge provided a flag-like string where some special characters such as braces and underscores were unchanged, suggesting 
a simple rotation cipher.

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ cat encrypted.txt 
xqkwKBN{z0bib1wv_l3kzgxb3l_i4j7l759}
```

Since the challenge name is **rotation**, I tested ROT ciphers by brute-forcing different rotation values. The flag was revealed 
when applying ROT18.
