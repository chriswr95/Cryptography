import sys
from analysis import *

# function definitions



# Main:

file_name = sys.argv[1]
key_length = sys.argv[2]
column_index = int(sys.argv[3])

print "file name is: " + file_name
print "key_length: " + key_length
key_length = int(key_length)

file = open(file_name, "r")

if file.mode != "r":
    print "Error: Could not open file"

input = file.read()

#Convert input into data structure we want
cipher_text = []
for i in range(0, len(input), 5):
    cipher_text.append(input[i:i+5])

#convert cipher text into columns modulo key length
columns = [[] for _ in range(key_length)]

for i in range(len(cipher_text)):
    index = i % key_length
    columns[index].append(cipher_text[i])


#create all possible blocks, 0 - 25
blocks = []
for i in range(26):
    blocks.append("{0:05b}".format(i))

#Test Case
# print "COLUMN BEFORE DECRYPTION:"
# print columns[column_index]
for i in range(len(blocks)):
    column = decrypt(columns[column_index], blocks[i])
    if valid_input(column):
        character_frequencies = frequency_analysis(column)
        tot_eta = 0
        if "e" in character_frequencies.keys():
            tot_eta += character_frequencies["e"]
        if "t" in character_frequencies.keys():
            tot_eta += character_frequencies["t"]
        if "a" in character_frequencies.keys():
            tot_eta += character_frequencies["a"]

        print "key: " + binary_to_char(blocks[i]) + " --> " + str(tot_eta)
        # for char in character_frequencies.keys():
        #     print("%s %%%s" % (char, "#" * character_frequencies[char]))
