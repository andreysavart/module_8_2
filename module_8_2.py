def personal_sum(numbers):

    result = 0  # Инициализация суммы

    incorrect_data = 0  # Счётчик некорректных данных

    for number in numbers:

        try:

            result += number  # Попытка сложить значение

        except TypeError:

            print(f'Некорректный тип данных для подсчёта суммы - {number}')

            incorrect_data += 1  # Увеличиваем счётчик некорректных данных

    return result, incorrect_data  # Возвращаем сумму и количество ошибок

def calculate_average(numbers):

    try:

        total_sum, incorrect_data = personal_sum(numbers)  # Используем personal_sum для вычисления суммы

        average = total_sum / (len(numbers) - incorrect_data)  # Рассчитываем среднее

    except ZeroDivisionError:

        return 0  # Если делим на 0, возвращаем 0

    except TypeError:

        print('В numbers записан некорректный тип данных')

        return None  # Если некорректный тип, возвращаем None

    return average  # Возвращаем среднее арифметическое

# Примеры вызова

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Некорректный тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанный тип

print(f'Результат 3: {calculate_average(567)}')  # Не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректный ввод

