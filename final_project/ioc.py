import sys

file_name = sys.argv[1]

print "file name is: " + file_name

file = open(file_name, "r")

if file.mode != "r":
    print "Error: Could not open file"

input = file.read()



#Convert input into data structure we want
cipher_text = []
for i in range(0, len(input), 5):
    cipher_text.append(input[i:i+5])
    



for key_length in range(1,26):
    total = 0
    coincidences = 0

    for i in range(len(cipher_text)):
        for j in range(i + key_length, len(cipher_text), key_length):
            total += 1
            if(cipher_text[i] == cipher_text[j]):
                coincidences += 1
                # print "coincidence!"
                # print "i: " + str(i) + " j: " + str(j) + "char: " + cipher_text[i]

    index_of_coincidence = float(coincidences) / float(total)

    print("%3d%7.2f%% %s" % (key_length, 100 * index_of_coincidence, "#" * int(0.5 + 500 * index_of_coincidence)))
