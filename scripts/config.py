import configparser


def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def change_theme(root, style, theme):
    style.theme_use(theme)
    root.update_idletasks()  # обновить интерфейс
    root.update()


def change_font(
        root, size: int, family: str, head_label, query_label, query_entry, city_label, city_entry,
        final_label, user_graph_label, user_col1_combobox, user_col2_combobox, user_type_combobox,
        text_report_label
):
    font = (family, size)
    head_label.configure(font = (family, size + 16))
    query_label.configure(font=font)
    query_entry.configure(font=font)
    city_label.configure(font=font)
    city_entry.configure(font=font)
    final_label.configure(font=font)
    user_graph_label.configure(font=font)
    user_col1_combobox.configure(font=font)
    user_col2_combobox.configure(font=font)
    user_type_combobox.configure(font=font)
    text_report_label.configure(font=font)
    root.update_idletasks()
    root.update()
    root.update_idletasks()
    root.update()