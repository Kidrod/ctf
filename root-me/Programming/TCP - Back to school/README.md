# Challenge: [TCP - Back to school](https://www.root-me.org/en/Challenges/Programming/TCP-Back-to-school)
5 pts
# Description
To start this test using the TCP protocol, you need to connect to a program on a network socket.

 > Calculate the square root of number 1 and multiply by number 2.
 > Then round the result to two decimal places.
 > You have 2 seconds to send the correct answer from the moment the program sends you the calculation.

# Solution
I firstly started connecting to the server and tried receiving its message, I found out that every time I connected, it gave me a random number to calculate. Because I only had 2 seconds to submit my result of calculation to obtain the flag, I put another part in my script in order to do math calculation. 

```sh
┌──(kali㉿kali)-[~/rootme/Programming]
└─$ python solve.py
[+] Opening connection to challenge01.root-me.org on port 52002: Done

====================
 GO BACK TO COLLEGE
====================
You should tell me the answer of this math operation in less than 2 seconds !

Calculate the square root of 238 and multiply by 8285 = 
[*] Switching to interactive mode

```
