"""
Модуль для работы с конфигурационным файлом и изменения интерфейса программы.

Автор:
- Глинник Егор

Функции:
- read_config(filename): Считывает конфигурационный файл и возвращает объект ConfigParser.
- change_theme(root, style, theme): Изменяет тему интерфейса программы.
- change_font(root, size, family, head_label, query_label, query_entry, city_label, city_entry,
        final_label, user_graph_label, user_col1_combobox, user_col2_combobox, user_type_combobox,
        text_report_label): Изменяет шрифт для различных элементов интерфейса.
- center_frame_content(frame): Центрирует содержимое фрейма.
"""

import configparser


def read_config(filename: str):
    """
    Считывает конфигурационный файл и возвращает объект ConfigParser.

    Входные данные:
    - filename: Строка с именем конфигурационного файла.

    Выходные данные:
    - config: Объект ConfigParser.

    Автор:
    - Глинник Егор
    """
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def change_theme(root, style, theme: str):
    """
    Изменяет тему интерфейса программы.

    Входные данные:
    - root: Объект корневого окна Tkinter.
    - style: Объект стиля ttkbootstrap.Style.
    - theme: Строка с названием темы.

    Выходные данные:
    -

    Автор:
    - Глинник Егор
    """
    style.theme_use(theme)
    root.update_idletasks()  # обновить интерфейс
    root.update()


def change_font(
    root, size: int, family: str, head_label, query_label, query_entry, city_label,
    city_entry, final_label, graphs_label, user_graph_label, user_col1_combobox,
    user_col2_combobox, user_type_combobox, text_report_label
):
    """
    Изменяет шрифт для различных элементов интерфейса.

    Входные данные:
    - root: Объект корневого окна Tkinter.
    - size: Целое число, размер шрифта.
    - family: Строка, название шрифта.
    - head_label: Объект метки заголовка.
    - query_label: Объект метки для запроса.
    - query_entry: Объект поля ввода для запроса.
    - city_label: Объект метки для города.
    - city_entry: Объект поля ввода для города.
    - final_label: Объект метки для отображения завершения операции.
    - user_graph_label: Объект метки для пользовательского графика.
    - user_col1_combobox: Объект выпадающего списка для выбора колонки 1.
    - user_col2_combobox: Объект выпадающего списка для выбора колонки 2.
    - user_type_combobox: Объект выпадающего списка для выбора типа графика.
    - text_report_label: Объект метки для текстовых отчетов.

    Выходные данные:
    -

    Автор:
    - Глинник Егор

    Примечание:
    Данная функция изменяет шрифт для указанных элементов и обновляет интерфейс.
    """
    font = (family, size)
    head_label.configure(font=(family, size + 16))
    query_label.configure(font=font)
    query_entry.configure(font=font)
    city_label.configure(font=font)
    city_entry.configure(font=font)
    final_label.configure(font=font)
    graphs_label.configure(font=font)
    user_graph_label.configure(font=font)
    user_col1_combobox.configure(font=font)
    user_col2_combobox.configure(font=font)
    user_type_combobox.configure(font=font)
    text_report_label.configure(font=font)
    root.update_idletasks()
    root.update()
    root.update_idletasks()
    root.update()
