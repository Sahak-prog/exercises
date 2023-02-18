import math
a = int(input("Enter a value for the circumference of the circle: "))
for i in range(100):
    if a == 0:
        a = int(input("enter a true value: "))
        pass
    else:
        area_of_circle = (float(math.pi)) * (a ** 2)
        print("So your circumference of the circle is: {0}".format(area_of_circle))
        break