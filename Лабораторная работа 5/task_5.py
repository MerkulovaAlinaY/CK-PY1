import random
import string


def get_random_password(n) -> str:
    password = "".join(random.sample((string.ascii_lowercase + string.ascii_uppercase + string.digits), k=n))
    return password


print(get_random_password(8))