class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def beep(self):
        print ("Car {} {} make beep".format(self.brand, self.model))

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        if cars is None:
            self.cars = []
        else:
            if isinstance(cars, list):
                self.cars = cars
            else:
                print("Need list of cars")
                exit(-1)

    def __iter__(self):
        return self.cars.__iter__()

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)

    def describe(self):
        print ("There is {} cars in the garage".format(len(self.cars)))


if __name__ == '__main__':
    car1 = Car('Toyota', 'Camry')
    car2 = Car('Daewoo', 'Matiz')
    car3 = Car('Opel', 'Astra')

    garage = Garage([car1, car2, car3])
    garage.describe()

    garage.add(Car('Nissan', ''))
    garage.delete(1)

    for car in garage:
        car.beep()


