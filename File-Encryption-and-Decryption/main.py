#
# Name Vincent Leahy        
# Date 4/24/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 


#defining the cipher.

codes = {'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '&', 'c': '*',
    'D': '(', 'd': ')', 'E': '1', 'e': '2', 'F': '3', 'f': '4',
    'G': '5', 'g': '6', 'H': '7', 'h': '8', 'I': '{', 'i': '}',
    'J': '[', 'j': ']', 'K': '<', 'k': '>', 'L': '/', 'l': '|',
    'M': '$', 'm': '^', 'N': '~', 'n': '`', 'O': '-', 'o': '+',
    'P': '=', 'p': '_', 'Q': '!', 'q': '?', 'R': ':', 'r': ';',
    'S': ',', 's': '.', 'T': 'A', 't': 'B', 'U': 'C', 'u': 'D',
    'V': 'E', 'v': 'F', 'W': 'G', 'w': 'H', 'X': 'I', 'x': 'J',
    'Y': 'K', 'y': 'L', 'Z': 'M', 'z': 'N'}

# Input the file and encrypt the contents of the file.

def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    encrypted_content = ''
    for char in content:
        if char in codes:
            encrypted_content += codes[char]
        else:
            encrypted_content += char #This is to keep the punctiuations, spaces, and other charachers.

    with open(output_file, 'w') as f:
        f.write(encrypted_content)

encrypt_file('text.txt', 'encrypted.txt')

# Reverse the dictionary for decryption
decode = {v: k for k, v in codes.items()}

def decrypt_file(input_file, output_file):
    with open(input_file, 'r') as f:
        encrypted_content = f.read()

    decrypted_content = ''
    for char in encrypted_content:
        if char in decode:
            decrypted_content += decode[char]
        else:
            decrypted_content += char  # Keep spaces, punctuation, etc.

    with open(output_file, 'w') as f:
        f.write(decrypted_content)

# Example usage
decrypt_file('encrypted.txt', 'decrypted.txt')