class Airplane:
    def __init__(self, plane_type, max_capacity, passengers=0):
        self.plane_type = plane_type
        self.max_capacity = max_capacity
        self.passengers = passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.plane_type == other.plane_type
        return False
# print(isinstance(5, str))

    def __add__(self, num):
        new_passengers = 0
        if isinstance(num, int):
            if num > 0:
                new_passengers = self.passengers + num
                if new_passengers > self.max_capacity:
                    new_passengers = self.max_capacity
            return Airplane(self.plane_type, self.max_capacity, new_passengers)
        return self

    def __sub__(self, num):
        new_passengers = 0
        if isinstance(num, int):
            new_passengers = self.passengers - num
            if new_passengers < 0:
                new_passengers = 0
            return Airplane(self.plane_type, self.max_capacity, new_passengers)
        return self
    # __iadd__
    # __isub__

    def __gt__(self, other):
        return self.max_capacity > other.max_capacity

    def __lt__(self, other):
        return self.max_capacity < other.max_capacity

    def __str__(self):
        return (f'Airplane(type={self.plane_type},'
                f'max_capacity={self.max_capacity},'
                f'passengers={self.passengers})')

plane1 = Airplane('Boeing 777', 366)
plane2 = Airplane('Airbus A490', 850)
plane3 = Airplane('Boeing 777', 450)

print(plane1 == plane2)#False
print(plane1 == plane3)#True

print(plane1 + 100)
print(plane1 - 100)

print(plane1 > plane2)
print(plane1 < plane2)
print(plane1 > plane3)
plane1 +=  4
print(plane1)





