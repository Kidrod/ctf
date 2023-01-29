# Challenge: [Python Wrangling](https://play.picoctf.org/practice/challenge/166)
10 Points
# Description 
Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](./ende.py) using [this password](./pw.txt) to get [the flag](./flag.txt.en)?
# Solution
When running this python file in the Terminal, it gives me 2 options:

```sh
┌──(kali㉿kali)-[~/picoCTF/Python_Wrangling]
└─$ python3 ./ende.py                                                                                                                                                                                        
Usage: ./ende.py (-e/-d) [file]

```

I think -e meaning encrypt and -d meaning decrypt. Following the description, I import file flag.txt.en and using password in file pw.txt to get the flag.

```sh
┌──(kali㉿kali)-[~/picoCTF/Python_Wrangling]
└─$ python3 ./ende.py -d ./flag.txt.en                                                                                                                                                                     
Please enter the password:67c6cc9667c6cc9667c6cc9667c6cc96
picoCTF{4p0*************6}
```

The flag is: picoCTF{*********************}