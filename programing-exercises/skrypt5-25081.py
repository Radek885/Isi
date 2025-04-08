import math

def find_roots_method1():
    return [math.sqrt(i) for i in range(1, 257) if i % 2 == 0]

def find_roots_method2():
    roots = []
    for i in range(1, 257):
        if i % 2 == 0:
            roots.append(math.sqrt(i))
    return roots

if __name__ == '__main__':
    print("Metoda 1:", find_roots_method1())
    print("Metoda 2:", find_roots_method2())