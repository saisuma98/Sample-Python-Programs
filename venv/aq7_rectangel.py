
class RECTANGE:

    width = 0
    height = 0
    corner_x = 0
    corner_y = 0

    def __init__(self, width=0, height=0, corner_x=0, corner_y=0):
        self.width = width
        self.height = height
        self.corner_x = corner_x
        self.corner_y = corner_y

    def center(self):
        center_x = (self.width - self.corner_x) / 2
        center_y = (self.height - self.corner_y) / 2
        return center_x,center_y

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*self.width + 2*self.height


rectangle = RECTANGE(100, 200, 10, 20)

print("Center of rectangle = ", rectangle.center())
print("Area of rectangle = ", rectangle.area())
print("Perimeter of rectangle = ", rectangle.perimeter())

