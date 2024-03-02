file1 = open('enc', 'r')
encoded_string = file1.read()

decoded_string = ""
for i in range(0, len(encoded_string), 1):
    combined_value = ord(encoded_string[i])
    first_char_value = combined_value >> 8  # Extract the first character
    second_char_value = combined_value & 0xFF  # Extract the second character
    decoded_string += chr(first_char_value) + chr(second_char_value)

print(decoded_string)