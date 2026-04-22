def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Конвертер температур")
    try:
        temp = float(input("Введите температуру: "))
        unit = input("Введите единицу измерения (C, F, K): ").strip().upper()

        if unit == 'C':
            c = temp
            f = celsius_to_fahrenheit(c)
            k = celsius_to_kelvin(c)
        elif unit == 'F':
            f = temp
            c = fahrenheit_to_celsius(f)
            k = fahrenheit_to_kelvin(f)
        elif unit == 'K':
            k = temp
            c = kelvin_to_celsius(k)
            f = kelvin_to_fahrenheit(k)
        else:
            print("Некорректная единица измерения. Используйте C, F или K.")
            return

        print(f"\nРезультаты:")
        print(f"Цельсий: {c:.2f} °C")
        print(f"Фаренгейт: {f:.2f} °F")
        print(f"Кельвин: {k:.2f} K")

    except ValueError:
        print("Ошибка: введите числовое значение температуры.")

if __name__ == "__main__":
    main()
