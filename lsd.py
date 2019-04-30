# List original filenames

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

def demystifyFilename(filename, password):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fernet = Fernet(makeKey(password))
    return fernet.decrypt(filename[:-10].encode()).decode()


password = getpass.getpass('Password used for encryption:')

for root, dirs, files in os.walk("."):  
    for filename in files:
        if filename.endswith('.encrypted'):
            print("{0: <20} : {1: <80}".format(demystifyFilename(filename,password),filename))