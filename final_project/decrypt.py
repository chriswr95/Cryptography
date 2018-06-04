import sys

# Function Definitions
def char_to_binary(character):
    return "{0:05b}".format(ord(character) - 97)


# Main
file_name = sys.argv[1]
key = sys.argv[2]

file = open(file_name, "r")

if file.mode != "r":
    print "Error: Could not open file"

input = file.read()

#Convert input into data structure we want
cipher_text = []
for i in range(0, len(input), 5):
    cipher_text.append(input[i:i+5])

#Convert key into binary
