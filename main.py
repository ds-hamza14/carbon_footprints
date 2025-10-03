from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (safe for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FootprintInput(BaseModel):
    car_km: float
    bus_km: float
    meals_meat: int
    meals_veg: int
    bottles: int

factors = {
    "car_km": 0.2,
    "bus_km": 0.08,
    "meat_meal": 5.0,
    "veg_meal": 2.0,
    "plastic_bottle": 0.1
}

@app.get("/")
def home():
    return {"message": "Carbon Footprint API running!"}

@app.post("/calculate")
def calculate(data: FootprintInput):
    footprint = (
        data.car_km * factors["car_km"] +
        data.bus_km * factors["bus_km"] +
        data.meals_meat * factors["meat_meal"] +
        data.meals_veg * factors["veg_meal"] +
        data.bottles * factors["plastic_bottle"]
    )
    return {"carbon_footprint_kg": round(footprint, 2)}
