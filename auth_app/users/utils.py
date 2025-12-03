import bcrypt


FORMAT = 'utf-8'


def make_password(raw_password):
    byte_password = raw_password.encode(FORMAT)
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte_password, salt).decode(FORMAT)


def compare_passwords(provided_password, hashed_password):
    return bcrypt.checkpw(provided_password.encode(FORMAT), hashed_password.encode(FORMAT))
