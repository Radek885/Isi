import random
import string

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_passwords(num_passwords, length):
    return [generate_password(length) for _ in range(num_passwords)]

def write_to_file(filename, passwords):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

if __name__ == '__main__':
    passwords = generate_passwords(1000, 6)
    write_to_file('passwords.txt', passwords)
