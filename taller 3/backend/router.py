class Engine(BaseModel):
    type: str
    potency: float
    weight: float

class Vehicle(BaseModel):
    engine: Engine
    chasis: str
    model: str
    year: int
    gas_consumption: float

class Car(Vehicle):
    color: str

class Truck(Vehicle):
    pass

class Yacht(Vehicle):
    passenger_capacity: int

class Motorcycle(Vehicle):
    pass

class LoginRequest(BaseModel):
    username: str
    password: str

class AddVehicleRequest(BaseModel):
    vehicle_type: str
    engine_type: str
    engine_potency: float
    engine_weight: float
    chasis: str
    model: str
    year: int
    color: Optional[str] = None
    passenger_capacity: Optional[int] = None