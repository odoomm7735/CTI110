# Michael Odoom
# June 25, 2024
# P2Lab1

"""Assignment tets student's knowledge of how to write code that performs
mathematical calculations and displays informamtion to users."""

#Import maths module to use the constant, math.pi
import math

#get the radius from user
radius = float(input("what is the radius of the circle? "))
print()

#calculate the diameter
diameter=2 * radius
circumference=2 * radius * math.pi
area = math.pi * radius**2

#Display the output
print(f'The diameter of the circle is {diameter:.1f}\n')

print(f'The circumference of the circle is {circumference:.2f}\n')

print(f'The area of the circle is {area:.3f}')

input("press enter to exit")