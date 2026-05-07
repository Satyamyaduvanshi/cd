P1 : Write a program to demonstrate sending a digitally signed document, including signing
and verification.

Code:

from cryptography.hazmat.primitives.asymmetric import rsa, padding from
cryptography.hazmat.primitives import hashes
import hashlib
import base64
print("\nGenerating RSA Key Pair")
private_key = rsa.generate_private_key(
public_exponent=65537,
key_size=2048
)
public_key = private_key.public_key()
print("PUBLIC KEY GENERATED\n")

print("Enter message to sign:")
user_input = input(">> ")
if user_input.strip() == "":
user_input = "Humpty dumpty sat on the wall"
document = user_input.encode()
print("Document:", user_input, "\n")

print("Hashing Document (SHA-256)...")
doc_hash = hashlib.sha256(document).hexdigest()
print("Hash:", doc_hash, "\n")

print("Signing Document...")
signature = private_key.sign(
document,
padding.PSS(
mgf=padding.MGF1(hashes.SHA256()),
salt_length=padding.PSS.MAX_LENGTH
),
hashes.SHA256()
)
signature_b64 = base64.b64encode(signature).decode()
print("Signature :", signature_b64[:60], "...\n")
try:
public_key.verify(
signature,

document,
padding.PSS(
mgf=padding.MGF1(hashes.SHA256()),
salt_length=padding.PSS.MAX_LENGTH ),
hashes.SHA256()
)
print("Signature VALID\n")
except Exception:
print("Signature INVALID\n")

print("Do you want to test tampering?
(y/n)") choice = input(">> ").lower()
if choice == "y":
tampered_input = input("Enter tampered message: ")
tampered_doc = tampered_input.encode()
try:
public_key.verify(
signature,
tampered_doc,
padding.PSS(
mgf=padding.MGF1(hashes.SHA256()),
salt_length=padding.PSS.MAX_LENGTH ),
hashes.SHA256()
)
print("Signature VALID (Unexpected)\n")
except Exception:
print("Signature INVALID (Tampering Detected)\n")







P2: Create a blockchain containing block hash, transaction history, time of creation

import hashlib
import datetime
import json
class Block:
def __init__(self, index, transactions, timestamp,
previous_hash): self.index = index
self.transactions = transactions
self.timestamp = timestamp
self.previous_hash = previous_hash
self.hash = self.calculate_hash()
def calculate_hash(self):
block_string = json.dumps({
"index": self.index,
"transactions": self.transactions,
"timestamp": str(self.timestamp),
"previous_hash": self.previous_hash
}, sort_keys=True).encode()
return hashlib.sha256(block_string).hexdigest()
class Blockchain:
def __init__(self):
self.chain = [self.create_genesis_block()]
def create_genesis_block(self):
return Block(0, ["Genesis Block"], datetime.datetime.now(), "0")
def get_latest_block(self):
return self.chain[-1]
def add_block(self, transactions):
latest_block = self.get_latest_block()
new_block = Block(
latest_block.index + 1,
transactions,
datetime.datetime.now(),
latest_block.hash
)
self.chain.append(new_block)
def print_chain(self):
for block in self.chain:
print(block.index)
print(block.timestamp)

print(block.transactions)
print(block.previous_hash)
print(block.hash)
print()
bc = Blockchain()
bc.add_block(["Alice pays Bob ₹500", "Bob pays Charlie ₹200"])
bc.add_block(["Charlie pays Dave ₹100"])
bc.print_chain()
Output:










LAB Exercise 3
Q1. Write a C++ program to generate SHA-256 hash using any available library.
Q2. Using SHA 256, obtain the message digest of string “Blockchain Developer”.
Q3. Generate SHA-256 hashes for:
- "Hello World"
- "Hello world"

import hashlib
def generate_sha256(text):

encoded_text = text.encode('utf-8')

sha256_hash = hashlib.sha256(encoded_text)

return sha256_hash.hexdigest()

message = input("Enter a message: ")
print("SHA-256 Hash:", generate_sha256(message))

import hashlib
text = "Blockchain Developer"
hash_value =

hashlib.sha256(text.encode()).hexdigest
() print("SHA-256 Hash:", hash_value)

import hashlib
text1 = "Hello World"
text2 = "Hello world"
hash1 =

hashlib.sha256(text1.encode()).hex
digest() hash2 =
hashlib.sha256(text2.encode()).hex
digest()
print("Hello World ->", hash1)
print("Hello world ->", hash2)











LAB Exercise 4
Q1.Write a program to generate SHA-256 hash of “Hello World”
import hashlib
# Input string
text = "Hello World"

# Generate SHA-256 hash
hash_object = hashlib.sha256(text.encode())
# Get hexadecimal digest

hash_hex = hash_object.hexdigest()
# Print result
print("Original Text:", text)
print("SHA-256 Hash:", hash_hex)










LAB Exercise 5
Use any programming language to implement the Question:
Q1. Write a program to implement RSA encryption and decryption where:
●
p = 17, q = 11
●
Choose e = 7
Perform the following:

Calculate: n and φ(n)
Find the

Encrypt the message: M = 8

Decrypt the ciphertext and verify that you get the original message.
EVERY STUDENT TAKE DIFFERENT VALUE OF "M" AND "e"

NAME : SATYAM YADAV
COURSE: BSC(HONS) COMPUTER SCIENCE

RSA Encryption and Decryption
1. Aim
To implement RSA algorithm.
2. Given Values
p = 17, q = 11, e = 7, M = 8
3. Calculations
n = 187

φ(n) = 160
d = 23
4. Encryption
C = 134
5. Decryption
M = 8
6. Code
# RSA Implementation
p = 17
q = 11
e = 7
M = 8
# Step 1
n = p * q
phi = (p - 1) * (q - 1)
# Step 2: Find d
def mod_inverse(e, phi):
for d in range(1, phi):
if (e * d) % phi == 1:
return d
d = mod_inverse(e, phi)
# Step 3: Encryption
C = pow(M, e, n)
# Step 4: Decryption
M_decrypted = pow(C, d, n)
# Output
print("p =", p, "q =", q)
print("n =", n)
print("phi(n) =", phi)
print("e =", e)
print("d =", d)
print("Original Message =", M)
print("Encrypted Message =", C)
print("Decrypted Message =", M_decrypted)

7. Output







LAB Exercise 6

Q1. Create a simple blockchain using Proof of Work (PoW) and perform the following:
- Create with transaction data (e.g., A → B, B → C, C → D).
- Set (hash must start with "00").
For each block:
●
Calculate hash
●
Perform mining (PoW)
●
Link with previous block

import hashlib
class Block:
def __init__(self, index, data, previous_hash):
self.index = index
self.data = data
self.previous_hash = previous_hash
self.nonce = 0
self.hash = self.mine_block()
def calculate_hash(self):
value = str(self.index) + self.data + self.previous_hash + str(self.nonce)
return hashlib.sha256(value.encode()).hexdigest()

def mine_block(self):
print(f"\nMining Block {self.index}...")
while True:
hash_value = self.calculate_hash()
if hash_value.startswith("00"):
print(f"Block {self.index} mined with nonce {self.nonce}")
return hash_value
else:
self.nonce += 1

class Blockchain:
def __init__(self):
self.chain = []
self.create_genesis_block()
def create_genesis_block(self):
genesis_block = Block(0, "Genesis Block", "0")
self.chain.append(genesis_block)
def add_block(self, data):
prev_block = self.chain[-1]
new_block = Block(len(self.chain), data, prev_block.hash)
self.chain.append(new_block)
def print_chain(self):
print("\n===== BLOCKCHAIN =====")
for block in self.chain:
print("\nIndex:", block.index)
print("Data:", block.data)
print("Hash:", block.hash)
print("Previous Hash:", block.previous_hash)
print("Nonce:", block.nonce)
blockchain = Blockchain()

blockchain.add_block("A -> B")
blockchain.add_block("B -> C")
blockchain.add_block("C -> D")

blockchain.print_chain()








LAB Exercise 7
Use any programming language to implement the Question:
Q1. Create a blockchain of 5 blocks, print hash of each block, and verify chain integrity.
Q2.
Tamper with 3rd block and show how validation fails.

Q2. Create a blockchain having 5 nodes and check its validity.
Question 1
class Block:
def __init__(self, index, data, previous_hash):
self.index = index
self.timestamp = time.time()
self.data = data
self.previous_hash = previous_hash
self.hash = self.calculate_hash()
def calculate_hash(self):
value = str(self.index) + str(self.timestamp) + self.data + self.previous_hash
return hashlib.sha256(value.encode()).hexdigest()
class Blockchain:
def __init__(self):
self.chain = [self.create_genesis_block()]
def create_genesis_block(self):
return Block(0, "Genesis Block", "0")
def add_block(self, data):
prev_block = self.chain[-1]
new_block = Block(len(self.chain), data, prev_block.hash)
self.chain.append(new_block)
def is_valid(self):
for i in range(1, len(self.chain)):
current = self.chain[i]
previous = self.chain[i - 1]
# Check current hash
if current.hash != current.calculate_hash():
return False
# Check chain link

if current.previous_hash != previous.hash:
return False
return True
blockchain = Blockchain()
for i in range(1, 5):
blockchain.add_block(f"Block {i} Data")
print("Blockchain Hashes")
for block in blockchain.chain:
print(f"Block {block.index} Hash: {block.hash}")
print("\nIs Blockchain Valid?", blockchain.is_valid())
print("\nTampering with Block 3...")
blockchain.chain[3].data = "Hacked Data"
blockchain.chain[3].hash = blockchain.chain[3].calculate_hash()
print("Is Blockchain Valid After Tampering?", blockchain.is_valid())



Question 2 :
class Node:
def __init__(self, name, blockchain):
self.name = name
self.blockchain = blockchain
def validate_chain(self):
return self.blockchain.is_valid()
# Create 5 nodes

nodes = []
for i in range(5):
nodes.append(Node(f"Node-{i+1}", blockchain))
# Check validity on all nodes
print("\n=== Node Validation ===")
for node in nodes:
print(f"{node.name} Validates Chain:", node.validate_chain())







LAB Exercise 8
Q1. Implement a smart contract using solidity programming language.
Q2. Create a contract to store student name and age. (Use: - string and uint )
Q3. Write a contract to transfer funds between users.
Full contract code :
Contract address: 0xd9145CCE52D386f254917e481eB44e9943F39138
Account used here:
1:0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
2:0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2
Code 👍
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract CombinedContract {
// -------------------------------
// Q1: Simple Storage
// -------------------------------
uint public storedData;
function set(uint x) public {
storedData = x;
}
function get() public view returns (uint) {
return storedData;
}
// -------------------------------

// Q2: Student Info
// -------------------------------
struct Student {
string name;
uint age;
}
Student public student;
function setStudent(string memory _name, uint _age) public {
student = Student(_name, _age);
}
function getStudent() public view returns (string memory, uint) {
return (student.name, student.age);
}
// -------------------------------
// Q3: Transfer Funds
// -------------------------------
// Deposit Ether
function deposit() public payable {}
// Check contract balance
function getBalance() public view returns (uint) {
return address(this).balance;
}
// Transfer Ether
function transferFunds(address payable _to, uint _amount) public {
require(address(this).balance >= _amount, "Insufficient
balance");
_to.transfer(_amount);
}
}
