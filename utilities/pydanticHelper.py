from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class Engine(BaseModel):
    stroke: int
    age: int

class Colour(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN =  "green"

class Car(BaseModel):
    model: str = Field(min_length=2)
    make: Optional[int] = Field(gt=2005)
    color: Colour
    isSedan: bool = None
    engine: Engine


engine_bmw = Engine(stroke=4, age=10)
BMW = Car(model="x3", make=2007, color=Colour.RED, isSedan=False, engine=engine_bmw)
print(BMW)

print(f"Color of the BMW is {BMW.color.value}")
print(f"Engine age is {BMW.engine.age}, stroke length is {BMW.engine.stroke}")

ford_obj = Car(model="Ford",color=Colour.GREEN, engine=engine_bmw)
print(ford_obj)