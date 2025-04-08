def check_number():
    liczba = input("Podaj łańcuch znaków: ")
    
    if len(liczba) >= 2 and all(char.isdigit() for char in liczba):
        print(f"{liczba} jest liczbą.")
    else:
        print(f"{liczba} nie jest liczbą.")

if __name__ == '__main__':
    check_number()