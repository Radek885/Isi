def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnożenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    return a % b
