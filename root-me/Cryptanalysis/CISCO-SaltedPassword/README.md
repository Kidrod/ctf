# Challenge: [CISCO - Salted Password](https://www.root-me.org/en/Challenges/Cryptanalysis/CISCO-Salted-Password)
10 Points
# Description
Your company's network administrator forgot his administration passwords. He does however have a backup of his startup-config file. Use it to recover his passwords!

The flag is the concatenation of the "enable" and "administrator" passwords.

Good luck!
# Solution
This challenge provide me a backup file, I need to retrieve 2 password of enable and administrator, then concat them to have the flag.

For a while researching, I think I could solve this challenge by using openssl. This tool is used to generate Cisco password hashes as well.

But before finding the flag. I have to clarify some elements in Cisco password type 5.

- $1: indicates it's MD5 hash
- $mERr: is a salt
- $A419.HL58lq743wXS4kSM1: means salt + password MD5 hash

Next, I find 2 password in the cases generating by openssl. 

```sh

┌──(kali㉿kali)-[~/root-me/Cryptanalysis/CISCO-SaltedPassword]
└─$ openssl passwd -1 -salt mERr -table -in /home/kali/rockyou.txt | grep HL58lq743wXS 
*************** $1$mERr$A419.HL58lq743wXS4kSM1

┌──(kali㉿kali)-[~/root-me/Cryptanalysis/CISCO-SaltedPassword]
└─$ openssl passwd -1 -salt mERr -table -in /home/kali/rockyou.txt | grep 74CxKANvoekD
**********      $1$mERr$yhf7f2RnC74CxKANvoekD.

```

Concat 2 password to get the flag.

The flag is: *********
