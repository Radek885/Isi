class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(f"{self.name} is barking!")

if __name__ == '__main__':
    dog1 = Dog("Burek", 3, "brown")
    dog2 = Dog("Reksio", 5, "black")
    dog3 = Dog("Azor", 2, "white")

    dog1.sound()
    dog2.sound()
    dog3.sound()
