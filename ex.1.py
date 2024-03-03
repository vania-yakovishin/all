class TransportVehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Максимальна швидкість: {self.max_speed} км/год")
vehicle1 = TransportVehicle("Автомобіль", 200)
vehicle1.display_info()