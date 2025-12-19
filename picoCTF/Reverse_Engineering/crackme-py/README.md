# Challenge: [crackme-py](https://play.picoctf.org/practice/challenge/175)
5 Points
# Description
Let inspect a given python file
# Solution
This challenge was quite straightforward and mainly focused on code analysis. 

By reviewing the python source code, I noticed that the main function only called the `choose_greatest()` function, 
while the `decode_secret()` function was never used.

```python
def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)
```

The `decode_secret()` function implemented the ROT47 cipher, which operates on a reference alphabet of 94 characters. Since the 
rotation value is 47, exactly half of the alphabet length. Hence, the same function can be used for both encoding and decoding.

The encoded string was provided at the beginning of the source code, therefore I simply invoked the `decode_secret()` funtion 
from the main program and passed the encoded string as the `secret` parameter.

```python
decode_secret("A:4@r%uL`>0c0Abc?FE0g`_47fgaagg6ffN")
```

After running the program, the decoded output was printed which revealed the flag.
