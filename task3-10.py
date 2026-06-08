class Parking:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cars = 0

    def check_status(self):
        print(f"Зайнято місць: {self.cars}/{self.capacity}")

    def enter_car(self):
        if self.cars >= self.capacity:
            print("Паркінг заповнений. В'їзд неможливий.")
            return False

        self.cars += 1
        print("Автомобіль заїхав.")
        return True

    def exit_car(self):
        if self.cars <= 0:
            print("Паркінг порожній.")
            return False

        self.cars -= 1
        print("Автомобіль виїхав.")
        return True


if __name__ == "__main__":
    parking = Parking(capacity=3)

    parking.check_status()

    parking.enter_car()
    parking.enter_car()
    parking.enter_car()
    parking.enter_car()  # перевищення ліміту

    parking.check_status()

    parking.exit_car()
    parking.exit_car()

    parking.check_status()