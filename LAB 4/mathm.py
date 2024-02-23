import math

#Write a Python program to convert degree to radian.
rad = int(input())
print(math.radians(rad))


#Write a Python program to calculate the area of a trapezoid.
a, b, h = list(map(int, input().split()))

print((a + b) * h * 0.5)


#Write a Python program to calculate the area of regular polygon.

side, length = list(map(int, input().split()))

print(0.25 * side * (length ** 2) * math.tan(math.pi / side))


#Write a Python program to calculate the area of a parallelogram.

x, y = list(map(int, input().split()))

print(x * y)