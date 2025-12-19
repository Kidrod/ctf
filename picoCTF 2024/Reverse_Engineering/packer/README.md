# Challenge: [packer](https://play.picoctf.org/practice/challenge/421)
10 Points
# Description
Reverse this linux executable?
# Solution
I started the challenge by running the provided executable file to observe its behavior. The program prompted for a password, but any input resulted in "Accessed denied" which indicating the password check was likely obfuscated or bypassed.

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ ./out
Enter the password to unlock this file: picoCTF2024
You entered: picoCTF2024

Access denied
```

Next, I used `strings` command to inspect embedded strings inside the binary, but no plaintext password was found.

From the hint of this challenge, it mentioned how can we reduce the size of a binary after compiling. I noticed the header of `strings` command output, the executable file could be packed using UPX to reduce its size.

Hence, I ran `upx -d` command to decompress the file, it worked. I checked the output of `strings` command again and found the hex string of password there.

Finally, I used xxd command to decode the hex string and obtain the flag of this challenge.
