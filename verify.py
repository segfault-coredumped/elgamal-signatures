"""
ElGamal Digital Signature Generation

Generates ElGamal signatures using the parameters:
p, g, g^d, d, and message x.
"""

import sys

def main():
    p = int(sys.argv[1])
    g = int(sys.argv[2])
    g_pow_d = int(sys.argv[3])
    x = int(sys.argv[4])
    r = int(sys.argv[5])
    s = int(sys.argv[6])

    # calculate LHS, RHS
    # for lhs: (g^d)^r * r^s (mod p)
    lhs = (pow(g_pow_d, r, p) * pow(r, s, p)) % p
    # for rhs: g^x (mod p)
    rhs = pow(g, x, p)

    # check if LHS = RHS, if equal print 1, else 0
    if lhs == rhs:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
