# A1. Create a base class "polygon" and the derived class "triangle",
# demonstrate inheritance by inheriting find_area() function
# to calculate area of the triangle.

# base class
class Polygon:
    def find_area(self):
        pass   # to be overridden


# derived class
class Triangle(Polygon):

    def __init__(self):
        self.base = float(input("Enter base: "))
        self.height = float(input("Enter height: "))

    def find_area(self):
        return 0.5 * self.base * self.height


# main program
t = Triangle()
print("Area of triangle:", t.find_area())