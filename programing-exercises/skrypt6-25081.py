# skrypt6-25081.py
import random
import string

def create_random_dict():
    my_dict = {}
    for i in range(10, 21):
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        my_dict[i] = value
    print(my_dict)

if __name__ == '__main__':
    create_random_dict()
