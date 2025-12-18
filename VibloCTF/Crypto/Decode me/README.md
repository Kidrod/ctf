# Challenge: Decode Me
200 PTS
# Description
Let decode the given string, submit Flag{\<content\>}
```
XQAAgAD//////////wApEkTrkDGPBiZf763r/fwklFegK8CapImKmYB+/m5W2+i+RYa5StHksv1q7jGZ7qUhdwUenXavwntxgUKbbKX0hkNVdU+GzMN1lZBwWHy9RFeh9xpH5tfrFV5p2yvjrrowlAr+L6a5Rmo5ssrx9KiTxyN9N85FpgT05cd12SBgE1UMkBopv4BmG7cjdSOyX0qip8otKwJ1qdJxnwfc+NB2c/TogTYsvk1l3mRiKd6DLU3eEbM89aOtH6fZqn8l/jE8fVAYKH7V7zax1TPCpvR8iaiyAdPSZGcl8RkKcN0l4kWT49flcepPJVCzqIJil1Inuj9oXgc9e/5Vg82f/AeGciy7pwfu0UayZ72MlxTp7sbjlpXCNvO9d14jozMWJe5zTns6/poPxboDROGE+/2dexhBRabB+94HZ2r4YnUzwNCcwDHNRlwujrH/ceUZfCyeAd12CAii07LZmMh8ZiGxwtbCNEE6nMW2b91Cn7JYk2Iu//+vL1Oi
```
# Solution

It was obvious to recongize the given string was base64-encoded, so I started by decoding it using base64, and writing the output to a file.

```sh
┌──(kali㉿kali)-[~/viblo/ctf/decode_me]
└─$ echo "XQAAgAD//////////wApEkTrkDGPBiZf763r/fwklFegK8CapImKmYB+/m5W2+i+RYa5StHksv1q7jGZ7qUhdwUenXavwntxgUKbbKX0hkNVdU+GzMN1lZBwWHy9RFeh9xpH5tfrFV5p2yvjrrowlAr+L6a5Rmo5ssrx9KiTxyN9N85FpgT05cd12SBgE1UMkBopv4BmG7cjdSOyX0qip8otKwJ1qdJxnwfc+NB2c/TogTYsvk1l3mRiKd6DLU3eEbM89aOtH6fZqn8l/jE8fVAYKH7V7zax1TPCpvR8iaiyAdPSZGcl8RkKcN0l4kWT49flcepPJVCzqIJil1Inuj9oXgc9e/5Vg82f/AeGciy7pwfu0UayZ72MlxTp7sbjlpXCNvO9d14jozMWJe5zTns6/poPxboDROGE+/2dexhBRabB+94HZ2r4YnUzwNCcwDHNRlwujrH/ceUZfCyeAd12CAii07LZmMh8ZiGxwtbCNEE6nMW2b91Cn7JYk2Iu//+vL1Oi" | base64 -d > data
```

Then I checked the file type of `data` and discovered that it was LZMA compressed data. Hence, I renamed it with .lzma extension and extracted it.

```sh
┌──(kali㉿kali)-[~/viblo/ctf/decode_me]
└─$ xz --format=lzma -d data.lzma 
```

To identify the output format, I inspected the file header using the `strings` command.

Alright, the final data was an audio file .wav, I listened to the audio and noticed repetitive beeping sounds, which strongly suggested morse code. I then uploaded this file to an online morse decoder to decode the message, and obtain the flag.

Notice: this challenge validates the flag in a case-sensitive manner.
