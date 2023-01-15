# Challenge: [Mind your Ps and Qs](https://play.picoctf.org/practice/challenge/162)
20 Points
# Description
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?
# Solution
When start the challenge it will send you a file contains some information:
```
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537
```
n is is the result of multiplying two prime numbers p and q (n = p * q) and c is the cipher, e is used to compute d. I solve this challenge by using [this link](https://www.dcode.fr/rsa-cipher). A lazy solution :))
```
Flag is: picoCTF{****************}
```
