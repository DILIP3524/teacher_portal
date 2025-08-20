import os
import hashlib
import binascii
import time
import hmac

SESSION_TOKENS = {}


def generate_session_token():
    raw = os.urandom(32)
    stamp = str(int(time.time()))
    return binascii.hexlify(raw).decode() + '.' + stamp


def hash_password(password: str):
    salt = os.urandom(16)
    pwd = password.encode("utf-8")
    pwd_hashed = hashlib.pbkdf2_hmac("sha256", pwd, salt, 100000)
    return binascii.hexlify(pwd_hashed).decode() , binascii.hexlify(salt).decode()


def verify_password(stored_hash, salt, provided_password):
    salt_bytes = binascii.unhexlify(salt)
    hash_bytes = binascii.unhexlify(stored_hash)
    new_hash = hashlib.pbkdf2_hmac("sha256", provided_password.encode("utf-8"), salt_bytes, 100000)
    return hmac.compare_digest(new_hash, hash_bytes)


def create_session(user_id):
    token = generate_session_token()
    SESSION_TOKENS[token] = {"user_id": user_id, 
                             "expires": time.time() + 3600}
    return token


def get_session_user(token):
    info = SESSION_TOKENS.get(token)
    if not info:
        return None
    if time.time() > info["expires"]:
        del SESSION_TOKENS[token]
        return None
    return info["user_id"]


def delete_session(token):
    if token in SESSION_TOKENS:
        del SESSION_TOKENS[token]


# hashed = hash_password("Ninja3524@")
# print(hashed)


