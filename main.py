import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()

    calc.add_car(calculator.Car(name="Toyota", price=30000, fuel_economy=7, service_cost=1200, insurance_cost=2500))

    calc.add_car(calculator.ElectricCar(name="Tesla", price=200000, insurance_cost=55000, power_consumption=150))

    calc.print_cars()