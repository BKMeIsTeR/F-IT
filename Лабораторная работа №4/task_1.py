"""
Автор: Рябой Евгений
Дата: 15.10.2023
Дисциплина: F-IT (ЦК-23)
Тема:       Работа с источниками данных
Лабораторная: Найти сумму произведений из списка словарей
Описание:   Вы работаете над аналитической программой, которая обрабатывает данные в формате JSON.
            [
                ...,
                {
                    "score": 0.0009456152645028281,
                    "weight": 1
                },
                ...
            ]
            Вам поставлена задача реализовать функцию, которая прочитает JSON файл и
            найдет сумму произведений двух значений в каждом словаре.
            Значения для умножения находятся по ключам "score" и "weight".
            Вам нужно вычислить произведение "score" * "weight" в каждом словаре и
            найти сумму этих произведений.

            Функция должна вернуть значение с плавающей запятой, округленное до 3 знаков после запятой.
            В ответе распечатайте полученную сумму.
"""


import json


# TODO решите задачу
def task(json_file: str, ndigits = 3) -> float:
    """Сумма произведений значений словарей из JSON-Файла"""

    with open(json_file, 'r', encoding="UTF-8") as file_input:
        data_json = json.load(file_input)

    if not data_json:
        raise ValueError("В файле нет сериализованных данных")

    dictionary_value_product = [item["score"] * item["weight"] for item in data_json]
    sum_dictionary_value_product = round(sum(dictionary_value_product), ndigits)

    return sum_dictionary_value_product


if __name__ == "__main__":
    JSON_INPUT = "input.json"
    print(task(JSON_INPUT))
