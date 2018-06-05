import sys
from analysis import *

#Main Function

file_name = sys.argv[1]
key_length = sys.argv[2]
column_index = int(sys.argv[3])

print "file name is: " + file_name
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

#INCOMPLETE
