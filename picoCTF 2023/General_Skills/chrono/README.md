# Challenge: [chrono](https://play.picoctf.org/practice/challenge/347)
20 Points
# Description
How to automate tasks to run at intervals on linux servers?
# Solution
From the hint of challenge, I assumed that this challenge was related to **cron**, which is used to schedule recurring tasks on 
Linux system.

I prioritized checking the `/etc/crontab` file instead of using `sudo crontab -e`, since the latter requires administrator 
privileges. 

This challenge was quite basic and I found the flag inside there.
