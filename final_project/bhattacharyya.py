import sys
from analysis import *

#Global Var
# letter frequencies contains the relative frequencies of all letters modified
# so that the minimum frezuency is 1.0
letter_frequencies = {"a":110.364864865, "c":37.5945945946, "b":20.1621621622,
    "e":171.648648649, "d":57.472972973, "g":27.2297297297, "f":30.1081081081,
    "i":94.1351351351, "h":82.3513513514, "k":10.4324324324, "j":2.06756756757,
    "m":32.5135135135, "l":54.3918918919, "o":101.445945946, "n":91.2027027027,
    "q":1.28378378378, "p":26.0675675676, "s":85.5, "r":80.9054054054,
    "u":31.8918918919, "t":122.378378378, "w":31.8918918919, "v":13.2162162162,
    "y":26.6756756757, "x":2.02702702703, "z":1.0}

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


for i in range(len(blocks)):
    column = decrypt_column(columns[column_index], blocks[i])
    if valid_input(column):
        character_frequencies = frequency_analysis(column)
        bhattacharyya_coefficient = bhattacharyya(character_frequencies, letter_frequencies)

        print "key: " + binary_to_char(blocks[i]) + " --> " + str(bhattacharyya_coefficient)
        # for char in character_frequencies.keys():
        #     print("%s %%%s" % (char, "#" * character_frequencies[char]))
