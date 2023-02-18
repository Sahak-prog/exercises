import math

a = int(input("enter A value:"))
for i in range(100):
    if a == 0:
        a = int(input("enter A value:"))
        pass
    else:
        b = int(input("Enter B value:"))
        c = int(input("Enter C value:"))
        d = (b ** 2) - (4 * a * c)
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print('Answers {0} and {1}'.format(x1, x2))
        break
