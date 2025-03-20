def generate_alphabet():
    return ''.join(chr(i) for i in range(ord('a'), ord('z')+1))

def write_to_file(filename, content, mode='w'):
    with open(filename, mode) as file:
        file.write(content)

if __name__ == '__main__':
    alphabet = generate_alphabet()
    write_to_file('alfabet1-25081.txt', alphabet)
    write_to_file('alfabet2-25081.txt', '\n'.join(alphabet))
