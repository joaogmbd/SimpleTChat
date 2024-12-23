import random
import string

def generate_username():
    return "User" + "".join(random.choices(string.digits, k=4))
