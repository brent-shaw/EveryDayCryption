# Decrypt one or more files

import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import argparse
import getpass

def makeKey(password_provided):
    password = password_provided.encode()
    salt = b'ThisIsNotAPasswordItsASalt!'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def decryptFile(filename, password):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fernet = Fernet(makeKey(password))
    output_file = fernet.decrypt(filename.encode())

    with open(filename, 'rb') as f:
        data = f.read()

    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

    os.remove(filename)

    print(filename+' decrypted to '+output_file.decode())

parser = argparse.ArgumentParser(description='Decrypt files.')
parser.add_argument('files', metavar='F', type=str, nargs='+',
                    help='file to be decrypted')

args = parser.parse_args()
password = getpass.getpass('Password for file decryption:')
for filename in args.files:
    if filename.endswith('.encrypted'):
        decryptFile(filename, password)
