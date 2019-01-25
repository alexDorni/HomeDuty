import binascii
import hashlib
import os


# Crypt the password
def crypt_password(item):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    pwd_hash = hashlib.pbkdf2_hmac('sha512',
                                   item.encode('utf-8'),
                                   salt,
                                   100000)
    pwd_hash = binascii.hexlify(pwd_hash)

    # Return ascii code
    return (salt + pwd_hash).decode('ascii')


# Decrypt the password
def verify_password(hashed_password, provided_password):
    salt = hashed_password[:64]
    stored_password = hashed_password[64:]

    pwd_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'),
                                   salt.encode('ascii'), 100000)

    pwd_hash = binascii.hexlify(pwd_hash).decode('ascii')

    # Return a bool
    return pwd_hash == stored_password
