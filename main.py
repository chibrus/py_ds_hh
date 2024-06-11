from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
import library.parser
import library.graph_generator


def search():
    final_label.configure(text="Ваш запрос обрабатывается...", bootstyle="info")
    root.update_idletasks()  # обновить интерфейс
    query = query_entry.get()
    city = city_entry.get()

    library.parser.count = 0
    library.parser.gradesG = [0, 0, 0, 0]
    library.parser.postsG = [0, 0, 0, 0, 0]
    gradesG, postsG = library.parser.main(query, city)  # парсим
    df = library.graph_generator.main()
    
    salary_vs_vacancies_button.grid(row=0, column=0, padx=5, pady=5)
    salary_vs_vacancies_button.configure(command=lambda: library.graph_generator.create_salary_vs_vacancies_plot(df))
    experience_vs_vacancies_button.grid(row=0, column=1, padx=5, pady=5)
    experience_vs_vacancies_button.configure(command=lambda: library.graph_generator.create_experience_vs_vacancies_plot(df))
    employment_type_vs_vacancies_button.grid(row=0, column=2, padx=5, pady=5)
    employment_type_vs_vacancies_button.configure(command=lambda: library.graph_generator.create_employment_type_vs_vacancies_plot(df))
    requirements_vs_vacancies_button.grid(row=0, column=3, padx=5, pady=5)
    requirements_vs_vacancies_button.configure(command=lambda: library.graph_generator.create_requirements_vs_vacancies_plot(df, query.lower()))
    level_vs_vacancies_button.grid(row=0, column=4, padx=5, pady=5)
    level_vs_vacancies_button.configure(command=lambda: library.graph_generator.create_level_vs_vacancies_plot(gradesG))
    specialty_vs_vacancies_button.grid(row=0, column=5, padx=5, pady=5)
    specialty_vs_vacancies_button.configure(command=lambda: library.graph_generator.create_specialty_vs_vacancies_plot(postsG))

    final_label.configure(text="Готово!", bootstyle="success")


root = Tk()
root.geometry("800x500")
root.title("Сбор и анализ данных с hh.ru")

style = Style(theme='solar')

head_label = ttk.Label(root, text="Сбор и анализ данных с hh.ru", font=("Arial", 30))
head_label.pack(pady=30)

query_frame = ttk.Frame(root)
query_frame.pack(pady=10, padx=10, fill="x")
query_label = ttk.Label(query_frame, text="Запрос:", font=("Arial", 14))
query_label.pack(side=LEFT, padx=5)
query_entry = ttk.Entry(query_frame, font=("Arial", 14))
query_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

city_frame = ttk.Frame(root)
city_frame.pack(pady=10, padx=10, fill="x")
city_label = ttk.Label(city_frame, text="Город:", font=("Arial", 14))
city_label.pack(side=LEFT, padx=5)
city_entry = ttk.Entry(city_frame, font=("Arial", 14))
city_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

search_button = ttk.Button(root, text="Поиск", command=search, style='primary.TButton')
search_button.pack(pady=20)

final_label = ttk.Label(root, text="", font=("Arial", 14))
final_label.pack(pady=20)

# Фрейм для размещения кнопок
buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=20)

salary_vs_vacancies_button = ttk.Button(buttons_frame, text="Зарплата")
experience_vs_vacancies_button = ttk.Button(buttons_frame, text="Опыт")
employment_type_vs_vacancies_button = ttk.Button(buttons_frame, text="Тип занятости")
requirements_vs_vacancies_button = ttk.Button(buttons_frame, text="Требования")
level_vs_vacancies_button = ttk.Button(buttons_frame, text="Уровень")
specialty_vs_vacancies_button = ttk.Button(buttons_frame, text="Специальность")

# Центрирование фрейма с кнопками
buttons_frame.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
