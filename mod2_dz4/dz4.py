#Каждое задание сделал в новой фигуре для удобности проверки

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
penguins = sns.load_dataset('penguins')
df = pd.DataFrame(penguins)

print(df.isna().sum()) # Проверяем все ли у нас есть значения

#Заполняем пропуски в даннных.
#Так как это числовые данные, берем среднее значение для наполнения
df['bill_length_mm'] = df['bill_length_mm'].fillna(df['bill_length_mm'].mean())
df['bill_depth_mm'] = df['bill_depth_mm'].fillna(df['bill_depth_mm'].mean())
df['flipper_length_mm'] = df['flipper_length_mm'].fillna(df['flipper_length_mm'].mean())
df['body_mass_g'] = df['body_mass_g'].fillna(df['body_mass_g'].mean())
# В данной задаче эта колонка не в приоритете по важности данных.
# По этому лучше будет удалить чем заполнять рандомом
df = df.dropna(subset=['sex'])
print(f'Заполнили средними значениями ->\n{df.isna().sum()}')

plt.figure(figsize=(14,8)) # 4-ри графика к первому заданию
plt.subplot(2,2,1) # index graph 1
sns.scatterplot(data= df, x='flipper_length_mm',y='body_mass_g', hue=df['species'])
plt.title('Задание 1. Распредиление веса и роста птиц')
plt.grid(axis='y')
plt.xlabel('Длина крыла(мм)')
plt.ylabel('Масса тела(г)')

plt.subplot(2,2,2) # index graph 2
sns.histplot(data=df, x='flipper_length_mm',y='body_mass_g')
plt.xlabel('Длина крыла(мм)')
plt.ylabel('Масса тела(г)')

plt.subplot(2,2,3) # index graph 3
sns.barplot(data=df, x='flipper_length_mm', y='body_mass_g')
plt.xlabel('Длина крыла(мм)')
plt.ylabel('Масса тела(г)')
plt.grid(axis='y')
plt.xticks(rotation=90) # улучшаем читаемость значений по Х (Поворот на 90 градусов)
plt.xlim(0,55) # Ограничиваем длину оси Х

plt.subplot(2,2,4) # index graph 4
sns.kdeplot(data=df, x='flipper_length_mm', y='body_mass_g', fill=True, cmap="rocket")
plt.xlabel('Длина крыла(мм)')
plt.ylabel('Масса тела(г)')


type_peng = df['species']
flipper = df['flipper_length_mm']

plt.figure(figsize=(8,5)) # Создаем новую фигуру(полотно) для графиков задания 2
plt.subplot(2,2,1)
sns.boxplot(data=df, x=type_peng, y=flipper, hue=df['species'])
plt.title('Задание 2. Длина плавника относительно типа птиц')
plt.xlabel('Вид птиц')
plt.ylabel('Длина крыла(мм)')
plt.grid(axis='y')

#Новая фигура для задания 3
corr_df = df.corr(numeric_only=True)
plt.figure(figsize=(12,5))
sns.heatmap(corr_df, annot=True, vmin=-1)
plt.title('Задание 3. График корреляции')



plt.show()
