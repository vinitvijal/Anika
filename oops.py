class anika:

    def __init__(self, num: int) -> None:
        self.num = num

    def sqrt(self):
        return (self.num)**0.5
    
    def square(self):
        return (self.num)**2
    
    def cube(self):
        return (self.num)**3
    

v = anika('25')
y = anika(45)

print(v.cube())
print(y.square())
print(v.sqrt())
