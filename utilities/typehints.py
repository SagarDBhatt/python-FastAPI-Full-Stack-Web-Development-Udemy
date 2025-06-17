class Typehint:
    def __init__(self, value1: float, value2: float):
        self.value1 = value1
        self.value2 = value2

    def get_sum(self) -> float:
        return float(self.value1 + self.value2)


obj = Typehint("adv", 4.3)
print(obj.get_sum())