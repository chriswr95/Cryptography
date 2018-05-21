import sys

##def swap(a, b):
print "hi"
print sys.argv[0] + " " + sys.argv[1]


def swap(a, b):
    a, b = b, a

def main(long n,long l, key):
    S = range((2**n) - 1)

    for i in range(0, 2**n):
        j = j + S[i] + key[i]
        S[i], S[j] = S[j], S[i]
        
