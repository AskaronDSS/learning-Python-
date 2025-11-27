import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class IrisDataAnalysis:
    def __init__(self):
        self.iris = load_iris()
        self.df = self.create_dataframe()

    def create_dataframe(self):
        df = pd.DataFrame(data=self.iris.data,columns=self.iris.feature_names)
        df['target'] = self.iris.target
        df['species'] = df['target'].apply(lambda x: self.iris.target_names[x])
        return df

    def task_A(self):
        print("====== Task А ======\n\n")
        print("Форма даных (рядки, столбики):", self.df.shape)
        print("\nТипы даных:")
        print(self.df.dtypes)
        print("\nПервые 3 ряда с датасета:")
        print(self.df.head(3))
        print("\n")

    def task_B(self):
        print("====== Task B ======\n\n")
        print("Ключи датасета:", self.iris.keys())
        print("Розмер даных (рядки, столбики):", self.iris.data.shape)
        print("Названия характеристик:", self.iris.feature_names)
        print("\nОписание датасета:")
        print(self.iris.DESCR)
        print("\n")

    def task_C(self):
        print("====== Task C ======\n\n")
        print(self.df.describe())
        print("\n")
        print(self.df)

    def task_D(self, species_name):
        species_data = self.df[self.df['species'] == species_name]
        print(f"====== Задание D ======\n\n"
              f"=== Наблюдения для вида: {species_name} ===")
        print(species_data.head(2))
        return species_data
    def task_E(self):
        plt.figure(figsize=(12,6))
        plt.subplot(2,2,1)
        sns.scatterplot(
            data=self.df,
            x=self.df['sepal length (cm)'],
            y=self.df['sepal width (cm)'],
            hue=self.df['species'])
        plt.grid()
        plt.subplot(2,2,2)
        sns.boxplot(data=self.df,
            x=self.df['target'],
            y=self.df['sepal length (cm)'],
            hue=self.df['species'])
        plt.grid(axis='y')
        plt.subplot(2,2,3)
        sns.barplot(data=self.df,
            x=self.df['sepal length (cm)'],
            y=self.df['sepal width (cm)'],
            hue=self.df['species'],
            )
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.show()

    def task_F(self):
        plt.figure(figsize=(6,6))
        sns.histplot(data=self.df, x=self.df['target'],hue=self.df['species'])
        plt.grid(axis='y')
        plt.show()
    def task_G_and_H(self):
        X = self.df[self.iris.feature_names]
        y = self.df['target']

        X_train,X_test,y_train,y_test = train_test_split(
            X,y,test_size=0.3,random_state=42
        )
        print(f'====== Задание G и H ======\n\n'
              f'Набор для тренировки:\n{X_train.shape[0]}\n'
              f'Набор для тестирования:\n{X_test.shape[0]}\n'
              f'Первые строки тренеровочного набора:\n{X_train.head()}\n'
              f'у_тренировочное:\n{y_train.head()}\n'
              f'Первые строки тестового набора:\n{X_test.head()}\n'
              f'у_тест:\n{y_test.head()}\n'
              )
    def task_I(self):
        X = self.df[self.iris.feature_names]
        y = self.df['target']
        X_train,X_test,y_train,y_test = train_test_split(
            X,y,test_size=0.2,random_state=42
        )
        print(f'====== Задание I ======\n\n{self.df['target']}')
        print(f'Набор для тренировки:\n{X_train.shape[0]}\n'
              f'Набор для тестирования:\n{X_test.shape[0]}\n'
              f'Первые строки тренеровочного набора:\n{X_train.head()}\n'
              f'у_тренировочное:\n{y_train.head()}\n'
              f'Первые строки тестового набора:\n{X_test.head()}\n'
              f'у_тест:\n{y_test.head()}\n'
              )
    def task_J(self):
        X = self.df[self.iris.feature_names]
        y = self.df['target']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        print(f"Количество тренировочных данных: {X_train.shape[0]}")
        print(f"Количество тестовых данных: {X_test.shape[0]}")

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train,y_train)

        y_pred = knn.predict(X_test)

        print(f'====== Задание J ======\n'
              f'Прогнозы классов:\n{y_pred}\n'
              f'Наши классы(реальные)\n{y_test}\n'
              f'Точность: {accuracy_score(y_test,y_pred)}')
if __name__ == "__main__":
    anal = IrisDataAnalysis()
    anal.task_A()
    anal.task_B()
    anal.task_C()
    setosa = anal.task_D('setosa')
    versicolor = anal.task_D('versicolor')
    virginica = anal.task_D('virginica')
    anal.task_E()
    anal.task_F()
    anal.task_G_and_H()
    anal.task_I()
    anal.task_J()