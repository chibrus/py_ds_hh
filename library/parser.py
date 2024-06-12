"""
Модуль для получения данных о вакансиях с сайта hh.ru, сохранения их в файл Excel и подсчета статистики.

Автор:
- Глинник Егор

Функции:
- get_data(query, page): Отправляет запрос на сервер hh.ru и получает данные о вакансиях.
- excel_generator(ws, data, query_city): Генерирует содержимое Excel-файла на основе полученных данных о вакансиях.
- main(query, query_city): Основная функция, вызывает остальные функции для получения данных, генерации Excel и подсчета статистики.

Переменные:
- count: Счетчик количества обработанных вакансий.
- gradesG: Список для подсчета количества вакансий по категориям (Junior, Middle, Senior).
- postsG: Список для подсчета количества вакансий по должностям (Backend, Frontend, QA, Аналитик, Mobile).

Пример использования (если файл используется как скрипт):
- query: Строка с запросом для поиска вакансий.
- query_city: Строка с названием города для фильтрации вакансий.
"""

import requests
import openpyxl
import os


count = 0
gradesG = [0, 0, 0, 0]     # Junior, Middle, Senior
postsG = [0, 0, 0, 0, 0]   # Backend, Frontend, QA, Аналитик, Mobile


def get_data(query, page):
    """
    Отправляет запрос на сервер hh.ru и получает данные о вакансиях.

    Входные данные:
    - query: Строка с запросом для поиска вакансий.
    - page: Номер страницы с результатами поиска.

    Выходные данные:
    - response.json(): JSON-ответ с данными о вакансиях.

    Автор:
    - Глинник Егор
    """
    response = requests.get(f"https://api.hh.ru/vacancies?text={query}&page={page}&area=113")
    return response.json()


def excel_generator(ws, data, query_city):
    """
    Генерирует содержимое Excel-файла на основе полученных данных о вакансиях.

    Входные данные:
    - ws: Объект рабочего листа Excel-файла.
    - data: JSON-данные о вакансиях.
    - query_city: Строка с названием города для фильтрации вакансий.

    Выходные данные:
    -

    Автор:
    - Глинник Егор
    """
    global gradesG
    global postsG
    global count
    for vacancy in data["items"]:
        title = vacancy["name"]
        city = vacancy["area"]["name"]
        salary_data = vacancy.get("salary", {})
        salary = salary_data.get("from", "-") if salary_data else "-"
        employer_name = vacancy["employer"]["name"]
        experience_data = vacancy.get("experience", {})
        experience = experience_data.get("name", "-") if experience_data else "-"
        requirements = vacancy["snippet"]["requirement"]
        employment_type = vacancy["employment"]["name"]
        has_test = "Есть" if vacancy.get("has_test", False) else "Нет"
        schedule = vacancy.get("schedule", {}).get("name", "-")
        id = vacancy.get("id")

        if query_city == city and salary != "-":
            ws.append([
                title, salary, employer_name, experience, requirements, employment_type,
                has_test, schedule, id
            ])
            count += 1

            name = title.lower()
            # grades
            if "junior" in name:
                gradesG[0] += 1
            elif "middle" in name:
                gradesG[1] += 1
            elif "senior" in name:
                gradesG[2] += 1
            else:
                gradesG[3] += 1
            # posts
            if "android" in name or "ios" in name or "мобильный" in name:
                postsG[4] += 1
            if "frontend" in name:
                postsG[1] += 1
            elif "backend" in name or "разработчик" in name or "программист" in name or "developer" in name:
                postsG[0] += 1
            if "QA" in name or "тестировщик" in name:
                postsG[2] += 1
            if "analyst" in name or "аналитик" in name:
                postsG[3] += 1


def main(query, query_city):
    """
    Основная функция, вызывает остальные функции для получения данных, генерации Excel и подсчета статистики.

    Входные данные:
    - query: Строка с запросом для поиска вакансий.
    - query_city: Строка с названием города для фильтрации вакансий.

    Выходные данные:
    - gradesG: Список с количеством вакансий по категориям (Junior, Middle, Senior).
    - postsG: Список с количеством вакансий по должностям (Backend, Frontend, QA, Аналитик, Mobile).

    Автор:
    - Глинник Егор
    """
    global count
    global gradesG
    global postsG

    page = 0
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Название вакансии", "Зарплата", "Название работодателя", "Опыт работы", "Требования",
               "Тип занятости", "Наличие теста для кандидатов", "График работы", "ПК"])

    while count < 100:
        try:
            data = get_data(query, page)
            excel_generator(ws, data, query_city)
            page += 1
        except Exception as e:
            print(e)
            break

    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    wb.save(os.path.join(data_dir, "data.xlsx"))

    return gradesG, postsG


if __name__ == "__main__":
    query = "Test"
    query_city = "Москва"
    main(query, query_city)
