# skrypt15-25081.py

def add_numbers_divisible_by_3_or_5():
    numbers = []
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
    return numbers

if __name__ == '__main__':
    numbers = add_numbers_divisible_by_3_or_5()
    print("Liczby podzielne przez 3 lub 5:", numbers)
