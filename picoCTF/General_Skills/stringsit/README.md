# Challenge: [strings it](https://play.picoctf.org/practice/challenge/37)
100 Points
# Description 
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?
# Solution
Don't waste much time to resolve this challenge, just using strings command to print all strings in the binary file and combining simultaneously grep command to filter the flag string.

```sh
nano2222-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
nano2222-picoctf@webshell:~$ ls
strings
nano2222-picoctf@webshell:~$ strings strings | grep pico
picoCTF{*********}
```

The flag is: picoCTF{************}