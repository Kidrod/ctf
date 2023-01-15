import uu
from codecs import decode

encoded_msg = b'begin 644 root-me_challenge_uudeview\nB5F5R>2!S:6UP;&4@.RD*4$%34R`](%5,5%)!4TE-4$Q%"@``\n`\n \nend\n'
print(decode(encoded_msg, 'uu'))
