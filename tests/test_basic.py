import sys
import os

# Добавляем путь к корню проекта для импорта app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_import_app():
    """Проверяем, что приложение импортируется без ошибок"""
    try:
        from app import app
        assert app is not None
        print("✓ Приложение импортируется корректно")
        return True
    except Exception as e:
        print(f"✗ Ошибка импорта: {e}")
        return False


def test_temperature_conversion_functions():
    """Проверяем функции конвертации температур"""
    from app.converter import (
        celsius_to_fahrenheit,
        celsius_to_kelvin,
        fahrenheit_to_celsius,
        fahrenheit_to_kelvin,
        kelvin_to_celsius,
        kelvin_to_fahrenheit
    )

    # Проверка Цельсий → Фаренгейт
    assert round(celsius_to_fahrenheit(0), 2) == 32.0
    assert round(celsius_to_fahrenheit(100), 2) == 212.0

    # Проверка Цельсий → Кельвин
    assert round(celsius_to_kelvin(0), 2) == 273.15
    assert round(celsius_to_kelvin(-273.15), 2) == 0.0

    # Проверка Фаренгейт → Цельсий
    assert round(fahrenheit_to_celsius(32), 2) == 0.0
    assert round(fahrenheit_to_celsius(212), 2) == 100.0

    # Проверка Кельвин → Цельсий
    assert round(kelvin_to_celsius(273.15), 2) == 0.0
    assert round(kelvin_to_celsius(0), 2) == -273.15

    print("✓ Все функции конвертации работают корректно")
    return True


def test_index_route_get():
    """Проверяем GET-запрос к главной странице"""
    from app import app
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Конвертер температур' in response.data
    print("✓ GET / возвращает 200 и содержит заголовок")
    return True


def test_history_route():
    """Проверяем страницу истории"""
    from app import app
    with app.test_client() as client:
        response = client.get('/history')
        assert response.status_code == 200
        assert b'История конвертаций' in response.data
    print("✓ GET /history возвращает 200")
    return True


def test_post_conversion():
    """Проверяем POST-запрос с конвертацией"""
    from app import app
    with app.test_client() as client:
        response = client.post('/', data={
            'temperature': '100',
            'unit': 'C'
        })
        assert response.status_code == 200
        # Проверяем, что результат отображается
        assert b'212.0' in response.data  # 100°C = 212°F
        assert b'373.15' in response.data  # 100°C = 373.15K
    print("✓ POST / с валидными данными работает")
    return True


def test_post_invalid_input():
    """Проверяем обработку неверного ввода"""
    from app import app
    with app.test_client() as client:
        response = client.post('/', data={
            'temperature': 'abc',
            'unit': 'C'
        })
        assert response.status_code == 200
        assert b'Ошибка' in response.data or b'error' in response.data
    print("✓ POST / с некорректными данными показывает ошибку")
    return True


if __name__ == "__main__":
    print("=" * 50)
    print("Запуск тестов Flask-приложения")
    print("=" * 50)

    tests = [
        test_import_app,
        test_temperature_conversion_functions,
        test_index_route_get,
        test_history_route,
        test_post_conversion,
        test_post_invalid_input,
    ]

    passed = 0
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Тест {test.__name__} упал с ошибкой: {e}")

    print("=" * 50)
    print(f"Результат: {passed}/{len(tests)} тестов пройдено")
    sys.exit(0 if passed == len(tests) else 1)