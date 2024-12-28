import json


def load_json(file_path):
    """Загрузка данных из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def fill_values(tests, values_dict):
    """Заполнение поля value в тестах на основании значений."""
    for test in tests:
        test_id = test.get("id")

        # Заполняем значение для текущего теста, если оно есть
        if test_id in values_dict:
            test["value"] = values_dict[test_id]

        # Если есть вложенные значения, обрабатываем их рекурсивно
        if "values" in test:
            fill_values(test["values"], values_dict)


def main(tests_file, values_file, report_file):
    try:
        # Загружаем данные
        tests_data = load_json(tests_file)
        values_data = load_json(values_file)

        # Создаем словарь значений для быстрого доступа
        values_dict = {item['id']: item['value'] for item in values_data.get("values", [])}

        # Заполняем значения в тестах
        if "tests" in tests_data:
            fill_values(tests_data["tests"], values_dict)

        # Сохраняем заполненные тесты в report.json
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(tests_data, f, ensure_ascii=False, indent=4)

        print(f"Файл '{report_file}' успешно создан.")

    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e}")
    except json.JSONDecodeError:
        print("Ошибка: не удалось декодировать JSON.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Замените 'tests.json' и 'values.json' на ваши файлы
if __name__ == "__main__":
    main('tests.json', 'values.json', 'report.json')
