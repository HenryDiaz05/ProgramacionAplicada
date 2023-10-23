class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print('new circle diameter: {d}'.format(d=diameter))
        self.radius = diameter/2
    def circumference(self):
        return 2*self.pi*self.radius
    def area(self):
        return self.pi*self.radius**2

class Rectangle:
    def __init__(self, base, height):
        print('the base is: {b}, the height is: {h}'.format(b=base,h=height))
        self.base = base
        self.height = height
    def perimeter(self):
        return 2*self.base+2*self.height
    def area(self):
        return  self.base*self.height

class TriangleRectangle:
    def __init__(self, base, height):
        print('the base is: {b}, the height is: {h}'.format(b=base,h=height))
        self.base = base
        self.height = height
        self.hypotenuse = (base**2 + height**2)**0.5
    def perimeter(self):
        return self.base+self.height+self.hypotenuse 
    def area(self):
        return  (self.base*self.height)/2

teaching_table = Circle(36)
print(teaching_table.circumference())
print(teaching_table.area())

board = Rectangle(5,15)
print(board.perimeter())
print(board.area())

rule = TriangleRectangle(30,10)
print(rule.perimeter())
print(rule.area())