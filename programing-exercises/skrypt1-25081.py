def check_digit():
    znak = input("Podaj pojedynczy znak: ")[0]

    if znak.isdigit():
        print(f"{znak} jest cyfrą")
    else:
        print(f"{znak} nie jest cyfrą")

    if ord(znak) >= 48 and ord(znak) <= 57:
        print(f"{znak} jest cyfrą")
    else:
        print(f"{znak} nie jest cyfrą")

if __name__ == '__main__':
    check_digit()