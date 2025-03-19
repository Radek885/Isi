# skrypt13-25081.py

def print_numbers_not_divisible_by_3():
    for i in range(1, 51):
        if i % 3 != 0:
            print(i)

if __name__ == '__main__':
    print_numbers_not_divisible_by_3()
