import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()

    calc.add_car(calculator.Car(name="Toyota", price=30000, fuel_economy=7, service_cost=1200, insurance_cost=2500))

    calc.add_car(calculator.Car(name="BMW", price=30000, fuel_economy=7, service_cost=1200, insurance_cost=2500))

    calc.print_cars()