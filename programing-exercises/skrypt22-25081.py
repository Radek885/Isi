def find_longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        return max(words, key=len)

def find_words_with_length(filename, length):
    with open(filename, 'r') as file:
        words = file.read().split()
        return [word for word in words if len(word) == length]

if __name__ == '__main__':
    filename = 'wordlist_10000.txt'
    print("Najdluzszy wyraz:", find_longest_word(filename))
    print("Wyrazy o dlugosci 10:", find_words_with_length(filename, 10))
