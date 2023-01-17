# Challenge: [Hash - Message Digest 5](https://www.root-me.org/en/Challenges/Cryptanalysis/Hash-Message-Digest-5)
5 Points
# Description
Crack the given hash.
# Solution
According to the title, easily recognize this string is an MD5 hash with 16 characters
```
7ecc19e1a0be36ba2c6f05d06b5d3058
```
I crack MD5 hashes with John The Ripper tool and my command as bellow:
```console
┌──(kali㉿kali)-[~/root-me/Cryptanalysis/md5]
└─$ echo "7ecc19e1a0be36ba2c6f05d06b5d3058" > md5hash

┌──(kali㉿kali)-[~/root-me/Cryptanalysis/md5]
└─$ sudo john --format=raw-md5 --wordlist=/home/kali/rockyou.txt md5hash

```
The flag is: *******