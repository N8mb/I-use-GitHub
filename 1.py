import math

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника: {area:.2f}")
else:
    print("Треугольник с такими сторонами не существует.")