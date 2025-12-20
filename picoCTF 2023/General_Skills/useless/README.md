# Challenge: [useless](https://play.picoctf.org/practice/challenge/384)
20 Points
# Description
There's an interesting script in the user's home directory

Additional details will be available after launching your challenge instance.
# Solution
I started the challenge in the home directory of the provided remote instance. There was only one excutable file, so I decided
to inspect it first.

```sh
picoplayer@challenge:~$ file useless 
useless: Bourne-Again shell script, ASCII text executable
```

From the output above, I knew that this file is a bash script rather than a binary, which means it is readable. Hence, I used 
the `cat` command to inspect its content.

```sh
picoplayer@challenge:~$ cat useless 
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
        if [[ "$1" == "add" ]]
        then 
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"  

        elif [[ "$1" == "sub" ]]
        then 
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub" 

        elif [[ "$1" == "div" ]]
        then 
          div=$(( $2 / $3 ))
          echo "The quotient is: $div" 

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul" 

        else
          echo "Read the manual"
         
        fi
fi
```

The calculation logic itself did not seem exploitable, however, I noticed the message "Read the manual", which suggested 
me checking the manual page of this shell script.

```sh
picoplayer@challenge:~$ man useless
```

After reading the manual page, I obtained the flag.
