import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def create_dictionary():
    return {i: generate_random_string(8) for i in range(10, 21)}

if __name__ == '__main__':
    slownik25081 = create_dictionary()
    print("Słownik:", slownik25081)