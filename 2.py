def to_meters(value, unit):
    conversions = {
        'км': 1000,
        'м': 1,
        'см': 0.01,
        'мм': 0.001,
        'mi': 1609.344,
        'yd': 0.9144
    }
    return value * conversions[unit]

def from_meters(value, unit):
    conversions = {
        'км': 1/1000,
        'м': 1,
        'см': 100,
        'мм': 1000,
        'mi': 1/1609.344,
        'yd': 1/0.9144
    }
    return value * conversions[unit]

def main():
    units = ['км', 'м', 'см', 'мм', 'mi', 'yd']

    print("Доступные единицы измерения:")
    print(", ".join(units))

    from_unit = input("Введите исходную единицу измерения: ").strip()
    if from_unit not in units:
        print("Ошибка: неизвестная единица измерения.")
        return

    to_unit = input("Введите целевую единицу измерения: ").strip()
    if to_unit not in units:
        print("Ошибка: неизвестная единица измерения.")
        return

    try:
        value = float(input("Введите значение для конвертации: "))
    except ValueError:
        print("Ошибка: введите числовое значение.")
        return

    meters = to_meters(value, from_unit)
    result = from_meters(meters, to_unit)

    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()