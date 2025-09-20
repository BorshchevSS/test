class Airplane:
    def __init__(self, plan_type, max_capacity, passengers=0):
        self.plane_type = plan_type
        self.max_capacity = max_capacity
        self.passengers = passengers

    # переопределение магического метода ==
    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.plane_type == other.plane_type
        return False

    # переопределение магического метода +
    def __add__(self, num):
        new_passengers = 0
        if isinstance(num, int):
            if num > 0:
                new_passengers = self.passengers + num
                if  new_passengers > self.max_capacity:
                    new_passengers = self.max_capacity
            return Airplane(self.plane_type, self.max_capacity, new_passengers)
        return self

    # переопределение магического метода -
    def __sub__(self, num):
        new_passengers = 0
        if isinstance(num, int):
            if num > 0:
                new_passengers = self.passengers - num
                if  new_passengers < self.max_capacity:
                    new_passengers = 0
            return Airplane(self.plane_type, self.max_capacity, new_passengers)
        return self

    def __str__(self):
        return f"Airplane(type={self.plane_type}, max_capacity = {self.max_capacity}, passengers = {self.passengers}"

plane1 = Airplane("SSJ", 100)
plane2 = Airplane("Boing 777", 200)
plane3 = Airplane("SSJ", 100)

print(plane1)
plane1_1 = plane3 + 10
print(plane1_1)
print(plane1 == plane3)
plane1_2 = plane1_1 - 300
print(plane1_2)

