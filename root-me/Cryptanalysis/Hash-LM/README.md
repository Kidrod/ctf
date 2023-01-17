# Challenge: [Hash - LM](https://www.root-me.org/en/Challenges/Cryptanalysis/Hash-LM)
5 Points
# Description
Retrieve the password of the Administrator user from the information output by the secretsdump tool of the Impacket suite.
# Solution
I go through Administrator hashes and get an LM hash based on the format: username : unique_identifier : LMhash : NThash. Accordingly, the third field is an LM hash.

Since I don't have a specialized hardware to use hashcat, I crack the LM hash by using John The Ripper, another good tool for cracking passwords. 

```console
┌──(kali㉿kali)-[~/root-me/Cryptanalysis/lm]
└─$ echo "d3bf255c530633b9aad3b435b51404ee" > lmhash
                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/root-me/Cryptanalysis/lm]
└─$ sudo john --format=LM --wordlist=/home/kali/rockyou.txt lmhash

```
The flag is: ****************
