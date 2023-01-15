# Challenge: [Encoding - UU](https://www.root-me.org/en/Challenges/Cryptanalysis/Encoding-UU)
5 Points
# Description
Get the validation password.
# Solution
Here is the encoded message which challenge provided:
```
_=_ 
_=_ Part 001 of 001 of file root-me_challenge_uudeview
_=_ 

begin 644 root-me_challenge_uudeview
B5F5R>2!S:6UP;&4@.RD*4$%34R`](%5,5%)!4TE-4$Q%"@``
`
end

```
Based on the title and preference in this challenge, I take the uu-encoding message from the line starting *begin* to the line having *end*. 

Then, I write a script to decode the above message with python.
```python
import uu
from codecs import decode

encoded_msg = b'begin 644 root-me_challenge_uudeview\nB5F5R>2!S:6UP;&4@.RD*4$%34R`](%5,5%)!4TE-4$Q%"@``\n`\n \nend\n'
print(decode(encoded_msg, 'uu'))

```
Excute to see the flag.

Flag is: ***********