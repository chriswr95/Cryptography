import sys
from analysis import *

# Function Definitions
def char_to_binary(character):
    return "{0:05b}".format(ord(character) - 97)


# Main
file_name = sys.argv[1]
string_key = sys.argv[2]

file = open(file_name, "r")

if file.mode != "r":
    print "Error: Could not open file"

input = file.read()
print "input: "
print input
print len(input)
#Convert input into data structure we want
cipher_text = []
for i in range(0, len(input), 5):
    print i
    cipher_text.append(input[i:i+5])

print "cipher text: "
print cipher_text
print "cipher_text length: " + str(len(cipher_text))

#Convert key into binary
key = []
print "key length: " + str(len(string_key))
for i in range(len(string_key)):
    key.append(char_to_binary(string_key[i]))

print key
#Apply key to cipher_text to get plain_text
plain_text = []
for i in range(len(cipher_text)):
    decrypted_block = xor(cipher_text[i], key[i % len(key)])
    plain_text.append(decrypted_block)

print "plain_text: "
print plain_text

string_plain_text = ""

for i in range(len(plain_text)):
    string_plain_text += binary_to_char(plain_text[i])

print string_plain_text

decrypted_file_name = "decrypted_" + file_name
plain_text_file = open(decrypted_file_name, "w")
plain_text_file.write(string_plain_text)
