**Challenge:** [Mod 26](https://play.picoctf.org/practice/challenge/144)
------------
ROT13 is a encrypt method that replaces a letter with the 13th letter after it in the alphabet.
``` 
Example: A <-> N, B <-> O, C <-> P
```
Here is my source code:
```
import codecs

ciphertext = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"

plaintext = codecs.decode(ciphertext, 'rot_13')
print(plaintext)
```
The flag: picoCTF{***********}
