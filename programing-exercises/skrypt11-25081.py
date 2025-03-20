def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sentence = input("Wprowad� sentencj�: ")
    print("Odwr�cona sentencja:", reverse_sentence(sentence))
