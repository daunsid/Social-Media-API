from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hashed(password: str):
    return pwd_context.hash(password)


def verify_pass(plain_pass, hashed_pass):
    return pwd_context.verify(secret=plain_pass, hash=hashed_pass)

