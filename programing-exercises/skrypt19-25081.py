# skrypt19-25081.py

def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    s = input("Wprowadü wyraz lub zdanie: ")
    print("Czy to palindrom?", is_palindrome(s))
