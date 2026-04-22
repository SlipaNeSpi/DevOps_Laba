from flask import render_template, request
from app import app
import csv
import os
from datetime import datetime

# ---------- Функции конвертации ----------
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

# ---------- Главная страница ----------
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

            # --- Сохранение в историю (CSV) ---
            history_file = os.path.join(os.path.dirname(__file__), 'history.csv')
            file_exists = os.path.isfile(history_file)

            with open(history_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(['timestamp', 'input_temp', 'input_unit', 'c', 'f', 'k'])
                writer.writerow([
                    datetime.now().isoformat(),
                    temp,
                    unit,
                    result['c'],
                    result['f'],
                    result['k']
                ])

        except ValueError:
            error = "Ошибка: введите числовое значение температуры."

    return render_template('index.html', result=result, error=error)


# ---------- Страница истории ----------
@app.route('/history')
def history():
    history_file = os.path.join(os.path.dirname(__file__), 'history.csv')
    records = []
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            records = list(reader)
    return render_template('history.html', records=records)