class Vehicle:
    def __init__(self, name, year, mileage):
        self.name = name
        self.year = year
        self.mileage = mileage

    @property
    def is_old(self):
        return 2023 - self.year > 10

    @property
    def is_long_mileage(self):
        return self.mileage > 100000

class Car(Vehicle):
    def __init__(self, name, year, mileage):
        super().__init__(name, year, mileage)

if __name__ == '__main__':
    vehicle = Vehicle("Toyota", 2005, 120000)
    car1 = Car("Honda", 2015, 80000)
    car2 = Car("Ford", 2010, 150000)

    print(f"{vehicle.name} is old: {vehicle.is_old}, long mileage: {vehicle.is_long_mileage}")
    print(f"{car1.name} is old: {car1.is_old}, long mileage: {car1.is_long_mileage}")
    print(f"{car2.name} is old: {car2.is_old}, long mileage: {car2.is_long_mileage}")
