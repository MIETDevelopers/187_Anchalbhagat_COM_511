class Cylinder:
# class attribute
    pi = 3.14
    def __init__(self, radius, height):
# instance variables
        self.radius = radius
        self.height = height
if __name__ == '__main__':
    c1 = Cylinder(4,20)
    c2 = Cylinder(10, 50)
print(f'Pi for c1:{c1.pi} and c2:{c2.pi}')
print(f'Radius for c1:{c1.radius} and c2:{c2.radius}')
print(f'Height for c1:{c1.height} and c2:{c2.height}')
print(f'Pi for both c1 and c2 is: {Cylinder.pi}')