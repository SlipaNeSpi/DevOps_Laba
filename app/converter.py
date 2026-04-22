from flask import render_template, request
from app import app

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
    return (k - 32) * 5/9

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            temp = float(request.form['temperature'])
            unit = request.form['unit'].upper()
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
                error = "Некорректная единица измерения. Используйте C, F или K."
                return render_template('index.html', error=error)

            result = {
                'c': round(c, 2),
                'f': round(f, 2),
                'k': round(k, 2)
            }
        except ValueError:
            error = "Ошибка: введите числовое значение температуры."

    return render_template('index.html', result=result, error=error)