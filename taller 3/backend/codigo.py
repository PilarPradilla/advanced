"""
This file contains the code for a menu which can add vehicle
information and display the registered information.

Author: Maria del Pilar Pradilla Cely
"""

#==================== Class Engine ===============================
class Engine:
    """
    This is a class about the vehicle engine.

    Attributes:
    - type (str): The type of engine.
    - potency (float): The potency of the engine.
    - weight (float): The weight of the engine.

    Methods:
    - __init__(): This is the constructor method of the class.
    - __str__(): This is the toString method of the class.
    """
    def __init__(self, type: str, potency: float, weight: float):
        self.type = type
        self.potency = potency
        self.weight = weight

    def __str__(self) -> str:
        return f"(Type: {self.type}, Potency: {self.potency}, Weight: {self.weight})"

#==================== Class Vehicle ===============================
class Vehicle:
    """
    This is a class about the vehicle.

    Attributes:
    - engine (Engine): The engine of the vehicle.
    - chasis (str): The type of chassis (A or B).
    - model (str): The model of the vehicle.
    - year (int): The manufacturing year of the vehicle.
    - gas_consumption (float): The calculated gas consumption of the vehicle.

    Methods:
    - __init__(): This is the constructor method of the class.
    - calculate_gas_consumption(): This method calculates the gas consumption.
    - __str__(): This is the toString method of the class.
    """
    def __init__(self, engine: Engine, chasis: str, model: str, year: int):
        if chasis not in ["A", "B"]:
            raise ValueError("This chasis is not valid.")
        self.engine = engine
        self.chasis = chasis
        self.model = model
        self.year = year
        self.gas_consumption = self.calculate_gas_consumption()

    def calculate_gas_consumption(self) -> float:
        """
        This method calculates the gas consumption.
        Returns:
        - float: The gas consumption of the vehicle.
        """
        if self.chasis == 'A':
            gas_consumption = 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.3
        elif self.chasis == 'B':
            gas_consumption = 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.5
        return gas_consumption

    def __str__(self) -> str:
        return (f"Engine: {self.engine}, Chasis: {self.chasis}, Model: {self.model}, "
                f"Gas consumption: {self.gas_consumption}, Year: {self.year}")

#==================== Class Car ===============================
class Car(Vehicle):
    """
    This is a class about the vehicle car.

    Attributes:
    - color (str): The color of the car.

    Methods:
    - __init__(): This is the constructor method of the class.
    - __str__(): This is the toString method of the class.
    """
    def __init__(self, engine, chasis, model, year, color: str):
        super().__init__(engine, chasis, model, year)
        self.color = color

    def __str__(self) -> str:
        return f"Car = {super().__str__()}, Color: {self.color}"

#==================== Class Truck ===============================
class Truck(Vehicle):
    """
    This is a class about the vehicle truck.

    Methods:
    - __init__(): This is the constructor method of the class.
    - __str__(): This is the toString method of the class.
    """
    def __init__(self, engine, chasis, model, year):
        super().__init__(engine, chasis, model, year)

    def __str__(self) -> str:
        return f"Truck = {super().__str__()}"

#==================== Class Yacht ===============================
class Yacht(Vehicle):
    """
    This is a class about the vehicle yacht.

    Attributes:
    - passenger_capacity (int): The passenger capacity of the yacht.

    Methods:
    - __init__(): This is the constructor method of the class.
    - __str__(): This is the toString method of the class.
    """
    def __init__(self, engine, chasis, model, year, passenger_capacity: int):
        super().__init__(engine, chasis, model, year)
        self.passenger_capacity = passenger_capacity

    def __str__(self) -> str:
        return f"Yacht = {super().__str__()}, Passenger capacity: {self.passenger_capacity}"

#==================== Class Motorcycle ===============================
class Motorcycle(Vehicle):
    """
    This is a class about the vehicle motorcycle.

    Methods:
    - __init__(): This is the constructor method of the class.
    - __str__(): This is the toString method of the class.
    """
    def __init__(self, engine, chasis, model, year):
        super().__init__(engine, chasis, model, year)

    def __str__(self) -> str:
        return f"Motorcycle = {super().__str__()}"

#==================== Functions to search vehicles ===============================
def search(attribute):
    """
    This function searches for vehicles of a specific type in the list_vehicles.

    Args:
    - attribute (type): The type of vehicle to search for (e.g., Car, Truck, Yacht, Motorcycle).
    """
    for vehicle in list_vehicles:
        if isinstance(vehicle, attribute):
            print(vehicle)

def search_model(attribute):
    """
    This function searches for vehicles with a specific model in the list_vehicles.

    Args:
    - attribute (str): The model of the vehicle to search for.
    """
    for vehicle in list_vehicles:
        if vehicle.model == attribute:
            print(vehicle)

def search_chassis(attribute):
    """
    This function searches for vehicles with a specific chassis type in the list_vehicles.

    Args:
    - attribute (str): The chassis type of the vehicle to search for (A or B).
    """
    for vehicle in list_vehicles:
        if vehicle.chasis == attribute:
            print(vehicle)

def search_year(attribute):
    """
    This function searches for vehicles from a specific year in the list_vehicles.

    Args:
    - attribute (int): The year of the vehicle to search for.
    """
    for vehicle in list_vehicles:
        if vehicle.year == attribute:
            print(vehicle)

# List of registered vehicles
list_vehicles = [
    Car(Engine("jd", 34, 434), "A", "x", 343, "black"),
    Truck(Engine("jd", 34, 434), "A", "x", 2015)
]

# Dictionary of administrators
admins = {
    "Pablo": "pablo123",
    "Mario": "password123"
}

#===============Menu===================
print("""Do you want to log in as an administrator or as an external user?
1. Administrator
2. External user""")
try:
    aux1 = int(input("Enter the number of the action you want to perform: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

valid = False

if aux1 == 1:
    username = input("Username: ")
    password = input("Password: ")
    if username in admins and admins[username] == password:
        valid = True

print("""Menu:
1. Catalog.
2. Search vehicle.
3. Add Vehicles""")
try:
    aux2 = int(input("Enter the number of the action you want to perform: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Add Vehicles as Administrator
if aux1 == 1 and aux2 == 3 and valid:
    print("""Which vehicle do you want to add?
    1. Car
    2. Truck
    3. Yacht
    4. Motorcycle
    """)
    try:
        aux = int(input("Enter the number of the vehicle: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()

    try:
        engine_type = input("What is the type of vehicle engine? ")
        engine_potency = float(input("What is the potency of the vehicle engine? "))
        engine_weight = float(input("What is the weight of the vehicle engine? "))
        chasis = input("What is the type of chassis? (A or B) ")
        model = input("What is the model of the vehicle? ")
        year = int(input("What is the year of the vehicle? "))
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
        exit()

    try:
        if aux == 1:
            color = input("What is the color of the car? ")
            car = Car(Engine(engine_type, engine_potency, engine_weight), chasis, model, year, color)
            list_vehicles.append(car)
        elif aux == 2:
            truck = Truck(Engine(engine_type, engine_potency, engine_weight), chasis, model, year)
            list_vehicles.append(truck)
        elif aux == 3:
            passenger_capacity = int(input("What is the passenger capacity of the yacht? "))
            yacht = Yacht(Engine(engine_type, engine_potency, engine_weight), chasis, model, year, passenger_capacity)
            list_vehicles.append(yacht)
        elif aux == 4:
            motorcycle = Motorcycle(Engine(engine_type, engine_potency, engine_weight), chasis, model, year)
            list_vehicles.append(motorcycle)
        else:
            print("The option is not valid.")
    except ValueError as e:
        print(f"An error occurred")

    print()
    print("Registered vehicles: ")
    for elem in list_vehicles:
      print(elem)
      print()

# Administrator not registered
elif aux1 == 1 and not valid:
    print("Invalid username or password.")

# Add vehicles as external user
elif aux1 == 2 and aux2 == 3:
    print("External users can't add vehicles.")

# Catalog
elif aux2 == 1:
    print("Registered vehicles: ")
    for elem in list_vehicles:
        print(elem)
        print()

# Search Vehicle
elif aux2 == 2:
    print("""Filter:
    1. Type of vehicle.
    2. Chassis.
    3. Model
    4. Year""")
    try:
        aux = int(input("Enter the number of the filter: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()

    if aux == 1:
        print("""What type of vehicle do you want to search?
        1. Car
        2. Truck
        3. Yacht
        4. Motorcycle""")
        try:
            type = int(input("Enter the number of the vehicle type: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            exit()

        if type == 1:
            search(Car)
        elif type == 2:
            search(Truck)
        elif type == 3:
            search(Yacht)
        elif type == 4:
            search(Motorcycle)
        else:
            print("This option is not valid.")
    elif aux == 2:
        print("What type of chassis do you want to search? (A or B)")
        type = input("Enter chassis type: ")
        if type == "A" or type == "B":
            search_chassis(type)
        else:
            print("This option is not valid.")
    elif aux == 3:
        model = input("What model are you looking for? ")
        search_model(model)
    elif aux == 4:
        try:
            year = int(input("What year are you looking for? "))
            search_year(year)
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("This option is not valid.")
else:
    print("This option is not valid.")
