# -*- coding: utf-8 -*-
"""LVADSUSR75_barathvaraj_lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXrmaF_KzUNDwd4Jc-uGaglsX8no-FZp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df=pd.read_csv("/content/drive/MyDrive/pred_analysis_datasets/finalassess/seeds.csv")
df

from matplotlib import pyplot as plt
df.plot(kind='scatter', x='Area', y='Perimeter', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

df.info()

df.isna().sum()

df.fillna(method='bfill',inplace=True)
df.isna().sum()

from sklearn.ensemble import IsolationForest
iso=IsolationForest(contamination=0.02)
outliers=iso.fit_predict(df)
df_outliers=df.iloc[np.where(outliers==-1)]
df_outliers
df.drop(df_outliers.index,inplace=True)
df.info()

from sklearn.decomposition import PCA
pca=PCA(n_components=4)
X=pca.fit_transform(df)

from sklearn.metrics import silhouette_score,davies_bouldin_score,calinski_harabasz_score
cluster_list=[1,2,3,4,5,6,7,8]
sum_squared_lst=[]
score_list=[]
for i in cluster_list:
  kmeans=KMeans(n_clusters=i)
  kmeans.fit(X)
  sse=kmeans.inertia_
  sum_squared_lst.append(sse)
print(score_list)
sns.lineplot(x=cluster_list,y=sum_squared_lst)
plt.show()

print("From the elbow graph we can see that 2 is the optimal cluster number")
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
X_pred=kmeans.predict(X)
sil_score=silhouette_score(X,X_pred)
davies_score=davies_bouldin_score(X,X_pred)
cal_score=calinski_harabasz_score(X,X_pred)
print("Silhouette Score = ", sil_score)
print("Davies Bouldin Score = ", davies_score)
print("Calinski Harabasz Score = ", cal_score)

df['clusters']=X_pred
print(df)

cluster_centers=kmeans.cluster_centers_
sns.scatterplot(data=df,x='Area',y='Perimeter', hue='clusters')
plt.title("Clusters")
plt.show()