import random

def guess_number():
    number = random.randint(1, 100)
    while True:
        guess = int(input("Zgadnij liczbe w zakresie od 1 do 100): "))
        if guess < number:
            print("Za mala liczba.")
        elif guess > number:
            print("Za duza liczba.")
        else:
            print("Gratulacje! Zgadles liczbe.")
            break

if __name__ == '__main__':
    guess_number()
