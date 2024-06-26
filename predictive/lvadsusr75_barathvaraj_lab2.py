# -*- coding: utf-8 -*-
"""LVADSUSR75_barathvaraj_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16MarhXQSeJ9sW8rEtsTB_dPBQSo0pACP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("/content/drive/MyDrive/pred_analysis_datasets/booking.csv")
# print(df.isna().sum())
# print(df[df.duplicated()])
sns.boxplot(df['average price'])
plt.show()


P75=df['average price'].describe().loc['75%']
P25=df['average price'].describe().loc['25%']
iqr=P75-P25

upper_whisker=P75+iqr*1.5
threshold=2.5
outlier_row=df.iloc[np.where(df['average price']>upper_whisker*threshold)]
print(df.info())
df.drop(33114,axis=0,inplace=True)
print(df.info())

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

transformed_room_type=le.fit_transform(df['room type'])
values_room_type=dict(zip(le.classes_,le.transform(le.classes_)))

transformed_meal_type=le.fit_transform(df['type of meal'])
values_meal_type=dict(zip(le.classes_,le.transform(le.classes_)))

transformed_market_segment=le.fit_transform(df['market segment type'])
values_market_segment=dict(zip(le.classes_,le.transform(le.classes_)))

transformed_booking_status=le.fit_transform(df['booking status'])
values_booking_status=dict(zip(le.classes_,le.transform(le.classes_)))

df['room type']=transformed_room_type
df['type of meal']=transformed_meal_type
df['market segment type']=transformed_market_segment
df['booking status']=transformed_booking_status
df

cor_matrix=df.corr()
cor_matrix

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

X=df.drop(['booking status','date of reservation','Booking_ID'],axis=1)
y=df['booking status']
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.25,random_state=42)

dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)
lr=LogisticRegression()
lr.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,recall_score,f1_score,confusion_matrix
y_pred=dt.predict(X_test)
acc_score=accuracy_score(y_pred,y_test)
print(acc_score)
recall_score=recall_score(y_pred,y_test)
print(recall_score)
f1_score=f1_score(y_pred,y_test)
print(f1_score)
confusion_matrix=confusion_matrix(y_pred,y_test)
print(confusion_matrix)