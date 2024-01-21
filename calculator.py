from apis import get_gas_price, get_power_price


class Calculator:
    # Композиция
    def __init__(self, mileage=15000, years=3, year_loss=10):
        # Список машин
        # self.cars = []
        # Пробег
        self.mileage = mileage
        # Машины
        self.cars = {} # Car: Year Price
        # Владение машиной лет
        self.years = years
        # % снижения стоимости машины в год
        self.year_loss = year_loss / 100

    # Добавить машину
    def add_car(self, car):
        # Годовая стоимость каждой машины
        year_cost = car.year_cost(self.mileage)
        # Цена машины
        price_per_year = car.price / self.years
        # Текущая цена машины
        left_price = self.get_left_price(car) / self.years
        self.cars[car] = year_cost + price_per_year - left_price

    # Получить оставшуюся цену машины
    def get_left_price(self, car):
        initial_price = car.price
        for i in range(self.years):
            initial_price -= initial_price * self.year_loss
        return initial_price

    def print_cars(self):
        for car, year_price in self.cars.items():
            print(f"{car.name}:\t\t{year_price}")


class Car:
    def __init__(self, name: str, price: int, fuel_economy: float, service_cost: int, insurance_cost: int):
        # Название машины
        self.name = name
        # Цена
        self.price = price
        # Расход топлева
        self.fuel_economy = fuel_economy
        # Стоимость обслуживания годовая
        self.service_cost = service_cost
        # Стоимость страховки годовая
        self.insurance_cost = insurance_cost

    # Стоимость владения автомобиля за год(статический)
    def static_year_cost(self):
        return self.service_cost + self.insurance_cost

    # Стоимость владения автомобился за год(динамический)
    def dynamic_year_cost(self, mileage: int):
        # Расход топлива * пробег / 100 * цена топлива за литр
        return self.fuel_economy * mileage / 100 * get_gas_price()

    # Общая сумма владения автомобиля
    def year_cost(self, mileage: int):
        return self.static_year_cost() + self.dynamic_year_cost(mileage)


class ElectricCar(Car):
    def __init__(self, name: str, price: int, insurance_cost: int, power_consumption: int):
        super().__init__(name=name, price=price, fuel_economy=0, service_cost=0, insurance_cost=insurance_cost)
        # Потребляемая мощность в Вт на 1км
        self.power_consumption = power_consumption

    def dynamic_year_cost(self, mileage: int):
        # Потребляемая мощность * пробег / 1000 * цену килова электричества
        return self.power_consumption * mileage / 1000 * get_power_price()

