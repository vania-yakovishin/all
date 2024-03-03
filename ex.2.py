class TransportVehicle:
    def __init__(self, name, max_range):
        self.name = name
        self.max_range = max_range
    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Дальність польоту: {self.max_range} км")
vehicle1 = TransportVehicle("Літак", 12000 )
vehicle1.display_info()