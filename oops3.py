class anika:
    def __init__(self, base, pow) -> None:
        self.base = base
        self.pow = pow

    def power(self):
        return self.base**self.pow
    

print(anika.power(5,3))