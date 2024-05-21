from tkinter import *
import src.parser
import src.graph_generator


def search():
    final_label.configure(text="Your request is being processed")
    query = query_entry.get()
    city = city_entry.get()
    gradesG, postsG = src.parser.main(query, city)
    final_label.configure(text="Done")
    # src.graph_generator.main(gradesG, postsG)
    print(gradesG)
    print(postsG)


root = Tk()
root.geometry("500x300")

head_label = Label(root, text="Headhunter parsing", font=("Arial", 30))
head_label.pack(pady=20)

query_label = Label(root, text="Query:", font=("Arial", 14))
query_label.pack()
query_entry = Entry(root, justify="center")
query_entry.pack()

city_label = Label(root, text="City:", font=("Arial", 14))
city_label.pack()
city_entry = Entry(root, justify="center")
city_entry.pack()

search_button = Button(root, text="search", command=search)
search_button.pack(pady=10)

final_label = Label(root, text="")
final_label.pack()

root.mainloop()
