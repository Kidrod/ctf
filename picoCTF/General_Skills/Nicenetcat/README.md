# Challenge: [Nice netcat...](https://play.picoctf.org/practice/challenge/156)
15 Points
# Description 
There is a nice program that you can talk to by using this command in a shell: **$ nc mercury.picoctf.net 35652**, but it doesn't speak English...
# Solution
When I paste the above netcat command, I give a string of numbers. I realize this is an ASCII string. 

```sh
nano2222-picoctf@webshell:~$ nc mercury.picoctf.net 35652
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
57 
98 
51 
98 
55 
51 
57 
50 
125 
10 
```

Copy the string and decode it to get the flag.
The flag is: picoCTF{****************} 