# Challenge: [The Numbers](https://play.picoctf.org/practice/challenge/68)
50 Points
# Description
The numbers... what do they mean?
# Solution
Resources for this challenge is a picture, the content is a string of decimal numbers. 

<img src='./media/the_numbers.png' alt='A string of decimal numbers' />

Carefully review the picture, I see 2 characters { } so I guess this is the flag but it was encoded. 

I test some first characters of the string by comparing to 'pico' in flag. I understand that the flag was encoded base-26. This is a easy method to encode, just use the index of the character in alphabet representing for the character.

A <-> 1, B <-> 2, C <-> 3, ........

Due to knowing the scheme, I write an python script to decode:

```python
def solve():
    s = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
    arr = s.split()
    a=[]
    for i in range(1,27):
        a.append(str(i))
    d = {}
    for i in range (26):
        d[a[i]] = chr(65 + i)
    print("".join([d.get(c,c) for c in arr])) 
if(__name__ == "__main__"):
    solve()
```

The flag is: picoCTF{********}