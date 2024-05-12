import pandas as pd
import os

df = pd.read_excel('./data/data.xlsx')

# Создаем папку для сохранения отчетов
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

def vacancy_report(df: pd.DataFrame, city: str) -> pd.DataFrame:
    """
    Создает отчет о вакансиях для указанного города.

    Parameters:
    df (pd.DataFrame): DataFrame с данными о вакансиях.
    city (str): Название города для отчета.

    Returns:
    pd.DataFrame: Отчет о вакансиях для указанного города.
    """
    
    city_data = df[df['Город'] == city]
    return city_data[['Название вакансии', 'Зарплата (руб)', 'Требуемый опыт работы']]


def programming_language_report(df: pd.DataFrame, language: str) -> pd.DataFrame:
    """
    Создает отчет о вакансиях для указанного языка программирования.

    Parameters:
    df (pd.DataFrame): DataFrame с данными о вакансиях.
    language (str): Название языка программирования для отчета.

    Returns:
    pd.DataFrame: Отчет о вакансиях для указанного языка программирования.
    """
    
    language_data = df[df['Язык программирования'] == language]
    return language_data[['Название вакансии', 'Зарплата (руб)', 'Требуемый опыт работы']]


def position_report(df: pd.DataFrame, position: str) -> pd.DataFrame:
    """
    Создает отчет о вакансиях для указанной должности.

    Parameters:
    df (pd.DataFrame): DataFrame с данными о вакансиях.
    position (str): Название должности для отчета.

    Returns:
    pd.DataFrame: Отчет о вакансиях для указанной должности.
    """
    
    position_data = df[df['Должности'] == position]
    return position_data[['Название вакансии', 'Зарплата (руб)', 'Требуемый опыт работы']]


def salary_range_report(df: pd.DataFrame, min_salary: int, max_salary: int) -> pd.DataFrame:
    """
    Создает отчет о вакансиях с зарплатой в указанном диапазоне.

    Parameters:
    df (pd.DataFrame): DataFrame с данными о вакансиях.
    min_salary (int): Минимальная зарплата.
    max_salary (int): Максимальная зарплата.

    Returns:
    pd.DataFrame: Отчет о вакансиях с зарплатой в указанном диапазоне.
    """
    
    salary_data = df[(df['Зарплата (руб)'] >= min_salary) & (df['Зарплата (руб)'] <= max_salary)]
    return salary_data[['Название вакансии', 'Зарплата (руб)', 'Требуемый опыт работы']]


def pivot_table_report(df: pd.DataFrame, index_column: str, columns_column: str, values_column: str) -> pd.DataFrame:
    """
    Создает сводную таблицу на основе указанных столбцов.

    Parameters:
    df (pd.DataFrame): DataFrame с данными.
    index_column (str): Имя столбца, который будет использоваться в качестве индекса.
    columns_column (str): Имя столбца, который будет использоваться в качестве столбцов.
    values_column (str): Имя столбца, значения которого будут агрегированы.

    Returns:
    pd.DataFrame: Сводная таблица.
    """
    return pd.pivot_table(df, index=index_column, columns=columns_column, values=values_column, aggfunc='count')


# Создаем отчет о вакансиях в Москве
moscow_vacancies = vacancy_report(df, 'Москва')
moscow_vacancies.to_markdown(os.path.join(output_folder, 'moscow_vacancies.md'), index=False)

# Создаем отчет о вакансиях для стажеров
developer_vacancies = position_report(df, 'Стажер')
developer_vacancies.to_markdown(os.path.join(output_folder, 'developer_vacancies.md'), index=False)

# Создаем отчеты о вакансиях с зарплатой от 50000 до 80000 рублей
salary_range = salary_range_report(df, 50000, 80000)
salary_range.to_markdown(os.path.join(output_folder, 'salary_range_report.md'), index=False)

# Создаем отчет о вакансиях для языка программирования Python
python_vacancies = programming_language_report(df, 'Python')
python_vacancies.to_markdown(os.path.join(output_folder, 'python_vacancies.md'), index=False)

# Создаем сводную таблицу по городам и компаниям
pivot_table = pivot_table_report(df, 'Город', 'Компания', 'Название вакансии')
pivot_table.to_markdown(os.path.join(output_folder, 'pivot_table_report.md'))