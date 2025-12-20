# Challenge: [Special](https://play.picoctf.org/practice/challenge/377)
80 Points
# Description
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface 
for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to 
test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)
# Solution
From the challenge description, the shell applied scheme of spell correction and capitalization, making it impossible to execute commands normally.

```sh
Special$ ls
Is 
sh: 1: Is: not found
Special$ whoami
Whom 
sh: 1: Whom: not found
```

After experimenting with various inputs and special characters, I noticed that I was able to use parentheses **()** to wrap my input which allow it to be executed as a system command. And to bypass the spell correction and capitalization, I used backslash **\** as an escape character.

```sh
Special$ (\ls)
(\ls) 
blargh
```

Then, I looked for a way to embed space character for my input, fortunately, `${IFS}` was helpful in this case.

```sh
Special$ (\ls${IFS}blargh)
(\ls${IFS}blargh) 
flag.txt
```

The **flag.txt** was found in the directory **blargh**, I simply ran the `cat` command to read and obtain the flag.
