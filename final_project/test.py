def char_to_binary(charecter):
    return "{0:05b}".format(int(charecter) - 97))

print char_to_binary("a")
print char_to_binary("b")
print char_to_binary("z")
