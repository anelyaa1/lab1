from math import tan,pi

length  = int(input())
number  = int(input())

area = (number * length ** 2)/(4 * tan(pi/number))
 
#Display the result
print("The area of Polygon is %.2f " % area)