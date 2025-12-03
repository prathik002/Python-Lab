from Graphics.RectFunctions import*
from Graphics.CircFunctions import*
from Graphics.DGraphics.SphereFunctions import*
from Graphics.DGraphics.CuboidFunctions import*


#Rectangle
l = int(input("Enter Length: "))
b = int(input("Enter Breadth: "))
print("Rectangle Area = ",RectArea(l,b))
print("Rectangle Perimeter = ",RectPerimeter(l,b))


#circle
r=int(input("enter radius of circle:"))
print("Circle Area=",CircArea(r))
print("Circle Perimeter=",CircPerimeter(r))

#sphere
r=int(input("enter radius of Sphere:"))
print("Sphere Area=",SpArea(r))
print("Sphere Volume=",SpPerimeter(r))

#cuboid
l=int(input("enter cuboid length:"))
b=int(input("enter cuboid breadth:"))
h=int(input("enter cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid Perimeter=",CubPerimeter(l,b,h))
