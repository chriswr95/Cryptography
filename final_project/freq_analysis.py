import sys

# function definitions
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

def decrypt(cipher_text, block):

    for i in range(len(cipher_text)):
        cipher_text[i] = xor(cipher_text[i], block)

    return cipher_text

# Main:

file_name = sys.argv[1]
key_length = sys.argv[2]

print "file name is: " + file_name
print "key_length: " + key_length
key_length = int(key_length)

file = open(file_name, "r")

if file.mode != "r":
    print "Error: Could not open file"

input = file.read()

#Convert input into data structure we want
cipher_text = []
for i in range(0, 100, 5):
    cipher_text.append(input[i:i+5])

#convert cipher text into columns modulo key length
columns = [[] for _ in range(key_length)]

for i in range(len(cipher_text)):
    index = i % key_length
    columns[index].append(cipher_text[i])
print "Columns:"
print columns

#create all possible blocks, 0 - 25
blocks = []
for i in range(26):
    blocks.append("{0:05b}".format(i))

print "blocks:"
print blocks
