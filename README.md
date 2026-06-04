# Elgamal Digital Signature Scheme (Python)
### Overview
This project implements the **ElGamal digital signature scheme**, a public-key cryptographic system used for message authentication and integrity.

It includes both signature generation and verification using modular arithmetic over large integers
___

### Features
- ElGamal signature generation
- ElGamal signature verification
- Support for arbitrary-size integers
- Random ephemeral key generation
- Modular inverse computation
- Command-line interface

___

### Usage
### Signature Generation
`python sign.py p g public_key d x`
### Example
`python sign.py 101 2 14 10 5`
### Output
`59
35`
___

### Signature Verification
`python verify.py p g public_key x r s`
### Example
`python verify.py 101 2 14 5 59 35`
### Output
`1`
___

### Notes
This implementation is for education purposes and does not use cryptographically secure randomness
