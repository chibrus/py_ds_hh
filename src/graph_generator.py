import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Создание папки "graphics", если она не существует
output_dir = "./graphics"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Загрузка данных из Excel
data = pd.read_excel('./data/data.xlsx')

# Функция для построения графиков в соответствии с заданиями
def generate_reports(data):
    # Перебираем все возможные комбинации переменных для построения отчетов
    columns = data.columns
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            col1 = columns[i]
            col2 = columns[j]

            # графический отчет «кластеризованная столбчатая диаграмма» для пары «качественный атрибут — качественный атрибут»
            if data[col1].dtype == 'object' and data[col2].dtype == 'object':
                sns.countplot(x=col1, hue=col2, data=data)
                plt.title(f'{col1} vs {col2}')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, f'clustered_bar_{col1}_{col2}.png'))
                plt.show()

            elif (data[col1].dtype in ['int64', 'float64']) and data[col2].dtype == 'object':
                # графический отчет «категоризированная гистограмма» для пары «количественный атрибут — качественный атрибут»
                sns.histplot(data=data, x=col1, hue=col2, multiple='stack')
                plt.title(f'{col1} vs {col2}')
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, f'categorized_histogram_{col1}_{col2}.png'))
                plt.show()

                # графический отчет «категоризированная диаграмма “box-and-whiskers”» для пары «количественный атрибут—качественный атрибут»
                sns.boxplot(x=col2, y=col1, data=data)
                plt.title(f'{col1} vs {col2}')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, f'categorized_boxplot_{col1}_{col2}.png'))
                plt.show()

            # графический отчет «категоризированная диаграмма рассеивания» для двух количественных атрибутов и одного качественного атрибута
            elif (data[col1].dtype in ['int64', 'float64']) and (data[col2].dtype in ['int64', 'float64']):
                sns.scatterplot(x=col1, y=col2, hue=col2, data=data)
                plt.title(f'{col1} vs {col2}')
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, f'categorized_scatterplot_{col1}_{col2}.png'))
                plt.show()

# Генерация отчетов
if __name__ == "__main__":
    generate_reports(data)