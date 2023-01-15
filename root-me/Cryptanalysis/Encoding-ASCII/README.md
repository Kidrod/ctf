# Challenge: [Encoding - ASCII](https://www.root-me.org/en/Challenges/Cryptanalysis/Encoding-ASCII)
5 Points
# Description
Decode the string.
# Solution
This is a string it wants me to decode: 
```
4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465
```
After observing the above string, I know this is a hex string. It has many solutions to decode it and I will solve it by linux command
```sh
┌──(kali㉿kali)-[~]
└─$ echo 4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465  | xxd -r -p                                                             130 ⨯
Le flag de ce challenge est: 2ac376481ae546cd689d5b91275d324e  
```
I use 2 commands *echo* and *xxd* within a pipe, echo will import the string to xxd to decode the string from hex to ascii.

The flag is: *******************