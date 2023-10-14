"""
Автор: Рябой Евгений
Дата: 08.10.2023

Дисциплина: F-IT (ЦК-23)
Тема:       Базовые типы языка Python и работа с ним
Лабораторная:   Разделение игроков на две команды
Описание:   У вас имеется информационный объем дискеты,
            равный 1,44 Мб, а также параметры книги, такие как количество страниц,
            число строк на странице и количество символов в строке.
            Ваша задача — рассчитать, сколько одинаковых книг можно поместить на
            дискету, и вывести результат на экран.
"""

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_list_payers = len(list_players)
half_count_of_list_payers = int(count_of_list_payers / 2)

team_players_first  = list_players[:half_count_of_list_payers]
team_players_second = list_players[half_count_of_list_payers:]

print(team_players_first)
print(team_players_second)