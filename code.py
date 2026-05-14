5. Implement caesar cipher substitution operation. 
CODE-
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - start + shift) % 26 + start)
        else:
            result += ch
    return result
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
msg = input("Enter message: ")
shift = int(input("Enter shift: "))
enc = caesar_encrypt(msg, shift)
print("Encrypted:", enc)
dec = caesar_decrypt(enc, shift)
print("Decrypted:", dec)
 
OUTPUT - 




6. Implement monoalphabetic and polyalphabetic cipher substitution operation. 
CODE-
#monoalphabetic
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
def mono_encrypt(text):
    result = ""
    for ch in text.upper():
        if ch in alphabet:
            result += key[alphabet.index(ch)]
        else:
            result += ch
    return result


def mono_decrypt(text):
    result = ""
    for ch in text.upper():
        if ch in key:
            result += alphabet[key.index(ch)]
        else:
            result += ch
    return result


msg = input("Enter message: ")
enc = mono_encrypt(msg)
print("Encrypted:", enc)
dec = mono_decrypt(enc)
print("Decrypted:", dec)
 
OUTPUT- 

# polyalphabetic
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    k = 0
    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[k % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            k += 1
        else:
            result += ch
    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    k = 0
    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[k % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            k += 1
        else:
            result += ch
    return result


msg = input("Enter message: ")
key = input("Enter key: ")
enc = vigenere_encrypt(msg, key)
print("Encrypted:", enc)
dec = vigenere_decrypt(enc, key)
print("Decrypted:", dec)



OUTPUT -
 


7. Implement playfair cipher substitution operation.
CODE-
def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    for ch in key:
        if ch not in used and ch.isalpha():
            matrix.append(ch)
            used.add(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)]
def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
def prepare(text):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))
    if len(text) % 2 != 0:
        text += 'X'
    return text
def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1+1)%5]
            result += matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1]
            result += matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result
def playfair_decrypt(text, key):
    matrix = generate_matrix(key)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1-1)%5]
            result += matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1]
            result += matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result


msg = input("Enter message: ")
key = input("Enter key: ")
enc = playfair_encrypt(msg, key)
print("Encrypted:", enc)
dec = playfair_decrypt(enc, key)
print("Decrypted:", dec)
OUTPUT- 



8. Implement hill cipher substitution operation. 
CODE-
import numpy as np
key = np.array([[3, 3],
                [2, 5]])
inverse_key = np.array([[15, 17],
                        [20, 9]])
def hill_encrypt(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        pair = [
            ord(text[i]) - 65,
            ord(text[i+1]) - 65
        ]
        enc = np.dot(key, pair) % 26
        result += chr(int(enc[0]) + 65)
        result += chr(int(enc[1]) + 65)
    return result
def hill_decrypt(text):
    result = ""
    for i in range(0, len(text), 2):
        pair = [
            ord(text[i]) - 65,
            ord(text[i+1]) - 65
        ]
        dec = np.dot(inverse_key, pair) % 26
        result += chr(int(dec[0]) + 65)
        result += chr(int(dec[1]) + 65)
    return result
msg = input("Enter message: ")
enc = hill_encrypt(msg)
print("Encrypted:", enc)
dec = hill_decrypt(enc)
print("Decrypted:", dec)
OUTPUT-



9. Implement rail fence cipher transposition operation.
CODE-
def encrypt(text, key):
    rail = ['' for _ in range(key)]
    row, step = 0, 1
    for ch in text:
        rail[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return ''.join(rail)
def decrypt(cipher, key):
    n = len(cipher)
    rail = [['' for _ in range(n)] for _ in range(key)]
    row, step = 0, 1
    for i in range(n):
        rail[row][i] = '*'
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    index = 0
    for i in range(key):
        for j in range(n):
            if rail[i][j] == '*':
                rail[i][j] = cipher[index]
                index += 1
    # read
    result = ''
    row, step = 0, 1
    for i in range(n):
        result += rail[row][i]
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return result
txt=input(str("enter the text: "))
k=int(input("enter the key: "))
print("original text = ", txt)
p=encrypt(txt,k)
print("encrypted text = ", p)
print("decrypted text = ", decrypt(p,k))
Output:- 
  
10. Implement row transposition cipher transposition operation. 
CODE-
def row_encrypt(text, key):
    cols = len(key)
    rows = -(-len(text) // cols)
    text += 'X' * (rows * cols - len(text))
    matrix = [list(text[i:i+cols]) for i in range(0, len(text), cols)]
    order = sorted(range(cols), key=lambda x: key[x])
    return ''.join(matrix[r][c] for c in order for r in range(rows))
def row_decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols
    order = sorted(range(cols), key=lambda x: key[x])
    matrix = [[''] * cols for _ in range(rows)]
    index = 0
    for c in order:
        for r in range(rows):
            matrix[r][c] = cipher[index]
            index += 1
    return ''.join(matrix[r][c] for r in range(rows) for c in range(cols))
text=input(str("enter the text: "))
keY=int(input("enter the key: "))
print("original text = ", text)
p=row_encrypt(text, key)
print("encrypted text = ", p)
print("decrypted text = ", row_decrypt(cipher, key))
OUTPUT-
enter the text: hello
enter the key: 1234
original text =  hello
encrypted text =  eXlXholX
decrypted text =  HELLOWORLDXX  
11. Implement product cipher transposition operation. 
CODE-
# Product Cipher using Double Transposition
def transpose_encrypt(text, key):
    result = ""
    for col in range(key):
        pointer = col
        while pointer < len(text):
            result += text[pointer]
            pointer += key
    return result


def transpose_decrypt(cipher, key):
    n = len(cipher)
    rows = (n + key - 1) // key
    grid = [''] * n
    index = 0
    for col in range(key):
        pointer = col
        while pointer < n:
            grid[pointer] = cipher[index]
            index += 1
            pointer += key
    return ''.join(grid)


# Input
message = input("Enter message: ")
key1 = 4
key2 = 3
# Encryption
step1 = transpose_encrypt(message, key1)
cipher = transpose_encrypt(step1, key2)
print("Encrypted Text:", cipher)
# Decryption
step2 = transpose_decrypt(cipher, key2)
plain = transpose_decrypt(step2, key1)
print("Decrypted Text:", plain)
OUTPUT-
 
