"""
Модуль для создания графического пользовательского интерфейса (GUI)
для сбора и анализа данных с hh.ru.

Автор:
- Глинник Егор
"""

from tkinter import Tk, LEFT, RIGHT, BOTTOM, CENTER
from ttkbootstrap import Style
from tkinter import ttk
import library.parser
import library.graph_generator
import library.user_graph
import library.text_report_generator
from scripts.config import *


def search():
    """
    Сообщает об обработке запроса, обновляет интерфейс и вызывает
    функцию для сбора данных

    Входные данные:
    -

    Выходные данные:
    -
    
    Автор:
    Глинник Егор
    """    
    final_label.configure(text="Ваш запрос обрабатывается...", bootstyle="info")
    root.update_idletasks()  # обновить интерфейс
    root.after(50, lambda: pars(query_entry.get(), city_entry.get()))


def pars(query, city):
    """
    Обрабатывает запрос пользователя, парсит данные о вакансиях и генерирует графики и текстовые отчеты.

    Входные данные:
    - query: Строка с запросом пользователя.
    - city: Строка с названием города.

    Выходные данные:
    -

    Автор:
    - Глинник Егор
    """
    
    library.parser.count = 0
    library.parser.gradesG = [0, 0, 0, 0]
    library.parser.postsG = [0, 0, 0, 0, 0]
    grades, posts = library.parser.main(query, city)  # парсим
    df = library.graph_generator.main()


    salary_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_salary_vs_vacancies_plot(df)
    )

    experience_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_experience_vs_vacancies_plot(df)
    )

    employment_type_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_employment_type_vs_vacancies_plot(df)
    )

    requirements_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_requirements_vs_vacancies_plot(df, query.lower())
    )

    level_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_level_vs_vacancies_plot(grades)
    )

    specialty_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_specialty_vs_vacancies_plot(posts)
    )


    user_graph_button.configure(
        command=lambda: library.user_graph.main(
            user_col1_combobox.get(), user_col2_combobox.get(), user_type_combobox.get()
        )
    )


    text_report1_button.configure(command=library.text_report_generator.generate_vacancy_reports)

    text_report2_button.configure(command=library.text_report_generator.generate_pivot_table_report)

    text_report3_button.configure(command=library.text_report_generator.generate_statistical_report)

    final_label.configure(text="Готово!", bootstyle="success")


def center_frame_content(frame):
    """
    Центрирует содержимое фрейма.

    Входные данные:
    - frame: Фрейм для центрирования содержимого.

    Выходные данные:
    -
    """
    for widget in frame.winfo_children():
        widget.pack_configure(anchor=CENTER)


config = read_config('scripts/config.ini')

root = Tk()
root.geometry(config.get('Window', 'size'))
style = Style(theme=config.get('Interface', 'theme'))
root.title("Сбор и анализ данных с hh.ru")
font = ("Arial", 14)

head_label = ttk.Label(
    root, text="Сбор и анализ данных с hh.ru", bootstyle="primary", font=("Arial", 30)
)
head_label.pack(pady=30)

# Фрейм для запроса
query_frame = ttk.Frame(root)
query_frame.pack(pady=10, padx=10, fill="x")
query_label = ttk.Label(query_frame, text="Запрос:", bootstyle="primary", font=font)
query_label.pack(side=LEFT, padx=5)
query_entry = ttk.Entry(query_frame, font=font)
query_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

# Фрейм для города
city_frame = ttk.Frame(root)
city_frame.pack(pady=10, padx=10, fill="x")
city_label = ttk.Label(city_frame, text="Город:", bootstyle="primary", font=font)
city_label.pack(side=LEFT, padx=5)
city_entry = ttk.Entry(city_frame, font=font)
city_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

search_button = ttk.Button(root, text="Поиск", command=search, style='primary.TButton')
search_button.pack(pady=20)

final_label = ttk.Label(root, text="", font=font)
final_label.pack(pady=10)

# Создаем виджет Notebook для вкладок
notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, fill="both", expand=True)

# Создаем фрейм для графиков
graphs_frame = ttk.Frame(notebook)
notebook.add(graphs_frame, text="Графики")

# Вставляем надпись "Графики"
graphs_label = ttk.Label(graphs_frame, text="Графики", bootstyle="primary", font=font)
graphs_label.pack(pady=10)

buttons_frame = ttk.Frame(graphs_frame)
buttons_frame.pack(pady=10)

salary_vs_vacancies_button = ttk.Button(buttons_frame, text="Зарплата")
salary_vs_vacancies_button.pack(side=LEFT, padx=5, pady=5)
experience_vs_vacancies_button = ttk.Button(buttons_frame, text="Опыт")
experience_vs_vacancies_button.pack(side=LEFT, padx=5, pady=5)
employment_type_vs_vacancies_button = ttk.Button(buttons_frame, text="Тип занятости")
employment_type_vs_vacancies_button.pack(side=LEFT, padx=5, pady=5)
requirements_vs_vacancies_button = ttk.Button(buttons_frame, text="Требования")
requirements_vs_vacancies_button.pack(side=LEFT, padx=5, pady=5)
level_vs_vacancies_button = ttk.Button(buttons_frame, text="Уровень")
level_vs_vacancies_button.pack(side=LEFT, padx=5, pady=5)
specialty_vs_vacancies_button = ttk.Button(buttons_frame, text="Специальность")
specialty_vs_vacancies_button.pack(side=LEFT, padx=5, pady=5)

# Центрируем содержимое вкладки графиков
center_frame_content(graphs_frame)

# Виджеты для пользовательских графиков
user_graph_frame = ttk.Frame(notebook)
notebook.add(user_graph_frame, text="Пользовательские графики")

user_graph_label = ttk.Label(
    user_graph_frame, text="Пользовательские графики", bootstyle="primary", font=font
)
user_graph_label.pack(pady=5)

user_graph_combobox_frame = ttk.Frame(user_graph_frame)
user_graph_combobox_frame.pack(pady=10)

columns = [
    "Зарплата", "Опыт работы", "Тип занятости",
    "Наличие теста для кандидатов", "График работы"
]
user_col1_combobox = ttk.Combobox(user_graph_combobox_frame, values=columns, font=font)
user_col1_combobox.pack(side=LEFT, padx=5, pady=5)
user_col2_combobox = ttk.Combobox(user_graph_combobox_frame, values=columns, font=font)
user_col2_combobox.pack(side=LEFT, padx=5, pady=5)
user_type_combobox = ttk.Combobox(
    user_graph_combobox_frame, values=[
        "Столбчатая диаграмма", "Категоризированная гистограмма",
        "Диаграмма Бокса-Вискера", "Диаграмма рассеивания"
    ], font=font
)
user_type_combobox.pack(side=LEFT, padx=5, pady=5)
user_graph_button = ttk.Button(user_graph_combobox_frame, text="Построить")
user_graph_button.pack(side=LEFT, padx=5, pady=5)

# Виджеты для текстовых отчётов
text_report_frame = ttk.Frame(notebook)
notebook.add(text_report_frame, text="Текстовые отчёты")

text_report_label = ttk.Label(
    text_report_frame, text="Текстовые отчёты", bootstyle="primary", font=font
)
text_report_label.pack(pady=5)

text_report_buttons_frame = ttk.Frame(text_report_frame)
text_report_buttons_frame.pack(pady=10)

text_report1_button = ttk.Button(text_report_buttons_frame, text="Простой текстовый отчёт")
text_report1_button.pack(side=LEFT, padx=5, pady=5)
text_report2_button = ttk.Button(text_report_buttons_frame, text="Сводная таблица")
text_report2_button.pack(side=LEFT, padx=5, pady=5)
text_report3_button = ttk.Button(text_report_buttons_frame, text="Статистический отчёт")
text_report3_button.pack(side=LEFT, padx=5, pady=5)

# Центрируем содержимое вкладки текстовых отчётов
center_frame_content(text_report_frame)

# Кнопки для изменения стиля интерфейса
theme_buttons_frame = ttk.Frame(root)
theme_buttons_frame.pack(side=BOTTOM, padx=10, pady=10, fill="x")
theme1_button = ttk.Button(
    theme_buttons_frame, text="Darkly",
    command=lambda: change_theme(root, style, 'darkly')
)
theme1_button.pack(side=LEFT, padx=5)
theme2_button = ttk.Button(
    theme_buttons_frame, text="Yeti",
    command=lambda: change_theme(root, style, 'yeti')
)
theme2_button.pack(side=LEFT, padx=5)
theme3_button = ttk.Button(
    theme_buttons_frame, text="Solar",
    command=lambda: change_theme(root, style, 'solar')
)
theme3_button.pack(side=LEFT, padx=5)
theme4_button = ttk.Button(
    theme_buttons_frame, text="Superhero",
    command=lambda: change_theme(root, style, 'superhero')
)
theme4_button.pack(side=LEFT, padx=5)

font1_button = ttk.Button(
    theme_buttons_frame, text="Arial",
    command=lambda: change_font(root, 14, "Arial", head_label, query_label, query_entry, city_label, city_entry,
        final_label, graphs_label, user_graph_label, user_col1_combobox, user_col2_combobox, user_type_combobox,
        text_report_label)
)
font1_button.pack(side=RIGHT, padx=5)
font2_button = ttk.Button(
    theme_buttons_frame, text="Times New Roman",
    command=lambda: change_font(root, 14, "Times New Roman", head_label, query_label, query_entry, city_label, city_entry,
        final_label, graphs_label, user_graph_label, user_col1_combobox, user_col2_combobox, user_type_combobox,
        text_report_label)
)
font2_button.pack(side=RIGHT, padx=5)


root.mainloop()
