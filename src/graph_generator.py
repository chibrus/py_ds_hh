import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Чтение данных из файла Excel
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.xlsx')
df = pd.read_excel(file_path)

# Создание директории для сохранения графиков, если её нет
output_dir = os.path.join(os.path.dirname(__file__), '..', 'graphics')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def create_salary_vs_vacancies_plot(df):
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


def create_requirements_vs_vacancies_plot(df):
    keywords = ['SQL', 'Django', 'Linux', 'Shell', 'Git', 'Flask', 'API', 'Docker']
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


def main(grades, posts):
    create_salary_vs_vacancies_plot(df)
    create_experience_vs_vacancies_plot(df)
    create_employment_type_vs_vacancies_plot(df)
    create_requirements_vs_vacancies_plot(df)
    create_level_vs_vacancies_plot(grades)
    create_specialty_vs_vacancies_plot(posts)


# main([1,1,1,1], [1,1,1,1,1])
