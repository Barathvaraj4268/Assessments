# -*- coding: utf-8 -*-
"""pred_analysis_lab_quiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Fr8vYyLMaIyVWZJSNs_wcZ1zXFTJ0j6
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import xgboost

df=pd.read_csv("/content/drive/MyDrive/lab_quiz/DSAI-LVA-DATASET for Quiz.csv")
df

df.info()

df.isna().sum()

for ind,col in df.iterrows():
  if col['ParentEducation'] == 'College':
    df.loc[ind,'ParentEducation']=np.random.choice(['Masters', 'Bachelors'])
  elif col['ParentEducation'] == 'HighSchool':
    df.loc[ind,'ParentEducation']=np.random.choice(['School', 'High School', 'Not Educated'])
df['ParentEducation'].value_counts()

for ind,col in df.iterrows():
  if (str(col['Pass'])=='Yes') & (col['PreviousTestScore']>=85):
    df.loc[ind,'Pass_criteria']='Pass with a high grade'
  elif (str(col['Pass'])=='Yes') & (col['PreviousTestScore']<=85):
    df.loc[ind,'Pass_criteria']='Pass with a low grade'
  elif(str(col['Pass'])=='No'):
    df.loc[ind,'Pass_criteria']='Fail'
df

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['ParentEducation']=le.fit_transform(df['ParentEducation'])
df['Pass']=le.fit_transform(df['Pass'])
df['Pass_criteria']=le.fit_transform(df['Pass_criteria'])
lst=dict(zip(le.classes_,le.transform(le.classes_)))
print(lst)
df

total_rows = len(df)
train_ratio = 0.7
train_size = int(total_rows * train_ratio)
test_size = total_rows - train_size

df_shuffled = df.sample(frac=1, random_state=42)

train_data = df_shuffled.head(train_size)
test_data = df_shuffled.tail(test_size)

train_data.to_csv("/content/drive/MyDrive/lab_quiz/training_data.csv")
test_data.to_csv("/content/drive/MyDrive/lab_quiz/test_data.csv")

train_data_import=pd.read_csv("/content/drive/MyDrive/lab_quiz/training_data.csv")
test_data_import=pd.read_csv("/content/drive/MyDrive/lab_quiz/test_data.csv")

X_train=train_data_import.drop(['Pass_criteria'], axis=1)
X_test=test_data_import.drop(['Pass_criteria'], axis=1)
y_train=train_data_import['Pass_criteria']
y_test=test_data_import['Pass_criteria']

lr=LogisticRegression()
lr.fit(X_train,y_train)

dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)

rf=RandomForestClassifier()
rf.fit(X_train,y_train)

svc=SVC()
svc.fit(X_train,y_train)

xgb=xgboost.XGBClassifier()
xgb.fit(X_train,y_train)

knn=KNeighborsClassifier()
knn.fit(X_train,y_train)

from sklearn.metrics import accuracy_score

y_pred_lr=lr.predict(X_test)
y_pred_dt=dt.predict(X_test)
y_pred_rf=rf.predict(X_test)
y_pred_svc=svc.predict(X_test)
y_pred_xgb=xgb.predict(X_test)
y_pred_knn=knn.predict(X_test)

import matplotlib.pyplot as plt
import seaborn as sns

lr_score=accuracy_score(y_test,y_pred_lr)
dt_score=accuracy_score(y_test,y_pred_dt)
rf_score=accuracy_score(y_test,y_pred_rf)
svc_score=accuracy_score(y_test,y_pred_svc)
xgb_score=accuracy_score(y_test,y_pred_xgb)
knn_score=accuracy_score(y_test,y_pred_knn)
x=['Logistic Regression', 'Decision Tree','Random Forest', 'Support Vector Classifier','XGBoost Classifier',' KNeighbors Classifier']
y=[lr_score, dt_score, rf_score,svc_score, xgb_score,knn_score]
model_outcome=[(i,j) for (i,j) in zip(x,y)]
plt.title('Model Accuracies')
plt.ylabel('Accuracy Score')
plt.xlabel('Models')
sns.barplot(x=y,y=x, orient='h')
plt.show()
plt.savefig('/content/drive/MyDrive/lab_quiz/model_comparison.png')

import json
with open('/content/drive/MyDrive/lab_quiz/model_outcome.txt', 'w') as f:
    json.dump(model_outcome, f)