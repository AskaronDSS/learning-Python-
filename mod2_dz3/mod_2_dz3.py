import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

iris_df = pd.read_csv(url, header=None, names=column_names)

class_setos = iris_df[iris_df['class'] == 'Iris-setosa']#Делаем выборку всех данных по классу Iris-setosa
new_df = iris_df[iris_df['class'] == 'Iris-versicolor'] # Берем данные с датафрейма у которых клас Iris-versicolor для задания 2.1
mean_petal_length_iris = iris_df['petal_length'].mean() # Создаем переменную для удобства использования в формуле нахождения значений больше среднего
count_iris = iris_df[iris_df['petal_length'] > mean_petal_length_iris].groupby('class').size()# наполняем Serios значениями из Датафрейма которые больше среднего

print(f'Задание 1.1 -> {iris_df.groupby('class')['sepal_length'].mean()}\n'
      f'Задание 1.2 :\n{class_setos['petal_width'].max(axis=0)}\n'
      f'Задание 1.3 :\n{iris_df['petal_length'].describe()}"\n'
      f'Задание 2.1 :\n{new_df}\n'
      f'Задание 2.2 :\n{iris_df[iris_df['petal_length'] > 5.0]}\n'
      f'Задание 3.1 :\n{iris_df.groupby('class')['petal_width'].mean()}\n'
      f'Задание 3.2 :\n{iris_df.groupby('class')['sepal_length'].min()}\n'
      f'Задание 3.3 :\n{count_iris}{type(count_iris)}')