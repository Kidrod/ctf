# Challenge: [Hash - DCC2](https://www.root-me.org/en/Challenges/Cryptanalysis/Hash-DCC2?action_solution=voir#ancre_solution)
5 Points
# Description
Retrieve the password of the Administrator user from the information output by the secretsdump tool of the Impacket suite.
# Solution
First, I have to get the DCC2 hash of Administrator in the output of secretsdump. It's not hard to find the line of DCC2 hash
```
ROOTME.LOCAL/Administrator:$DCC2$10240#Administrator#23d97555681813db79b2ade4b4a6ff25
```
After getting the hash, I use John The Ripper to crack it by the below command:
```sh
echo '$DCC2$10240#Administrator#23d97555681813db79b2ade4b4a6ff25' >> mscash && sudo john --format=mscash2 --wordlist=/home/kali/rockyou.txt mscash
```
The flag is: ***************