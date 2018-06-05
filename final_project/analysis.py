import string
import math

def binary_to_char(binary):
    return chr(int(binary, 2) + 97)

def char_to_binary(character):
    return "{0:05b}".format(ord(character) - 97)

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

def decrypt_column(cipher_text, key):
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

    for letter in string.ascii_lowercase:
        if char_to_binary(letter) in char_occurances.keys():
            char_freqs[letter] = char_occurances[char_to_binary(letter)]
        else:
            char_freqs[letter] = 0

    return char_freqs

def valid_input(text):
    for i in range(len(text)):
        if int(text[i], 2) > 25:
            return False
    return True

#note only works on distributions of lowercase ascii letters
def bhattacharyya(dist1, dist2):
    bhattacharyya_coefficient = 0
    for letter in string.ascii_lowercase:
        bhattacharyya_coefficient += math.sqrt(dist1[letter] * dist2[letter])

    return bhattacharyya_coefficient
