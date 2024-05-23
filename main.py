from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
import src.parser
import src.graph_generator


def search():
    final_label.configure(text="Ваш запрос обрабатывается...", bootstyle="info")
    root.update_idletasks()  # Обновить интерфейс
    query = query_entry.get()
    city = city_entry.get()

    src.parser.count = 0
    src.parser.gradesG = [0, 0, 0, 0]
    src.parser.postsG = [0, 0, 0, 0, 0]

    gradesG, postsG = src.parser.main(query, city)
    final_label.configure(text="Готово!", bootstyle="success")
    src.graph_generator.main(gradesG, postsG)


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

root.mainloop()
