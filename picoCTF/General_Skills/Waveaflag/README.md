# Challenge: [Wave a flag](https://play.picoctf.org/practice/challenge/170)
10 Points
# Description
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm) has extraordinarily helpful information...
# Solution
According to the description, I have to download a binary and find the flag in it. 

I can excute the file or just **cat** it to read, I choose the second.

```sh
┌──(kali㉿kali)-[~/picoCTF/Wave_a_flag]
└─$ cat warm | grep -ai "picoCTF"
]��f.�]�@f.�H�=� H��t    H�5�    UH)�H��H��H��H��?H�H��t▒H��     H��t
                                                                     ]��f�]�@f.��=y      u/H�=W  UH��t
����H����Q       ]����fDUH��]�f���UH��H���}�H�u��}�uH�=�������KH�E�H�H�H�5�H���������uH�=��i����H�E�H�H�H��H�=:��X������DAWAVI��AUATL�%F UH�-F SA��I��L)�H�H�������H��t 1��L��L��D��A��H��H9�u�H�[]A\A]A^A_Ðf.���H�H��Hello user! Pass me a -h to learn what I can do!-hOh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_30e77291}I don't know what '%s' means! I do know what -h means though!
```

The flag is: picoCTF{***********}