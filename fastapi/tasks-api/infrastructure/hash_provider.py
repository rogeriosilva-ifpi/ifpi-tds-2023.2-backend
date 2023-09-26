from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'])


def hash(input: str):
    return pwd_context.hash(input)


def verify(input: str, hash_input: str):
    return pwd_context.verify(input, hash_input)
