class Facade:
    pass 

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

class Circle:
    pi = 3.14
    #def area(self, radius):
        #return Circle.pi*radius**2
    def __init__(self, diameter):

        print('new circle diameter: {d}'.format(d=diameter))
        self.radius = diameter/2
    def circumference(self):
        return 2*self.pi*self.radius


teaching_table = Circle(36)
print(teaching_table.circumference())
        
"""
circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)
"""
