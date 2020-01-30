import random
import string

def ran_gen_a(size, chars):
    chars = string.ascii_uppercase + string.digits
    res = ''.join(random.choice(chars) for x in range(size))
    return res


if __name__ == "__main__":
    ran_gen_a