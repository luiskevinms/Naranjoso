from security.secret_key import key
from cryptography.fernet import Fernet

fernet =Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()