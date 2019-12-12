class Rectangle():
    def __init__(self, length, width):

        if length < 0 or width < 0:
            print("No negative values")
            return
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*self.length+2*self.width

    def area(self):
        return self.length*self.width


r1 = Rectangle(7,3)
print(r1.perimeter())
print(r1.area())
