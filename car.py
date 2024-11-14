vin_dict = {
    1234 : ('Skoda', 'Oktavia', 2013),
    2345 : ('Lada', 'Kalina', 2005),
    3456 : ('BMW', 'X5', 2019)
}


class Car:
    def __init__(self, make, model, year):
        make = vin_dict[vin[1]]
        model = vin_dict[vin[2]]
        year = vin_dict[vin[3]]

    def get_info(self):
        return print(f'Make: {make}, Model: {model}, Year: {year}')

    @classmethod
    def from_vin(cls, vin):
        return cls


    @staticmethod
    def is_valid_year(year):
        if not 1886 < year < 2024:
            print(f'{year} неподходящий год выпуска')


Car.from_vin(1234)
Car