from car import Car

car2 = Car('Mazda', 'RX-7', 1978)
car2.get_info()

car3 = Car.from_vin('2345')
car3.get_info()

Car.is_valid_year(2005)
