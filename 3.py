year = int(input("Введите год: "))

if (year % 400 == 0):
    print(f"{year} — високосный год.")
elif (year % 100 == 0):
    print(f"{year} — не является високосным годом.")
elif (year % 4 == 0):
    print(f"{year} — високосный год.")
else:
    print(f"{year} — не является високосным годом.")