from collections import Counter

from pydantic import BaseModel
from enum import Enum


class Engine(BaseModel):
    stroke: int
    age: int

class Colour(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN =  "green"

class Car(BaseModel):
    model: str
    make: int
    color: Colour
    isSedan: bool = None
    engine: Engine


engine_bmw = Engine(stroke=4, age=10)
BMW = Car(model="x3", make=2007, color=Colour.RED, isSedan=False, engine=engine_bmw)
print(BMW)

print(f"Color of the BMW is {BMW.color.value}")