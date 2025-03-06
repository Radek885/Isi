# skrypt4-25081.py
def find_all_substrings():
    text = input("Podaj łańcuch znaków: ")
    substring = input("Podaj ciąg do wyszukania: ")

    indices = [i for i in range(len(text)) if text.startswith(substring, i)]
    if indices:
        print(f"Wystąpienia ciągu: {indices}")
    else:
        print("Ciąg nie występuje.")

if __name__ == '__main__':
    find_all_substrings()
