from pwn import *
import re
import math

# Sever information
host = "challenge01.root-me.org"
port = 52002

# Connect to server
io = remote(host, port)

# Read data sent from server
data = io.recv(4096).decode('utf-8')

# Find all existing numbers in the string received from server
# For example the format of server's response: 
# 
# You should tell me the answer of this math operation in less than 2 seconds !
#
# Calculate the square root of 594 and multiply by 4994 =
nums = re.findall(r'\d+', data)

# I select the two last numbers in the list due to the first number is from '2 seconds'
num1 = int(nums[1])
num2 = int(nums[2])
# Perform calculation following the instruction
result = round(math.sqrt(num1) * num2, 2)
# Send result to server, encode it again before sending
io.sendline(str(result).encode())
# Receive the flag
print(io.recvall().decode())
# Keep the connection alive
io.interactive()
