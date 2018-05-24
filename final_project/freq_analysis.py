import sys

# function definitions

def binary_to_char(binary):
    return chr(int(binary, 2) + 97)

def xor(block1, block2):
    result_block = ""
    if(len(block1) != len(block2)):
        print "Error: Blocks are not the same size"
        return

    for i in range(len(block1)):
        if (block1[i] == block2[i]):
            result_block += "0"
        else:
            result_block += "1"

    return result_block

def decrypt(cipher_text, key):
    ans = []
    for i in range(len(cipher_text)):
        ans.append(xor(cipher_text[i], key))

    return ans

def frequency_analysis(plain_text):
    char_occurances = {}
    char_freqs = {}
    for i in range(len(plain_text)):
        if plain_text[i] in char_occurances.keys():
            char_occurances[plain_text[i]] += 1
        else:
            char_occurances[plain_text[i]] = 0

    for block in char_occurances:
        char_freqs[binary_to_char(block)] = char_occurances[block]

    return char_freqs

def valid_input(text):
    for i in range(len(text)):
        if int(text[i], 2) > 25:
            return False
    return True


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
