class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print(f"{self.name} is barking!")

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print(f"{self.name} is meowing!")

class Fox(Animal):
    def sound(self):
        print(f"{self.name} is yelping!")

if __name__ == '__main__':
    dog = Dog("Burek", 3, "male", "Labrador")
    cat = Cat("Mruczek", 2, "female", "Persian")
    fox = Fox("Lis", 4, "male")

    dog.sound()
    cat.sound()
    fox.sound()
