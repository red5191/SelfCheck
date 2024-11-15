vin_dict = {
    '1234' : ('Skoda', 'Oktavia', 2013),
    '2345' : ('Lada', 'Kalina', 2005),
    '3456' : ('BMW', 'X5', 2019)
}


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return print(f'Make: {self.make}, Model: {self.model}, Year: {self.year}')

    @classmethod
    def from_vin(cls, vin):
       return cls(vin_dict.get(vin)[0], vin_dict.get(vin)[1], vin_dict.get(vin)[2])

    @staticmethod
    def is_valid_year(year):
        if not 1886 < year < 2024:
            print(f'{year} неподходящий год выпуска')
        else:
            print(f'{year} подходящий год выпуска')

car1 = Car.from_vin('1234')
car1.get_info()