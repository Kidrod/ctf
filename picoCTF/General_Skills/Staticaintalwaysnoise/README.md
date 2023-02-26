# Challenge: [Static ain't always noise](https://play.picoctf.org/practice/challenge/163)
20 Points
# Description
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)? This [BASH script](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh) might help!
# Solution
This challenge gives me a binary file and require looking for a flag in it.

The first steps I always do are check out all strings existing in binary file. Fortunately, I find a flag. The provided bash script is not really necessary.

```sh
nano2222-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static

nano2222-picoctf@webshell:~$ strings static | less
```

The flag is: picoCTF{*******************}