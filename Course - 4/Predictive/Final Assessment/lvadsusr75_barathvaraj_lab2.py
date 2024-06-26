# -*- coding: utf-8 -*-
"""LVADSUSR75_barathvaraj_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qVILWL7-wLnb9gcRwIhlx54YVwBfoMsi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
import xgboost

df=pd.read_csv("/content/drive/MyDrive/pred_analysis_datasets/finalassess/auto-mpg.csv")
df

from matplotlib import pyplot as plt
df['mpg'].plot(kind='hist', bins=20, title='mpg')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
df.plot(kind='scatter', x='horsepower', y='weight', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

df.info()

df.columns

df.info()
df.loc[df['horsepower']=='?','horsepower']=np.nan
print(df['horsepower'].unique())
df['horsepower'].astype('float64')
df.info()

df.isna().sum()

df['displacement'].fillna(df['displacement'].median(),inplace=True)
df['horsepower'].fillna(df['horsepower'].median(),inplace=True)
df['acceleration'].fillna(df['acceleration'].median(),inplace=True)
df.isna().sum()

df.drop(['car name'], axis=1, inplace=True)
from sklearn.ensemble import IsolationForest
iso=IsolationForest(contamination=0.02)
outliers=iso.fit_predict(df)
df_outliers=df.iloc[np.where(outliers==-1)]
df.drop(df_outliers.index,inplace=True)
df.info()

df.corr()
print("Displacement is a highly correlated column so we can drop it")
df.drop(['displacement'], axis=1,inplace=True)

from sklearn.preprocessing import StandardScaler
X=df.drop(['mpg'],axis=1)
y=df['mpg']
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

lr=LinearRegression()
rf=RandomForestRegressor()
dt=DecisionTreeRegressor()
xgb=xgboost.XGBRegressor()
svr=SVR()

lr.fit(X_train,y_train)
rf.fit(X_train,y_train)
dt.fit(X_train,y_train)
xgb.fit(X_train,y_train)
svr.fit(X_train,y_train)

y_pred_lr=lr.predict(X_test)
y_pred_rf=rf.predict(X_test)
y_pred_dt=dt.predict(X_test)
y_pred_xgb=xgb.predict(X_test)
y_pred_svc=svr.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

mean_squared_lr=mean_squared_error(y_test,y_pred_lr)
mean_squared_rf=mean_squared_error(y_test,y_pred_rf)
mean_squared_dt=mean_squared_error(y_test,y_pred_dt)
mean_squared_xgb=mean_squared_error(y_test,y_pred_xgb)
mean_squared_svr=mean_squared_error(y_test,y_pred_svc)

x_cols_m=['Logistic Regression','Random Forest','Decision Tree','XGBoost','SVC']
y_cols_m=[mean_squared_lr,mean_squared_rf,mean_squared_dt,mean_squared_xgb,mean_squared_svr]

sns.barplot(x=y_cols_m, y=x_cols_m,orient='h')
plt.show()

r2_score_lr=r2_score(y_test,y_pred_lr)
r2_score_rf=r2_score(y_test,y_pred_rf)
r2_score_dt=r2_score(y_test,y_pred_dt)
r2_score_xgb=r2_score(y_test,y_pred_xgb)
r2_score_svr=r2_score(y_test,y_pred_svc)

x_cols_r2=['Logistic Regression','Random Forest','Decision Tree','XGBoost','SVR']
y_cols_r2=[r2_score_lr,r2_score_rf,r2_score_dt,r2_score_xgb,r2_score_svr]

sns.barplot(x=y_cols_r2, y=x_cols_r2,orient='h')
plt.show()

print([(i,j) for i,j in zip(x_cols_m,y_cols_m)])
print([(i,j) for i,j in zip(x_cols_r2,y_cols_r2)])
print("The mean squared error for random forest is low and r2 score for random forest is high. So Random forest is the best performing model")