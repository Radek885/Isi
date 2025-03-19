# skrypt11-25081.py

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sentence = input("WprowadŸ sentencjê: ")
    print("Odwrócona sentencja:", reverse_sentence(sentence))
