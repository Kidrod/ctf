# Challenge: [Hash - SHA-2](https://www.root-me.org/en/Challenges/Cryptanalysis/Hash-SHA-2)\
5 Points
# Description 
This hash was stolen during a session interception on a critical application, errors may have occurred during transmission. No crack attempt has resulted so far; hash format seems unknown. Find the corresponding plaintext.

The answer is the SHA-1 of this password.
# Solution
First, I need to indentify what type of SHA-2 used here, I check the length of hash string
```console
┌──(kali㉿kali)-[~/root-me/Cryptanalysis/sha2-hash]
└─$ python -c "print(len('96719db60d8e3f498c98d94155e1296aac105ck4923290c89eeeb3ba26d3eef92'))" 
65

```
But 65 is not the real length, you can see a character 'k' in the string. Remove it and I indentify this is SHA-256 string. As the instruction, I have to decrypt SHA-2 string and hash it with SHA-1 to have the flag.

Have many website to decrypt SHA-256 string and I got the password is: **4dM1n**

Lastly, I just use SHA-1 for hashing the above password, that result is the flag.

The flag is: ************