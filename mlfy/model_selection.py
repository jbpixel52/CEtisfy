#%%
import numpy as np 
import json
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import pandas as pd 
#%%
sns.set_style('darkgrid')
#path='../data/track_features/tf_mini.csv'
path='../data/track_features/tf_mini.csv'
df_top=pd.read_csv(path)
df_k_means = pd.DataFrame(df_top, columns=['energy','valence','tempo'])
# %%

kmeans = KMeans(n_clusters=2,tol=0.1).fit(df_k_means)

print(f"LABELS: {kmeans.labels_}")

df_k_means['cluster']=kmeans.labels_
print(f"features in kmeans: {kmeans.n_features_in_}")
print(f"feature names in kmeans: {kmeans.feature_names_in_}")

centroids = kmeans.cluster_centers_
print(f"Centroides:\n{centroids}")
#%%
# Draw a combo histogram and scatterplot with density contours
x=df_k_means['valence']
y=df_k_means['energy']
f, ax = plt.subplots(figsize=(10, 10))
sns.scatterplot(x=x, y=y, s=5, hue=df_k_means['cluster'])
sns.histplot(x=x, y=y, bins=2, cmap="mako")
sns.kdeplot(x=x, y=y, levels=2,linewidths=1)

# %%

#sns.scatterplot()


# %%
