import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Создание директории для сохранения графиков, если её нет
output_dir = os.path.join(os.path.dirname(__file__), '..', 'graphics')


def create_salary_vs_vacancies_plot(df):
    """
    Создает график зависимости количества вакансий от зарплаты.

    Входные данные:
    df (pandas.DataFrame): DataFrame, содержащий данные о вакансиях. Ожидается наличие столбца 'Зарплата'.

    Выходные данные:
    Создается и сохраняется график в файле 'salary_vs_vacancies.png' в директории output.
    График также отображается на экране.

    Автор:
    Елисеев Иван
    """
    # Преобразование данных по зарплате в числовой формат
    df['Зарплата'] = pd.to_numeric(df['Зарплата'], errors='coerce')
    df.dropna(subset=['Зарплата'], inplace=True)

    # Подсчёт количества вакансий для каждой зарплаты
    salary_counts = df['Зарплата'].value_counts().reset_index()
    salary_counts.columns = ['Зарплата', 'Количество вакансий']

    # Создание графика
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Зарплата', y='Количество вакансий', data=salary_counts, s=100, color='blue', alpha=0.6,
                    edgecolor='w')

    # Настройка графика
    plt.title('Распределение количества вакансий по зарплате', fontsize=16)
    plt.xlabel('Зарплата', fontsize=14)
    plt.ylabel('Количество вакансий', fontsize=14)
    plt.grid(True)
    plt.tight_layout()

    # Сохранение графика
    output_path = os.path.join(output_dir, 'salary_vs_vacancies.png')
    plt.savefig(output_path, dpi=300)
    plt.show()


def create_experience_vs_vacancies_plot(df):
    """
    Создает график распределения количества вакансий по опыту работы.

    Входные данные:
    df (pandas.DataFrame): DataFrame, содержащий данные о вакансиях. Ожидается наличие столбца 'Опыт работы'.

    Выходные данные:
    Создается и сохраняется график в файле 'experience_vs_vacancies.png' в директории output.
    График отображается на экране.

    Автор:
    Елисеев Иван
    """
    experience_counts = df['Опыт работы'].value_counts().reset_index()
    experience_counts.columns = ['Опыт работы', 'Количество вакансий']

    # Создание графика
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Опыт работы', y='Количество вакансий', data=experience_counts, palette='viridis')

    # Настройка графика
    plt.title('Распределение количества вакансий по опыту работы', fontsize=16)
    plt.xlabel('Опыт работы', fontsize=14)
    plt.ylabel('Количество вакансий', fontsize=14)
    plt.grid(True)
    plt.tight_layout()

    # Сохранение графика
    output_path = os.path.join(output_dir, 'experience_vs_vacancies.png')
    plt.savefig(output_path, dpi=300)
    plt.show()


def create_employment_type_vs_vacancies_plot(df):
    """
    Создает график распределения количества вакансий по типу занятости.

    Входные данные:
    df (pandas.DataFrame): DataFrame, содержащий данные о вакансиях. Ожидается наличие столбца 'Тип занятости'.

    Выходные данные:
    Создается и сохраняется график в файле 'employment_type_vs_vacancies.png' в директории output.
    График отображается на экране.

    Автор:
    Елисеев Иван
    """
    employment_counts = df['Тип занятости'].value_counts().reset_index()
    employment_counts.columns = ['Тип занятости', 'Количество вакансий']

    # Создание графика
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Тип занятости', y='Количество вакансий', data=employment_counts, palette='plasma')

    # Настройка графика
    plt.title('Распределение количества вакансий по типу занятости', fontsize=16)
    plt.xlabel('Тип занятости', fontsize=14)
    plt.ylabel('Количество вакансий', fontsize=14)
    plt.grid(True)
    plt.tight_layout()

    # Сохранение графика
    output_path = os.path.join(output_dir, 'employment_type_vs_vacancies.png')
    plt.savefig(output_path, dpi=300)
    plt.show()


def stack(query):
    """
    Возвращает стек технологий в зависимости от запроса.

    Входные данные:
    query (str): Запрос, который может содержать ключевые слова, указывающие на технологии.

    Выходные данные:
    list: Список технологий, соответствующих запросу.

    Автор:
    Елисеев Иван
    """
    if "python" in query:
        return ['SQL', 'Django', 'Linux', 'Shell', 'Git', 'Flask', 'API', 'Docker']
    elif "c++" in query:
        return ['STL', 'Boost', 'Qt', 'CMake', 'Linux', 'Multithreading', 'OpenGL', 'Git']
    elif "c#" in query:
        return ['.NET', 'ASP.NET', 'Entity Framework', 'LINQ', 'WPF', 'Xamarin', 'Azure', 'SQL']
    elif "javascript" in query:
        return ['Node.js', 'React', 'Vue.js', 'Angular', 'ES6', 'TypeScript', 'Webpack', 'Jest']
    elif "java" in query:
        return ['Spring', 'Hibernate', 'Maven', 'JPA', 'Microservices', 'Kubernetes', 'Jenkins', 'SQL']
    elif "web" in query:
        return ['HTML', 'CSS', 'JavaScript', 'PHP', 'MySQL', 'WordPress', 'Bootstrap', 'jQuery']
    elif "go" in query:
        return ['Golang', 'Docker', 'Kubernetes', 'Microservices', 'REST', 'gRPC', 'PostgreSQL', 'Redis']
    elif "swift" in query:
        return ['iOS', 'Xcode', 'CocoaPods', 'CoreData', 'SwiftUI', 'Objective-C', 'UIKit', 'REST']
    elif "ruby" in query:
        return ['Rails', 'Sinatra', 'RSpec', 'Capistrano', 'Puma', 'Sidekiq', 'PostgreSQL', 'Heroku']
    elif "kotlin" in query:
        return ['Android', 'Ktor', 'Spring', 'Coroutines', 'Koin', 'Jetpack Compose', 'SQL', 'Gradle']
    elif "c" in query.split():
        return ['Embedded', 'RTOS', 'Microcontrollers', 'Linux', 'Kernel', 'GDB', 'Assembly', 'Makefile']
    else:
        return ['SQL', 'Linux', 'Shell', 'Git', 'API', 'Docker']


def create_requirements_vs_vacancies_plot(df, query):
    """
    Создает график распределения количества вакансий по требованиям.

    Входные данные:
    df (pandas.DataFrame): DataFrame, содержащий данные о вакансиях. Ожидается наличие столбца 'Требования'.
    query (str): Запрос, определяющий стек технологий для анализа.

    Выходные данные:
    Создается и сохраняется график в файле 'requirements_vs_vacancies.png' в директории output.
    График отображается на экране.
    """
    keywords = stack(query)
    requirements_counts = {keyword: df['Требования'].str.contains(keyword, case=False, na=False).sum() for keyword in
                           keywords}
    requirements_counts = pd.DataFrame(list(requirements_counts.items()), columns=['Требование', 'Количество вакансий'])

    # Создание графика
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Требование', y='Количество вакансий', data=requirements_counts, palette='magma')

    # Настройка графика
    plt.title('Распределение количества вакансий по требованиям', fontsize=16)
    plt.xlabel('Требование', fontsize=14)
    plt.ylabel('Количество вакансий', fontsize=14)
    plt.grid(True)
    plt.tight_layout()

    # Сохранение графика
    output_path = os.path.join(output_dir, 'requirements_vs_vacancies.png')
    plt.savefig(output_path, dpi=300)
    plt.show()


def create_level_vs_vacancies_plot(level_counts):
    """
    Создает график распределения количества вакансий по уровням.

    Входные данные:
    level_counts (dict): Словарь, содержащий количество вакансий для каждого уровня.

    Выходные данные:
    Создается и сохраняется график в файле 'level_vs_vacancies.png' в директории output.
    График отображается на экране.

    Автор:
    Елисеев Иван
    """
    levels = ['Junior-разработчик', 'Middle-разработчик', 'Senior-разработчик', 'Не указано']
    level_data = pd.DataFrame({'Уровень': levels, 'Количество вакансий': level_counts})

    # Создание графика
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Уровень', y='Количество вакансий', data=level_data, palette='coolwarm')

    # Настройка графика
    plt.title('Распределение количества вакансий по уровням', fontsize=16)
    plt.xlabel('Уровень', fontsize=14)
    plt.ylabel('Количество вакансий', fontsize=14)
    plt.grid(True)
    plt.tight_layout()

    # Сохранение графика
    output_path = os.path.join(output_dir, 'level_vs_vacancies.png')
    plt.savefig(output_path, dpi=300)
    plt.show()


def create_specialty_vs_vacancies_plot(specialty_counts):
    """
    Создает график распределения количества вакансий по специальностям.

    Входные данные:
    specialty_counts (dict): Словарь, содержащий количество вакансий для каждой специальности.

    Выходные данные:
    Создается и сохраняется график в файле 'specialty_vs_vacancies.png' в директории output.
    График отображается на экране.

    Автор:
    Елисеев Иван
    """
    specialties = ['Backend-разработчик', 'Frontend-разработчик', 'QA-инженер', 'Аналитик', 'Mobile-разработчик']
    specialty_data = pd.DataFrame({'Специальность': specialties, 'Количество вакансий': specialty_counts})

    # Создание графика
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Специальность', y='Количество вакансий', data=specialty_data, palette='cubehelix')

    # Настройка графика
    plt.title('Распределение количества вакансий по специальностям', fontsize=16)
    plt.xlabel('Специальность', fontsize=14)
    plt.ylabel('Количество вакансий', fontsize=14)
    plt.grid(True)
    plt.tight_layout()

    # Сохранение графика
    output_path = os.path.join(output_dir, 'specialty_vs_vacancies.png')
    plt.savefig(output_path, dpi=300)
    plt.show()


def main():
    """
    Основная функция для анализа данных о вакансиях.

    Возвращает DataFrame, содержащий данные о вакансиях из файла 'data.xlsx'.

    Автор:
    Елисеев Иван
    """
    # Чтение данных из файла Excel
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.xlsx')
    df = pd.read_excel(file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return df


if __name__ == "__main__":
    main()

