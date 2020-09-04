import random


def generate_code():
    my_hash = random.sample('123456789', 6)
    rand_value = ''.join(my_hash)
    return int(rand_value)
