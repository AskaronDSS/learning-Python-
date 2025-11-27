import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#Загрузка данных
penguins = sns.load_dataset("penguins")
print(penguins.head())
#удаление полей со значениями "нан"
penguins = penguins.dropna()
# разделение сета на две части.
# Х - то на что будет смотреть модель.
# У - то что мы хотим предвидить
X = penguins.drop("species", axis=1)
y = penguins["species"]


numeric_features = X.select_dtypes(include=["int64", "float64"]).columns
categorical_features = X.select_dtypes(include=["object"]).columns

# Разделяем данные на две части 80%/20%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Маштабируем числовые признаки
numeric_transformer = Pipeline(steps=[
('scaler', StandardScaler())
])

# Переводим текстовые признаки в числа
categorical_transformer = Pipeline(steps=[
('encoder', OneHotEncoder(handle_unknown='ignore'))
])
# обьекдиняем
preprocessor = ColumnTransformer(
transformers=[
('num', numeric_transformer, numeric_features),
('cat', categorical_transformer, categorical_features)
])
pipeline = Pipeline(steps=[
('preprocessor', preprocessor),
('classifier', RandomForestClassifier(random_state=42))
])

scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print("Средняя точность cross-validation:", scores.mean())
a = "Средняя точность cross-validation:", scores.mean()
#настройка GridSearch
param_grid = {
'classifier__n_estimators': [100, 200],
'classifier__max_depth': [None, 5, 10],
'classifier__min_samples_split': [2, 5]
}
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Лучшие:", grid_search.best_params_)

# Анализ результатов
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("\nОтчет классификации:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=best_model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.show()