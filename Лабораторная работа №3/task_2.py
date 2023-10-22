"""
Автор: Рябой Евгений
Дата: 13.10.2023
Дисциплина: F-IT (ЦК-23)
Тема:       Функции и методы
Лабораторная:   Поиск общих участников
Описание:   Вы организуете встречу для двух групп участников, и вам
            необходимо определить, кто является общими участниками для обеих групп.
            Для этого вам нужно написать функцию, которая будет принимать две строки с
            фамилиями участников, перечисленными без пробелов через разделитель.
            Чаще всего в качестве разделителя используется запятая.
Исходные данные:
            participants_first_group  = "Иванов|Петров|Сидоров"
            participants_second_group = "Петров|Сидоров|Смирнов"
"""


def find_common_participants(first_entrants: str, second_entrants: str, separator=',') -> list[str]:
    """Поиск общих фамилий

    Функция вовзращает отсортированный список с общими фамилиями из двух групп участников

    :param first_entrants: строка с фамилиями первой группы
    :param second_entrants: строка с фамилиями второй группы
    :param separator: разделитель в исходных строках с фамилиями групп между фамилиями.
                      По умолчанию: запятая ','
    :return: отсортированный список с общими фамилиями

    """
    list_first_entrants = first_entrants.split(separator)
    list_second_entrants = second_entrants.split(separator)

    # Преобразуем первую группу участников во множетсво, чтобы применить меторд intersection
    set_list_first_entrants = set(list_first_entrants)

    list_common_entrants = list(set_list_first_entrants.intersection(list_second_entrants))
    list_common_entrants.sort()

    return list_common_entrants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result1 = find_common_participants(participants_first_group, participants_second_group, '|')

print(result1)
