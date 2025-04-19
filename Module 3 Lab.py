class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model 
        self.doors = doors
        self.roof = roof

    def display_info (self):
        print("n---- Vehicle Information ----")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of Doors: {self.doors}")
        print(f"Type of roof: {self.roof}")
def main():
    print("Enter information for your car:")
    vehicle_type = "car"  # Automatically set
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")
    user_car = Automobile(vehicle_type, year, make, model, doors, roof)
    user_car.display_info()


main()