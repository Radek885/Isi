def find_substring():
    text = input("Podaj łańcuch znaków: ")
    substring = input("Podaj ciąg do wyszukania: ")

    index = text.find(substring)
    if index != -1:
        print(f"Ciąg '{substring}' znajduje się na pozycji {index}")
    else:
        print("Ciąg nie występuje.")

if __name__ == '__main__':
    find_substring()
