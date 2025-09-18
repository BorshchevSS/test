class Transport:
    def __init__(self, speed, color, brand):
        self.speed = speed
        self.color = color
        self.brand = brand

    def sound(self):
        print(f"Beep beep")


class Car(Transport):
    def __init__(self, speed, color, brand, seats):
        super().__init__(speed, color, brand)
        self.seats = seats

    def beeeeep(self):
        print("Какой-то звук")

    #Переопределение метода родительского класса
    def sound(self):
        print(f"Beep!!!")

car = Car(250, "red", "bmw", 3)
print(car.color)
car.sound()
car.beeeeep()