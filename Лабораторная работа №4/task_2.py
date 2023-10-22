"""
Автор: Рябой Евгений
Дата: 15.10.2023
Дисциплина: F-IT (ЦК-23)
Тема:       Работа с источниками данных
Лабораторная: Конвертер из CSV в JSON формат
Описание:   Вы работаете над программой для обработки данных, и
            вам поставлена задача реализовать конвертер из формата CSV в формат JSON.
            Вам требуется прочитать содержимое CSV файла, распарсить его и преобразовать в структуру данных JSON.

            Ваша задача состоит в том, чтобы написать программу, которая прочитает CSV файл, разберет его на
            отдельные столбцы и создаст для каждой записи словарь в формате JSON, где ключами будут названия столбцов, а
            значениями - соответствующие значения в этой строке.
"""


import csv
# TODO импортировать необходимые молули
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def converter_from_CSV_to_JSON_format() -> None:
    """Функция по конвертации данных из CSV-файла в JSON-файл"""

    with open(INPUT_FILENAME, 'r', encoding="UTF-8") as file_scv:  # TODO считать содержимое csv файла
        data_csv = csv.DictReader(file_scv)

        dict_ = [row for row in data_csv]

        with open(OUTPUT_FILENAME, 'w', encoding="UTF-8") as output_f:
            json.dump(dict_, output_f, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    converter_from_CSV_to_JSON_format()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
