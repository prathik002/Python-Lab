square_area = lambda a: a**2
rectangle_area = lambda l,b : l*b
triangle_area = lambda ba,h : 0.5*ba*h

a = int(input("Enter length:"))
print("Area of the square:", square_area(a))

l = int(input("Enter length:"))
b = int(input("Enter breadth:"))
print("Area of the rectangle:",rectangle_area(l,b))

ba = int(input("Enter length of base:"))
h = int(input("Enter height:"))
print("Area of triangle:",triangle_area(ba,h))
