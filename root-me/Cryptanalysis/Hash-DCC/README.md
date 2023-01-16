# Challenge: [Hash - DCC](https://www.root-me.org/en/Challenges/Cryptanalysis/Hash-DCC)
5 Points
# Description 
Retrieve the password of the Administrator user from the information output by the secretsdump tool of the Impacket suite.
# Solution
I found a clue to retrieve the password in the information of Dumping cached domain
> ROOTME.LOCAL/Administrator:15a57c279ebdfea574ad1ff91eb6ef0c:Administrator

To solve this, I used John The Ripper in Kali. Firstly, make a file contains the content of admin's password hashes
```console
echo 'Administrator:15a57c279ebdfea574ad1ff91eb6ef0c' >> mscash
```
Then, use John command like bellow
```console
john --format=mscash --wordlist=/usr/share/wordlists/rockyou.txt mscash
```
**Note**: Before run the command, you need to decompress to have rockyou.txt in /usr/share/wordlists
Flag is: **********
