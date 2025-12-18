#!/usr/bin/env python3
"""Decrypt `encrypted_seed.txt` locally using `student_private.pem` and print the hex seed."""
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

PRIV = 'student_private.pem'
ENC = 'encrypted_seed.txt'

def main():
    with open(PRIV, 'rb') as f:
        priv = serialization.load_pem_private_key(f.read(), password=None)
    with open(ENC, 'r') as f:
        enc_b64 = f.read().strip()
    ct = base64.b64decode(enc_b64)
    pt = priv.decrypt(
        ct,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    hex_seed = pt.decode('utf-8')
    print(hex_seed)
    with open('decrypted_seed.txt', 'w') as f:
        f.write(hex_seed)

if __name__ == '__main__':
    main()
