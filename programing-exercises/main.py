# main.py

from funkcje import dodawanie, odejmowanie, mnozenie, dzielenie, modulo

if __name__ == '__main__':
    a, b = 10, 3
    print("Dodawanie:", dodawanie(a, b))
    print("Odejmowanie:", odejmowanie(a, b))
    print("Mno¿enie:", mnozenie(a, b))
    print("Dzielenie:", dzielenie(a, b))
    print("Modulo:", modulo(a, b))
