def replace_letters(sentence):
    replacements = {'o': '0', 'e': '3', 'i': '1', 'a': '4'}
    return ''.join(replacements.get(c, c) for c in sentence)

if __name__ == '__main__':
    sentence = input("Wprowad� sentencj�: ")
    print("Zmodyfikowana sentencja:", replace_letters(sentence))
