"""
Модуль для построения различных видов графиков на основе данных из файла.

Этот модуль включает функции для:
- Построения кластеризованной столбчатой диаграммы.
- Построения категоризированной гистограммы.
- Построения категоризированной диаграммы Бокса-Вискера.
- Построения категоризированной диаграммы рассеивания.

Функции:
- plot_clustered_bar(df, col1, col2):
Построение кластеризованной столбчатой диаграммы.
- plot_categorized_histogram(df, col1, col2):
Построение категоризированной гистограммы.
- plot_categorized_boxplot(df, col1, col2):
Построение категоризированной диаграммы Бокса-Вискера.
- plot_categorized_scatter(df, col1, col2):
Построение категоризированной диаграммы рассеивания.
- main(col1, col2, plot_type):
Основная функция для построения графиков в зависимости от выбранного типа.

Авторы:
- Елисеев Иван
"""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Создание директории для сохранения графиков, если её нет
output_dir = os.path.join(os.path.dirname(__file__), '..', 'graphics')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def plot_clustered_bar(df, col1, col2):
    """
    Построение кластеризованной столбчатой диаграммы.

    Входные данные:
    df (DataFrame): База данных.
    col1 (str): Название столбца для оси x.
    col2 (str): Название столбца для оси y.

    Выходные данные:
    -

    Автор:
    - Елисеев Иван
    """
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)  # Увеличиваем размер шрифта
    ax = sns.barplot(
        data=df, x=col2, y=col1, hue=col1, dodge=False,
        palette='husl', legend=False, alpha=0.8, errorbar=None
    )
    plt.title('Кластеризованная столбчатая диаграмма', fontsize=18,
              fontweight='bold')  # Увеличиваем размер заголовка и делаем его жирным
    plt.xlabel(col2, fontsize=14, fontweight='bold')  # Делаем подпись оси x жирной
    plt.ylabel(col1, fontsize=14, fontweight='bold')  # Делаем подпись оси y жирной
    plt.yticks(fontsize=12)

    ax.yaxis.grid(True)
    ax.xaxis.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'clustered_bar.png'))
    plt.show()
    plt.close()


def plot_categorized_histogram(df, col1, col2):
    """
    Построение категоризированной гистограммы.

    Входные данные:
    df (DataFrame): База данных.
    col1 (str): Название столбца для оси y.
    col2 (str): Название столбца для оси x.

    Выходные данные:
    -

    Автор:
    - Елисеев Иван
    """
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)
    ax = sns.histplot(data=df, y=col1, x=col2, multiple='stack', alpha=0.8)
    plt.title(
        'Категоризированная гистограмма',
        fontsize=18, fontweight='bold', color='navy'
    )
    plt.xlabel(col2, fontsize=14, fontweight='bold', color='darkblue')
    plt.ylabel(col1, fontsize=14, fontweight='bold', color='darkblue')
    plt.xticks(fontsize=12, ha='right', color='gray')
    plt.yticks(fontsize=12, color='gray')

    ax.yaxis.grid(True)
    ax.xaxis.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'categorized_histogram.png'))
    plt.show()
    plt.close()


def plot_categorized_boxplot(df, col1, col2):
    """
    Построение категоризированной диаграммы Бокса-Вискера.

    Входные данные:
    df (DataFrame): База данных.
    col1 (str): Название столбца для оси y.
    сol2 (str): Название столбца для оси x.

    Выходные данные:
    -

    Автор:
    - Елисеев Иван 
    """
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)  # Увеличиваем размер шрифта
    ax = sns.boxplot(
        data=df, x=col2, y=col1, hue=col1, dodge=False,
        palette='pastel', legend=False, linewidth=2.5, width=0.8
    )  # Увеличиваем толщину линий и ширину коробок
    plt.title('Категоризированная диаграмма Бокса-Вискера', fontsize=22, fontweight='bold',
              color='navy')  # Увеличиваем размер заголовка и делаем его жирным
    plt.xlabel(col2, fontsize=16, fontweight='bold', color='darkblue')
    plt.ylabel(col1, fontsize=16, fontweight='bold', color='darkblue')
    plt.xticks(fontsize=14, ha='right', color='gray')  # Поворачиваем и выравниваем подписи оси x
    plt.yticks(fontsize=14, color='gray')  # Делаем подписи оси y серыми
    plt.grid(True, linestyle='--', alpha=0.7)  # Добавляем пунктирную сетку

    # Добавляем сетку
    ax.yaxis.grid(True)
    ax.xaxis.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'categorized_boxplot.png'))
    plt.show()
    plt.close()


def plot_categorized_scatter(df, col1, col2):
    """
    Построение категоризированной диаграммы рассеивания.

    Входные даннные:
    df (DataFrame): База данных.
    col1 (str): Название столбца для оси x.
    col2 (str): Название столбца для категоризации данных.

    Выходные данные:
    -

    Автор:
    - Елисеев Иван
    """
    # Аггрегирование данных для подсчета количества вакансий
    agg_df = df.groupby([col1, col2]).size().reset_index(name='Количество вакансий')

    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)  # Увеличиваем размер шрифта
    ax = sns.scatterplot(data=agg_df, y=col1, x='Количество вакансий',
                        hue=col2, s=150, palette='viridis', alpha=0.8,
                        edgecolor='k', linewidth=1.5)
    plt.title('Категоризированная диаграмма рассеивания', fontsize=22,
              fontweight='bold', color='navy')
    plt.xlabel('Количество вакансий', fontsize=16, fontweight='bold', color='darkblue')
    plt.ylabel(col1, fontsize=16, fontweight='bold', color='darkblue')
    plt.xticks(fontsize=14, color='gray')  # Делаем подписи оси x серыми
    plt.yticks(fontsize=14, color='gray')  # Делаем подписи оси y серыми
    plt.legend(title=col2, fontsize=12, title_fontsize=14)

    # Добавляем сетку
    ax.yaxis.grid(True)
    ax.xaxis.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'categorized_scatter.png'))
    plt.show()
    plt.close()


def main(col1, col2, plot_type):
    """
    Основная функция для построения графиков в зависимости от выбранного типа.

    Входные данные:
    col1 (str): Название столбца для оси x.
    col2 (str): Название столбца для оси y или категоризации данных.
    plot_type (str): Тип графика для построения.

    Выходные данные:
    -

    Автор:
    - Елисеев Иван
    """
    if col1 != col2:
        # Путь к файлу данных
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.xlsx')

        # Загрузка данных
        df = pd.read_excel(file_path)

        # Построение графиков в зависимости от типа
        if plot_type == 'Столбчатая диаграмма':
            plot_clustered_bar(df, col1, col2)
        elif plot_type == 'Категоризированная гистограмма':
            plot_categorized_histogram(df, col1, col2)
        elif plot_type == 'Диаграмма Бокса-Вискера':
            plot_categorized_boxplot(df, col1, col2)
        elif plot_type == 'Диаграмма рассеивания':
            plot_categorized_scatter(df, col1, col2)
