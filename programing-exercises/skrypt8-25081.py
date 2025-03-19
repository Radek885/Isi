import random
import string
from collections import Counter

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def create_dictionary(s):
    return Counter(s)

def create_tuple_list(dictionary):
    return list(dictionary.items())

if __name__ == '__main__':
    random_string = generate_random_string(100)
    dictionary = create_dictionary(random_string)
    tuple_list = create_tuple_list(dictionary)
    print("Slownik:", dictionary)
    print("Lista krotek:", tuple_list)
