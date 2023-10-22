"""
Автор: Рябой Евгений
Дата: 13.10.2023
Дисциплина: F-IT (ЦК-23)
Тема:       Функции и методы
Лабораторная:   Частотный анализ букв в тексте
Описание:   Вы работаете над проектом по анализу текстов, и вам нужно
            провести частотный анализ букв в заданном тексте.
            Частотный анализ поможет вам определить, какие буквы встречаются чаще всего, и
            построить статистику их использования.

            Задачу следует разбить на два этапа:
            1) подсчет количества каждой буквы,
            2) вычисление частоты каждой буквы. За каждый этап отвечает одна функция.
"""


def count_letters(text: str) -> dict[str, int]:
    """Функция принимает исходный текст и далее подсчитывает количество повторений каждой буквы в исходном тексте.

    *Регистр не учитывается.

    :param text: исходный текст
    :return: словарь слоедующей структуры:
            {
                key: буква,
                value: количество повторений
            }

    """
    letter_counts_dictionary = {}

    # Преобразуем все буквы в исходном тексте к нижнему регистру
    lower_case_text = text.lower()

    for char in lower_case_text:
        if char.isalpha():
            # Если символ уже есть в словаре, увеличиваем его счетчик на 1
            if char in letter_counts_dictionary:
                letter_counts_dictionary[char] += 1
            else:
                # Если символа нет в словаре, добавляем его с начальным счетчиком 1
                letter_counts_dictionary[char] = 1

            #letter_counts_dictionary[char] = letter_counts_dictionary.get(char, 0) + 1

    return letter_counts_dictionary


def calculate_frequency(letter_counts_dictionary: dict[str, int]) -> dict[str, float]:
    """Функция принимает исходный словарь и заменяет значение по каждому ключу с количества на частоту вхождения

    :param letter_counts_dictionary: исходный словарь следующей структуры:
            {
                key: буква,
                value: количество повторений
            }
    :return: словарь слоедующей структуры:
            {
                key: буква,
                value: частота буквы относительно всех буквы
            }

    """
    dictionary_size = sum(letter_counts_dictionary.values())

    letter_frequency_dictionary = {}

    for key, value in letter_counts_dictionary.items():
        letter_frequency_dictionary[key] = value / dictionary_size

    return letter_frequency_dictionary


def dictionary_output_with_two_digit(letter_counts_dictionary: dict[str, float]) -> None:
    """Функция выводит на экран исходный словарь по следующей структуре:
        ключ: значение_с_двумя_знаками_после_запятой

    :param letter_counts_dictionary: исходнрый словарь слоедующей структуры:
            {
                key: буква,
                value: частота буквы относительно всех буквы
            }
    :return:

    """
    for key, value in letter_counts_dictionary.items():
        print(f"{key}: {value:.2f}")


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


dictionary_output_with_two_digit(calculate_frequency(count_letters(main_str)))
