# skrypt5-25081.py
import math

# Sposób 1: List comprehension
def find_square_roots():
    numbers = [i for i in range(1, 257) if i % 2 == 0]
    square_roots = [math.sqrt(i) for i in numbers]
    print(square_roots)

if __name__ == '__main__':
    find_square_roots()
