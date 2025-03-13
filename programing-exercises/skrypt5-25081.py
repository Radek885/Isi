# skrypt5-25081.py
import math

def metoda_podzialu(x):
    a = 0
    b = 0

    for i in range(0, 257):
        if i*i >= x:
            a = pow(i,2)
            b = pow((i-1),2)
            break
    print("pierwiastek jest pomiędzy ", a," ",b)  

    while abs(x-pow(a,2)) > 0.001:
        if x > pow((a+b)/2,2):
            b = (a+b)/2
        else:
            a = (a+b)/2
    
    return a

# Sposób 1: List comprehension
def find_square_roots():
    numbers = [i for i in range(1, 257) if i % 2 == 0]
    square_roots = [math.sqrt(i) for i in numbers]
    print("Metoda 1:")
    print(square_roots)

# Sposób 2: Metoda równego podziału
    numbers = [i for i in range(1, 257) if i % 2 == 0]
    square_roots = [metoda_podzialu(i) for i in numbers]
    print("Metoda 2:")
    print(square_roots)

if __name__ == '__main__':
    find_square_roots()
