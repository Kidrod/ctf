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
Using default input encoding: UTF-8
Using default target encoding: CP850
Loaded 1 password hash (LM [DES 128/128 AVX])
Warning: poor OpenMP scalability for this hash type, consider --fork=4
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
********          (?)
1g 0:00:00:00 DONE (2023-01-17 00:41) 3.225g/s 5655Kp/s 5655Kc/s 5655KC/s ALVINS1..ADAMXOX
Use the "--show --format=LM" options to display all of the cracked passwords reliably
Session completed

```
The flag is: ****************