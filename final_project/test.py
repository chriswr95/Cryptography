# Function definitions
def char_to_binary(character):
    return "{0:05b}".format(ord(character) - 97)

#main
print char_to_binary("a")
print char_to_binary("b")
print char_to_binary("z")
