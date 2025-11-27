import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

titanic = sns.load_dataset("titanic")
print("Размер данных:", titanic.shape)
print(titanic.head())
print(titanic.info())
print(f"----------------------------\n"
      f"До\n"
      f"---------------------------- \n"
      f"{titanic.isna().sum()}")

# ----------------------------
# Очистка данных и подготовка признаков
# ----------------------------
titanic = titanic.drop(["deck", "embark_town", "alive", "class", "who", "adult_male", "alone"], axis=1)
titanic["age"] = titanic["age"].fillna(titanic["age"].median())
titanic["embarked"] = titanic["embarked"].fillna(titanic["embarked"].mode()[0])
titanic["sex"] = LabelEncoder().fit_transform(titanic["sex"])
titanic = pd.get_dummies(titanic, columns=["embarked"], drop_first=True)

titanic["family_size"] = titanic["sibsp"] + titanic["parch"] + 1
titanic["is_alone"] = (titanic["family_size"] == 1).astype(int)
print(f"----------------------------\n"
      f"После\n"
      f"---------------------------- \n"
      f"{titanic.isna().sum()}")

np.random.seed(42)
titles = np.random.choice(["Mr", "Mrs", "Miss", "Master"], size=len(titanic))
titanic["Name"] = ["Person " + title for title in titles]
titanic["Title"] = titanic["Name"].apply(lambda n: n.split()[-1])
titanic = pd.get_dummies(titanic, columns=["Title"], drop_first=True)

# ----------------------------
# EDA – графики
# ----------------------------
plt.figure(figsize=(16, 10))

plt.subplot(2,2,1)
sns.countplot(x="survived", data=titanic, hue="sex")
plt.title("Выжившие по полу")

plt.subplot(2,2,2)
sns.barplot(x="pclass", y="survived", data=titanic, hue="pclass")
plt.title("Выживаемость по классу билета")

plt.subplot(2,2,3)
sns.histplot(titanic["age"], kde=True)
plt.title("Распределение возраста пассажиров")

plt.subplot(2,2,4)
sns.heatmap(titanic.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Корреляционная матрица признаков")

plt.tight_layout()
plt.show()

# ----------------------------
# Подготовка данных для моделей
# ----------------------------
X = titanic.drop(["survived", "Name"], axis=1)
y = titanic["survived"]
print(f' 1 -  - - - -\n{X.head()}2---\n{X}')
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# ----------------------------
# Выбор моделей и обучение
# ----------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")
    print(f"{name}: Средняя точность = {scores.mean():.4f}")

# ----------------------------
# Тонкая настройка
# ----------------------------
param_grid_rf = {
    "n_estimators": [100, 200, 300],
    "max_depth": [3, 5, 7, None],
    "min_samples_split": [2, 5, 10]
}

grid_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5, scoring="accuracy")
grid_rf.fit(X_train, y_train)

print("\nЛучшая модель Random Forest:")
print(grid_rf.best_params_)
print(f"Лучшая точность (CV): {grid_rf.best_score_:.2f}")

best_model = grid_rf.best_estimator_

# ----------------------------
# Оценка модели на тестовой выборке
# ----------------------------

y_pred = best_model.predict(X_test)

print("\n--- Оценка модели на тесте ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1-score: {f1_score(y_test, y_pred):.4f}")
print("\nМатрица ошибок:")
print(confusion_matrix(y_test, y_pred))
print("\nОтчет классификации:")
print(classification_report(y_test, y_pred))

# ----------------------------
# Визуализация важности признаков
# ----------------------------
importances = pd.Series(best_model.feature_importances_, index=X.columns).sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=importances, y=importances.index)
plt.title("Важность признаков")
plt.ylabel("Характеристики")
plt.xlabel("Важность характеристик")
plt.grid(True)
plt.show()
