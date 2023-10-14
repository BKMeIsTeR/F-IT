"""
Автор: Рябой Евгений
Дата: 08.10.2023

Дисциплина: F-IT (ЦК-23)
Тема:       Базовые типы языка Python и работа с ним
Лабораторная:   Расчет количества книг на дискете
Описание:   У вас имеется информационный объем дискеты,
            равный 1,44 Мб, а также параметры книги, такие как количество страниц,
            число строк на странице и количество символов в строке.
            Ваша задача — рассчитать, сколько одинаковых книг можно поместить на
            дискету, и вывести результат на экран.
Исходные данные:    Информационный объем дискеты равен 1,44 Мб.
                    Количество страниц в книге - 100.
                    Число строк на странице - 50.
                    Количество символов в строке - 25.
                    Для хранения кода одного символа нужно 4 байта.
"""

# TODO Найдите количество книг, которое можно разместить на дискете
KILO = 1024

information_capacity_of_the_floppy_disc_MBytes = 1.44
number_of_pages_in_the_book = 100
number_of_lines_per_page = 50
number_of_characters_in_a_string = 25
character_capacity = 4

information_capacity_of_the_floppy_disc_Bytes = information_capacity_of_the_floppy_disc_MBytes \
                                                * KILO \
                                                * KILO

byte_in_the_book = number_of_pages_in_the_book * \
                   number_of_lines_per_page * \
                   number_of_characters_in_a_string * \
                   character_capacity

count_of_books = int(information_capacity_of_the_floppy_disc_Bytes // byte_in_the_book)

print("Количество книг, помещающихся на дискету:", count_of_books)
