def print_numbers_divisible_by_3_and_4():
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 4 == 0:
            print(i)
            count += 1
    print("Liczba znalezionych liczb:", count)

if __name__ == '__main__':
    print_numbers_divisible_by_3_and_4()
