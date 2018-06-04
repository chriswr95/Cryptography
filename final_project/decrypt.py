import sys

# Function Definitions
def char_to_binary(char):
    return "{0:05b}".format(int(char) - 97))


# Main
file_name = sys.argv[1]
key = sys.argv[2]
