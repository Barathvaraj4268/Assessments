# -*- coding: utf-8 -*-
"""pred_analysis_lab2_quiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qBTFJvC4hrvrHea3hwB7qBWkDYVdg8GU
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df_train=pd.read_csv("/content/drive/MyDrive/lab_quiz2/DSAILVA-TRAIN Data - Wheat.csv")
df_test=pd.read_csv("/content/drive/MyDrive/lab_quiz2/DSAILVA-TEST Data - Wheat.csv")
df_train

X=df_train[['Length of kernel','Width of kernel']]
scaler=MinMaxScaler()
X_scaled=scaler.fit_transform(X)
X_scaled

cluster_list=[1,2,3,4,5]
sse_lst=[]

for i in cluster_list:
  kmeans=KMeans(n_clusters=i)
  kmeans.fit(X_scaled)
  sse=kmeans.inertia_
  sse_lst.append(sse)

sns.lineplot(x=cluster_list, y=sse_lst)
plt.show()

kmeans_best_fit=KMeans(n_clusters=2)
kmeans_best_fit.fit(X_scaled)
clusters=kmeans_best_fit.predict(X_scaled)
df_train['cluster']=clusters
df_train

cluster_centers=kmeans_best_fit.cluster_centers_
sns.scatterplot(data=df_train,x='Area',y='Perimeter',hue='cluster')
plt.show()

X_test=df_test[['Length of kernel','Width of kernel']]
X_test_scaled=scaler.fit_transform(X_test)
clusters_test=kmeans_best_fit.predict(X_test_scaled)
df_test['Clusters']=clusters_test
write_file=df_test[['Length of kernel','Width of kernel','Clusters']]
write_file.to_csv("/content/drive/MyDrive/lab_quiz2/model_outcome")