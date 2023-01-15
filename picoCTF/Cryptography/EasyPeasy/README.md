# Challenge: [Easy Peasy](https://play.picoctf.org/practice/challenge/125)
40 Points
# Description
A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})
# Solution
When I start the challenge, I see the encrypted flag as below:
```console
nano2222-picoctf@webshell:~$ nc mercury.picoctf.net 36449
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b
```
I recognize that it also give a file otp.py. Take a look at this file:
```python
#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
	c = encrypt(c)

```
Temporarily, I understand that this programme has 2 function, startup() which is used to encrypt the flag I want to find and encrypt() which is used to encrypt input I enter. It uses XOR the flag with the key (both length is equal) and the rest of key is used to XOR with my input. A one-time pad is unbreakable but in this situation, it use the key again after each 50000 characters. 
First, I need the length of key, I can know it through the length of flag:
```console
nano2222-picoctf@webshell:~$ python -c "print(len('551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b'))"
64
```
Due to this is a hex lenghth, I have the length of flag is 32 characters. Turn back to file otp.py, I feel I can exploit this programme at line **if stop >= KEY_LEN**. Next, I will XOR the string of 32 characters 'a' and need a buffer contains 49968 characters ahead.
```console
nano2222-picoctf@webshell:~$ python -c "print('a'*49968);print('a'*32)" | nc mercury.picoctf.net 36449
```
The input is over the length of key, therefore, the last 32 characters 'a' will be XOR with the first 32 characters of the key which is used to XOR with the flag.
I have a result as below:
```console
What data would you like to encrypt? Here ya go!
034605413d190050083d1951533d1902053d1903003d1902553d190403500f3d
```
At this time, I have enough elements to find the flag. Encryted string of 32 characters 'a' and original string a help me find out the value of key used to encrypt flag. 
```console
nano2222-picoctf@webshell:~$ python
Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> ea = 0x034605413d190050083d1951533d1902053d1903003d1902553d190403500f3d
>>> pa = 0x6161616161616161616161616161616161616161616161616161616161616161
>>> ef = 0x551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b
>>> print(hex(ea^pa^ef))
0x3735333032623338363937613837313766306661656539633066643336613537
>>> print(bytes.fromhex('3735333032623338363937613837313766306661656539633066643336613537').decode('utf-8'))
75302b38697a8717f0faee9c0fd36a57
```
Flag is: picoCTF{***************}
