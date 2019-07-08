# Public  = membername
# Protected = _membername.       can be used in derived class
# Private = __membername     can be used in derived class


class Car():
    numWheels = "4"
    _color = "Black"
    __yearofManufacture = "2017"


class bmw(Car):
    def __init__(self):
        print("(Protected) color of car:", self._color)


car = Car()
print("(Public) number of wheels:", car.numWheels)
bmw = bmw()
print("(Private) year of manufacture", car._Car__yearofManufacture)
