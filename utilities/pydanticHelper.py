from pydantic import BaseModel


class Engine(BaseModel):
    stroke: int
    age: int


class Car(BaseModel):
    model: str
    make: int
    color: str
    isSedan: bool = None
    engine: Engine


engine_bmw = Engine(stroke=4, age=10)
BMW = Car(model="x3", make=2007, color="red", isSedan=False, engine=engine_bmw)
print(BMW)