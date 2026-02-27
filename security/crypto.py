from security.secret_key import key
from cryptography.fernet import Fernet, InvalidToken

fernet = Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    try:
        return fernet.decrypt(value.encode()).decode()
    except InvalidToken:
        return value