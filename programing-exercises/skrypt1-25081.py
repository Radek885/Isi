# skrypt1-25081.py
def check_digit():
    znak = input("Podaj pojedynczy znak: ")[0]

    # Sposób 1: Funkcja isdigit()
    if znak.isdigit():
        print(f"{znak} jest cyfrą")
    else:
        print(f"{znak} nie jest cyfrą")

    # Sposób 2: Funkcja isinstance()
    if isinstance(znak, int):
        print(f"{znak} jest cyfrą")
    else:
        print(f"{znak} nie jest cyfrą")

if __name__ == '__main__':
    check_digit()