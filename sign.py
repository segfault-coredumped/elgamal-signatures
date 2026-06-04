"""
ElGamal Digital Signature Generation

Generates ElGamal signatures using the parameters:
p, g, g^d, d, and message x.
"""

import sys
import random
import math

def random_e(pval, num_p_bits):
    # keep trying until valid value of e is found
    while True:
        # generate p random bits
        e = random.getrandbits(num_p_bits)

        # check if e is within range (0 < e < p-1)
        if 0 < e < pval:
            # check if coprime
            if math.gcd(e, pval) == 1:
                return e
            
def main():
    # define p, g, g^d, d, x as values taken from command line
    p = int(sys.argv[1])
    g = int(sys.argv[2])
    g_pow_d = int(sys.argv[3])
    d = int(sys.argv[4])
    x = int(sys.argv[5])

    # max range is p-1
    pval = p-1

    # get num bits in p
    num_p_bits = p.bit_length()

    # call function to get random e based on pval and number of p bits
    e = random_e(pval, num_p_bits)

    # calculate inverse of e (mod p-1)
    e_inverse = pow(e, -1, pval)

    # calculate r where r = g^e mod p
    r = pow(g, e, p)

    # calculate s where s = (x - d * r) * e^-1 (mod p-1)
    s = ((x-d*r) * e_inverse) % pval

    # output (r,s)
    print(r)
    print(s)


if __name__ == "__main__":
    main()



