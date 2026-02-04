import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

EMPLOYED_ENCODING = {
    'Yes': 1,
    'No': 0
}
EDUCATION_ENCODING = {
    'Graduate': 1,
    'Not Graduate': 0
}
PROVERTY_AREA_ENCODING = {
    'Urban': 2,
    'Semiurban': 1,
    'Rural': 0
}
LOAN_STATUS_ENCODING = {
    'Y': 1,
    'N': 0
}
MARRIED_ENCODING = {
    'Yes': 1,
    'No': 0
}
LOAN_ID_ENCODING = {
    'LP001002': 1,
    'LP001003': 2,
    'LP001005': 3,
    'LP001006': 4,
    'LP001008': 5,
    'LP001011': 6,
    'LP001013': 7,
    'LP001014': 8,
    'LP001018': 9,
    'LP001020': 10,
}

DEPENDENTS_ENCODING = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3+': 3
}
GENDER_ENCODING = {
    'Male': 1,
    'Female': 0
}
df = pd.read_csv('loan_data.csv')
df['Gender'] = df['Gender'].map(GENDER_ENCODING)
df['Dependents'] = df['Dependents'].map(DEPENDENTS_ENCODING)
df['Self_Employed'] = df['Self_Employed'].map(EMPLOYED_ENCODING)
df['Education'] = df['Education'].map(EDUCATION_ENCODING)
df['Property_Area'] = df['Property_Area'].map(PROVERTY_AREA_ENCODING)
df['Loan_Status'] = df['Loan_Status'].map(LOAN_STATUS_ENCODING)
df['Married'] = df['Married'].map(MARRIED_ENCODING)
df['Loan_ID'] = df['Loan_ID'].map(LOAN_ID_ENCODING)
df['Loan_ID'] = df['Loan_ID'].fillna(0)
df['Self_Employed'] = df['Self_Employed'].fillna(0)
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
df['Credit_History'] = df['Credit_History'].fillna(0)





target_col = 'Loan_Status' 
X = df.drop(target_col, axis=1)
y = df[target_col]


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


features = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=features)
plt.title('Самые важные поля в вашем датасете')
plt.show()
