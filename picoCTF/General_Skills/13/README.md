# Challenge: [13](https://play.picoctf.org/practice/challenge/62)
100 Points
# Description
Cryptography can be easy, do you know what ROT13 is? **cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}**
# Solution
ROT13 only works on 26 characters alphabet, all upper and lower case. Its scheme depends on dividing 26 characters into 2 parties. Each character presents for the other one so that their distance is 13. 

Based on its work. Here is the code to resolve: 

```python
def solve():
    s = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    print("".join([d.get(c,c) for c in s])) 
if(__name__ == "__main__"):
    solve()
```

The flag is: picoCTF{**********}