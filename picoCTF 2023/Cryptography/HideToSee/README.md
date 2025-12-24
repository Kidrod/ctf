# Challenge: [HideToSee](https://play.picoctf.org/practice/challenge/351)
50 Points
# Description
How about some hide and seek heh?
# Solution
Based on the challenge hint, I suspected that the image contained hidden information. I used steghide to extract embedded data from the file.

```sh
┌──(kali㉿kali)-[~/Downloads]
└─$ steghide extract -sf atbash.jpg
Enter passphrase: 
the file "encrypted.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "encrypted.txt".
```

After extracting the hidden file, I printed its contents.

```
┌──(kali㉿kali)-[~/Downloads]
└─$ cat encrypted.txt 
krxlXGU{zgyzhs_xizxp_zx751vx6}
```

The extracted text appeared to be encrypted. Since there were some clues related to Atbash cipher, I decoded the string using the Atbash cipher.

After decoding, I obtained the flag.
