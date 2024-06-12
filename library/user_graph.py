import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Создание директории для сохранения графиков, если её нет
output_dir = os.path.join(os.path.dirname(__file__), '..', 'graphics')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def plot_clustered_bar(df, col1, col2):
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)  # Увеличиваем размер шрифта
    ax = sns.barplot(data=df, x=col1, y=col2, palette='husl', alpha=0.8,
                     ci=None)  # Используем яркие цвета и добавляем прозрачность
    plt.title('Кластеризованная столбчатая диаграмма', fontsize=18,
              fontweight='bold')  # Увеличиваем размер заголовка и делаем его жирным
    plt.xlabel(col1, fontsize=14, fontweight='bold')  # Делаем подпись оси x жирной
    plt.ylabel(col2, fontsize=14, fontweight='bold')  # Делаем подпись оси y жирной
    plt.yticks(fontsize=12)

    # Добавляем метки на каждом столбце
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.2f'),
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 5),
                    textcoords='offset points',
                    fontsize=12)

    ax.yaxis.grid(True)
    ax.xaxis.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'clustered_bar.png'))
    plt.show()
    plt.close()


def plot_categorized_histogram(df, col1, col2):
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)  # Увеличиваем размер шрифта
    ax = sns.histplot(data=df, y=col1, x=col2, multiple='stack', alpha=0.8)  # Используем яркие цвета и добавляем прозрачность
    plt.title('Категоризированная гистограмма', fontsize=18, fontweight='bold', color='navy')  # Увеличиваем размер заголовка и делаем его жирным
    plt.xlabel(col1, fontsize=14, fontweight='bold', color='darkblue')  # Делаем подпись оси x жирной
    plt.ylabel(col2, fontsize=14, fontweight='bold', color='darkblue')  # Делаем подпись оси y жирной
    plt.xticks(fontsize=12, ha='right', color='gray')  # Поворачиваем и выравниваем подписи оси x
    plt.yticks(fontsize=12, color='gray')

    ax.yaxis.grid(True)
    ax.xaxis.grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'categorized_histogram.png'))
    plt.show()
    plt.close()


def plot_categorized_boxplot(df, col1, col2):
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)  # Увеличиваем размер шрифта
    ax = sns.boxplot(data=df, x=col2, y=col1, palette='pastel', linewidth=2.5,
                     width=0.8)  # Увеличиваем толщину линий и ширину коробок
    plt.title('Категоризированная диаграмма Бокса-Вискера', fontsize=22, fontweight='bold',
              color='navy')  # Увеличиваем размер заголовка и делаем его жирным
    plt.xlabel(col2, fontsize=16, fontweight='bold', color='darkblue')  # Делаем подпись оси x жирной
    plt.ylabel(col1, fontsize=16, fontweight='bold', color='darkblue')  # Делаем подпись оси y жирной
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
    # Аггрегирование данных для подсчета количества вакансий
    agg_df = df.groupby([col1, col2]).size().reset_index(name='Количество вакансий')

    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", font_scale=1.2)  # Увеличиваем размер шрифта
    ax = sns.scatterplot(data=agg_df, x=col1, y='Количество вакансий', hue=col2, s=150, palette='viridis', alpha=0.8, edgecolor='k', linewidth=1.5)  # Увеличиваем размер маркеров и добавляем прозрачность, также добавляем черные контуры маркерам
    plt.title('Категоризированная диаграмма рассеивания', fontsize=22, fontweight='bold', color='navy')  # Увеличиваем размер заголовка и делаем его жирным
    plt.xlabel(col1, fontsize=16, fontweight='bold', color='darkblue')  # Делаем подпись оси x жирной
    plt.ylabel('Количество вакансий', fontsize=16, fontweight='bold', color='darkblue')  # Делаем подпись оси y жирной
    plt.xticks(fontsize=14, color='gray')  # Делаем подписи оси x серыми
    plt.yticks(fontsize=14, color='gray')  # Делаем подписи оси y серыми
    plt.legend(title=col2, fontsize=12, title_fontsize=14)  # Увеличиваем размер шрифта в легенде и делаем его жирным

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'categorized_scatter.png'))
    plt.show()
    plt.close()


def main(col1, col2, plot_type):
    # Путь к файлу данных
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.xlsx')

    # Загрузка данных
    df = pd.read_excel(file_path)

    # Построение графиков в зависимости от типа
    if plot_type == 'clustered_bar':
        plot_clustered_bar(df, col1, col2)
    elif plot_type == 'categorized_histogram':
        plot_categorized_histogram(df, col1, col2)
    elif plot_type == 'categorized_boxplot':
        plot_categorized_boxplot(df, col1, col2)
    elif plot_type == 'categorized_scatter':
        plot_categorized_scatter(df, col1, col2)


if __name__ == "__main__":
    main()




