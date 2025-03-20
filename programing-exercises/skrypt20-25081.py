import random

def guess_number():
    number = random.randint(1, 100)
    while True:
        guess = int(input("Zgadnij liczb� (1-100): "))
        if guess < number:
            print("Za ma�a liczba.")
        elif guess > number:
            print("Za du�a liczba.")
        else:
            print("Gratulacje! Zgad�e� liczb�.")
            break

if __name__ == '__main__':
    guess_number()
