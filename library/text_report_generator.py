"""
Модуль для генерации текстовых отчетов о вакансиях на основе данных из файла Excel.

Этот модуль включает функции для:
- Генерации текстовых отчетов о вакансиях по различным параметрам.
- Создания и сохранения сводных таблиц по данным о вакансиях.
- Создания статистического отчета по данным о вакансиях.
- Открытия сгенерированных отчетов в текстовом редакторе операционной системы.

Функции:
- generate_vacancy_reports(): Генерирует текстовые отчеты о вакансиях на основе данных из файла.
- generate_pivot_table_report(): Генерирует сводную таблицу на основе данных из файла.
- generate_statistical_report(): Генерирует статистический отчет на основе данных из файла.
- open_file(output_file: str): Открывает указанный файл в текстовом редакторе операционной системы.

Автор:
- Чибиров Руслан
"""
import os
import sys
import subprocess
import pandas as pd
from tabulate import tabulate


def generate_vacancy_reports():
    """
    Генерирует текстовые отчеты о вакансиях на основе данных из файла Excel.

    Входные данные:
    -

    Выходные данные:
    -

    Автор:
    - Чибиров Руслан
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.xlsx')
    df = pd.read_excel(file_path)
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'output'), exist_ok=True)
    output_file = os.path.join(os.path.dirname(__file__), '..', 'output', 'vacancies_report.txt')
    reports = []

    # Отчет по зарплате и работодателям
    salary_employer_columns = ['Название вакансии', 'Зарплата', 'Название работодателя']
    salary_employer_headers = ['Название вакансии', 'Зарплата', 'Название работодателя']
    salary_employer_report = tabulate(
        df[salary_employer_columns],
        headers=salary_employer_headers,
        tablefmt="pretty"
    )
    reports.append("Отчет по зарплате и работодателям\n" + salary_employer_report)

    # Отчет по опыту работы и типу занятости
    experience_employment_columns = ['Название вакансии', 'Опыт работы', 'Тип занятости']
    experience_employment_headers = ['Название вакансии', 'Опыт работы', 'Тип занятости']
    experience_employment_report = tabulate(
        df[experience_employment_columns],
        headers=experience_employment_headers,
        tablefmt="pretty"
    )
    reports.append("Отчет по опыту работы и типу занятости\n" + experience_employment_report)

    # Отчет по наличию теста и графику работы
    test_schedule_columns = ['Название вакансии', 'Наличие теста для кандидатов', 'График работы']
    test_schedule_headers = ['Название вакансии', 'Наличие теста для кандидатов', 'График работы']
    test_schedule_report = tabulate(
        df[test_schedule_columns],
        headers=test_schedule_headers,
        tablefmt="pretty"
    )
    reports.append("Отчет по наличию теста и графику работы\n" + test_schedule_report)

    # Объединение всех отчетов в один файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(reports))
    open_file(output_file)


def generate_pivot_table_report():
    """
    Генерирует отчет в формате сводной таблицы на основе данных из файла Excel.
    Читает данные из файла Excel, создает сводную таблицу и сохраняет её в текстовый файл.

    Входные данные: 
    -

    Выходные данные:
    -

    Автор:
    - Чибиров Руслан
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.xlsx')
    df = pd.read_excel(file_path)
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'output'), exist_ok=True)
    output_file = os.path.join(os.path.dirname(__file__), '..', 'output', 'pivot_table_report.txt')
    agg_func = 'size'
    attributes = [
    ('Название работодателя', 'Тип занятости'),
    ('График работы', 'Опыт работы'),
    ('Название вакансии', 'График работы')
    ]
    report_lines = []

    for row_attr, col_attr in attributes:
        pivot_table = pd.pivot_table(df, index=row_attr, columns=col_attr,
                                     aggfunc=agg_func, fill_value=0)
        pivot_table = pivot_table.reset_index()

        report_lines.append(f"Сводная таблица для '{row_attr}' и '{col_attr}':\n")
        report_lines.append(tabulate(pivot_table, headers='keys', tablefmt="pretty"))
        report_lines.append("\n")

    # Сохранение отчета в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))
    open_file(output_file)


def generate_statistical_report():
    """
    Генерирует статистический отчет на основе данных из файла Excel.
    Читает данные из файла Excel, вычисляет статистику и сохраняет её в текстовый файл.

    Входные данные:
    -

    Выходные данные:
    -

    Автор:
    - Чибиров Руслан
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.xlsx')
    df = pd.read_excel(file_path)
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'output'), exist_ok=True)
    output_file = os.path.join(os.path.dirname(__file__), '..', 'output', 'statistical_report.txt')
    columns = ['Зарплата', 'Опыт работы', 'Тип занятости',
               'Наличие теста для кандидатов', 'График работы']
    report_lines = []

    # Для количественных переменных
    quantitative_columns = df[columns].select_dtypes(include=['number']).columns.tolist()
    if quantitative_columns:
        report_lines.append("Статистики для количественных переменных:\n")
        stats = df[quantitative_columns].describe().T
        stats['variance'] = df[quantitative_columns].var()
        stats = stats[['min', 'max', 'mean', 'std', 'variance']]
        report_lines.append(
            tabulate(stats, headers=['Переменная', 'Мин', 'Макс', 'Среднее',
                                    'Ст. отклонение', 'Дисперсия'], tablefmt="pretty"))
        report_lines.append("\n")

    # Для качественных переменных
    qualitative_columns = df[columns].select_dtypes(exclude=['number']).columns.tolist()
    if qualitative_columns:
        report_lines.append("Таблица частот для качественных переменных:\n")
        for column in qualitative_columns:
            report_lines.append(f"Переменная: {column}\n")
            freq_table = df[column].value_counts().reset_index()
            freq_table.columns = [column, 'Частота']
            freq_table['Процент'] = (freq_table['Частота'] / freq_table['Частота'].sum()) * 100
            freq_table['Процент'] = freq_table['Процент'].apply(lambda x: f"{x:.2f}%")
            report_lines.append(tabulate(freq_table, headers=[column, 'Частота', 'Процент'],
                                        tablefmt="pretty"))
            report_lines.append("\n")

    # Сохранение отчета в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))
    open_file(output_file)


def open_file(output_file: str):
    """
    Открывает указанный файл в текстовом редакторе операционной системы.
    Открывает файл, который указан в output_file, в текстовом редакторе операционной системы.

    Входные данные:
    -

    Выходные данные:
    -

    Автор:
    - Чибиров Руслан
    """
    # Проверяем операционную систему
    if sys.platform.startswith('win'):
        # Для Windows
        subprocess.Popen(['notepad.exe', output_file])
    elif sys.platform.startswith('darwin'):
        # Для MacOS
        subprocess.Popen(['open', output_file])
    else:
        print("Открытие файла не поддерживается на данной операционной системе.")
