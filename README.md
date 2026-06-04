# ElGamal Digital Signature Scheme (Python)

## Overview
This project implements the ElGamal digital signature scheme for public-key authentication and message integrity using modular arithmetic over large integers.

## Features
- ElGamal signature generation
- ElGamal signature verification
- Support for arbitrary-size integers
- Random ephemeral key generation
- Modular inverse computation
- Command-line interface

## Concepts Used
- Public-key cryptography
- Digital signatures
- Modular arithmetic
- Modular exponentiation
- Modular inverses
- Randomized algorithms

## Usage

### Signature Generation
```bash
python sign.py p g public_key d x
```

Example:
```bash
python sign.py 101 2 14 10 5
```

Output:
```
59
35
```

### Signature Verification
```bash
python verify.py p g public_key x r s
```

Example:
```bash
python verify.py 101 2 14 5 59 35
```

Output:
```
1
```

## Notes
This project is intended for educational purposes to demonstrate the ElGamal signature scheme and modular arithmetic concepts. It uses non-cryptographic randomness as permitted by the assignment.
