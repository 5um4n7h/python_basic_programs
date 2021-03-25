import math

side1 = int(input("Eneter side 1: "))
side2 = int(input("Eneter side 2: "))
side3 = int(input("Eneter side 3: "))
pm = (side1+side2+side3)/2
area = round(math.sqrt(pm*(pm-side1)*(pm-side2)*(pm-side3)),4)
print("Area of the triangle is",area)

