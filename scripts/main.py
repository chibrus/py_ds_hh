import configparser
from tkinter import Tk, LEFT, CENTER, BOTTOM, SW
from ttkbootstrap import Style
from tkinter import ttk
import library.parser
import library.graph_generator
import library.user_graph


def search():
    final_label.configure(text="Ваш запрос обрабатывается...", bootstyle="info")
    root.update_idletasks()  # обновить интерфейс
    root.after(50, lambda: pars(query_entry.get(), city_entry.get()))


def pars(query, city):
    library.parser.count = 0
    library.parser.gradesG = [0, 0, 0, 0]
    library.parser.postsG = [0, 0, 0, 0, 0]
    grades, posts = library.parser.main(query, city)  # парсим
    df = library.graph_generator.main()

    salary_vs_vacancies_button.grid(row=0, column=0, padx=5, pady=5)
    salary_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_salary_vs_vacancies_plot(df)
    )
    experience_vs_vacancies_button.grid(row=0, column=1, padx=5, pady=5)
    experience_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_experience_vs_vacancies_plot(df)
    )
    employment_type_vs_vacancies_button.grid(row=0, column=2, padx=5, pady=5)
    employment_type_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_employment_type_vs_vacancies_plot(df)
    )
    requirements_vs_vacancies_button.grid(row=0, column=3, padx=5, pady=5)
    requirements_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_requirements_vs_vacancies_plot(df, query.lower())
    )
    level_vs_vacancies_button.grid(row=0, column=4, padx=5, pady=5)
    level_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_level_vs_vacancies_plot(grades)
    )
    specialty_vs_vacancies_button.grid(row=0, column=5, padx=5, pady=5)
    specialty_vs_vacancies_button.configure(
        command=lambda: library.graph_generator.create_specialty_vs_vacancies_plot(posts)
    )

    user_graph_label.grid(row=0, column=0, columnspan=4, pady=5)
    user_col1_combobox.grid(row=1, column=0, padx=5, pady=5)
    user_col2_combobox.grid(row=1, column=1, padx=5, pady=5)
    user_type_combobox.grid(row=1, column=2, padx=5, pady=5)
    user_graph_button.grid(row=1, column=3, padx=5, pady=5)
    user_graph_button.configure(
        command=lambda: library.user_graph.main(
            user_col1_combobox.get(), user_col2_combobox.get(), user_type_combobox.get()
        )
    )

    final_label.configure(text="Готово!", bootstyle="success")


def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def change_theme(theme):
    style.theme_use(theme)
    root.update_idletasks()  # обновить интерфейс
    root.update()


config = read_config('config.ini')

root = Tk()
root.geometry(config.get('Window', 'size'))
style = Style(theme=config.get('Interface', 'theme'))
root.title("Сбор и анализ данных с hh.ru")

head_label = ttk.Label(
    root, text="Сбор и анализ данных с hh.ru", bootstyle="primary", font=("Arial", 30)
)
head_label.pack(pady=30)

# Фрейм для запроса
query_frame = ttk.Frame(root)
query_frame.pack(pady=10, padx=10, fill="x")
query_label = ttk.Label(query_frame, text="Запрос:", bootstyle="primary", font=("Arial", 14))
query_label.pack(side=LEFT, padx=5)
query_entry = ttk.Entry(query_frame, font=("Arial", 14))
query_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

# Фрейм для города
city_frame = ttk.Frame(root)
city_frame.pack(pady=10, padx=10, fill="x")
city_label = ttk.Label(city_frame, text="Город:", bootstyle="primary", font=("Arial", 14))
city_label.pack(side=LEFT, padx=5)
city_entry = ttk.Entry(city_frame, font=("Arial", 14))
city_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

search_button = ttk.Button(root, text="Поиск", command=search, style='primary.TButton')
search_button.pack(pady=20)

final_label = ttk.Label(root, text="", font=("Arial", 14))
final_label.pack(pady=10)

# Кнопки для отрисовки графиков
buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=10)
salary_vs_vacancies_button = ttk.Button(buttons_frame, text="Зарплата")
experience_vs_vacancies_button = ttk.Button(buttons_frame, text="Опыт")
employment_type_vs_vacancies_button = ttk.Button(buttons_frame, text="Тип занятости")
requirements_vs_vacancies_button = ttk.Button(buttons_frame, text="Требования")
level_vs_vacancies_button = ttk.Button(buttons_frame, text="Уровень")
specialty_vs_vacancies_button = ttk.Button(buttons_frame, text="Специальность")
buttons_frame.place(relx=0.5, rely=0.68, anchor=CENTER)

# Виджеты для пользовательских графиков
user_graph_frame = ttk.Frame(root)
user_graph_frame.pack(pady=10)
user_graph_label = ttk.Label(
    user_graph_frame, text="Пользовательские графики", bootstyle="primary", font=("Arial", 14)
)
columns = [
    "Зарплата", "Опыт работы", "Тип занятости",
    "Наличие теста для кандидатов", "График работы"
]
user_col1_combobox = ttk.Combobox(user_graph_frame, values=columns)
user_col2_combobox = ttk.Combobox(user_graph_frame, values=columns)
user_type_combobox = ttk.Combobox(
    user_graph_frame, values=[
        "clustered_bar", "categorized_histogram",
        "categorized_boxplot", "categorized_scatter"
    ]
)
user_graph_button = ttk.Button(user_graph_frame, text="Построить")
user_graph_frame.place(relx=0.5, rely=0.8, anchor=CENTER)

# Кнопки для изменения стиля интерфейса
theme_buttons_frame = ttk.Frame(root)
theme_buttons_frame.pack(side=BOTTOM, padx=10, pady=10, anchor=SW)
theme1_button = ttk.Button(
    theme_buttons_frame, text="Darkly",
    command=lambda: change_theme('darkly')
)
theme1_button.pack(side=LEFT, padx=5)
theme2_button = ttk.Button(
    theme_buttons_frame, text="Yeti",
    command=lambda: change_theme('yeti')
)
theme2_button.pack(side=LEFT, padx=5)
theme3_button = ttk.Button(
    theme_buttons_frame, text="Solar",
    command=lambda: change_theme('solar')
)
theme3_button.pack(side=LEFT, padx=5)
theme4_button = ttk.Button(
    theme_buttons_frame, text="Superhero",
    command=lambda: change_theme('superhero')
)
theme4_button.pack(side=LEFT, padx=5)

root.mainloop()