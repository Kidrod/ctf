# Challenge: [Transformation](https://play.picoctf.org/practice/challenge/104)
20 Points
# Description
I wonder what this really is... [enc](https://mercury.picoctf.net/static/dd6004f51362ff76f98cb8c699510f23/enc)

''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
# Solution
There are many ways to solve this challenge, some authors have also pointed out UTF-16BE encoding. However, I will write code to manually reverse it.

I predict that all characters of the flag having Unicode value within the 8-bit size range, so I can separate the two components from each other.

```python
file1 = open('enc', 'r')
encoded_string = file1.read()

decoded_string = ""
for i in range(0, len(encoded_string), 1):
    combined_value = ord(encoded_string[i])
    first_char_value = combined_value >> 8  # Extract the first character
    second_char_value = combined_value & 0xFF  # Extract the second character
    decoded_string += chr(first_char_value) + chr(second_char_value)

print(decoded_string)
```