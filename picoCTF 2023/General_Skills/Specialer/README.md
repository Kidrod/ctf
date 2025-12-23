# Challenge: [Specialer](https://play.picoctf.org/practice/challenge/378)
80 Points
# Description
Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most.
# Solution
The major difference between this challenge and **Special** is this challenge doesn't allow any commands to be executed apart from the `echo` command. Hence, I had to figure out how to read the flag using only the `echo` command.

First, I needed to run `echo` in a way similar to `ls` to identify where the flag was located. I knew that there were three directories to examine.

```sh
Specialer$ echo *
abra ala sim
Specialer$ echo abra/*
abra/cadabra.txt abra/cadaniel.txt
```

The remaining task was to find a way to use `echo` as an equivalent of the `cat` command in order to probe for the flag in each file within the known directories.

```sh
Specialer$ echo "$( < abra/cadabra.txt )"
Nothing up my sleeve!
```

I continued crawling through the directories and eventually obtained the flag.
