# skrypt20-25081.py

import random

def guess_number():
    number = random.randint(1, 100)
    while True:
        guess = int(input("Zgadnij liczbê (1-100): "))
        if guess < number:
            print("Za ma³a liczba.")
        elif guess > number:
            print("Za du¿a liczba.")
        else:
            print("Gratulacje! Zgad³eœ liczbê.")
            break

if __name__ == '__main__':
    guess_number()
