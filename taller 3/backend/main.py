from typing import List, Optional
from fastapi import APIRouter, HTTPException
from models import Engine, Vehicle, Car, Truck, Yacht, Motorcycle, LoginRequest, AddVehicleRequest


@router.post("/login")
def login(request: LoginRequest):
    if request.username in admins and admins[request.username] == request.password:
        return {"message": "Login successful", "valid": True}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
@router.get("/vehicles", response_model=List[Vehicle])
def get_vehicles():
    return list_vehicles
