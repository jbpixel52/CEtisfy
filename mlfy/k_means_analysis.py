# %%
import numpy as np
import json
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import pandas as pd
# %%
sns.set_style('darkgrid')
# path='../data/track_features/tf_mini.csv'
path = '../data/track_features/tf_mini.csv'
df_k_means = pd.DataFrame(pd.read_csv(path), columns=['energy','valence','tempo','duration','danceability','key','loudness','speechiness','acousticness','instrumentalness','liveness'])
# %%

kmeans = KMeans(n_clusters=2).fit(df_k_means)

df_k_means['cluster'] = kmeans.labels_
print(f"LABELS: {kmeans.labels_}")


# print(f"features in kmeans: {kmeans.n_feature_in_}")
# print(f"feature names in kmeans: {kmeans.feature_names_in_}")

centroids = kmeans.cluster_centers_
print(f"Centroides:\n{centroids}")
# %%
plt.figure(figsize=(15,15))
sns.pairplot(data=df_k_means,hue='cluster',)
features=["energy","valence","tempo", "duration","danceability","key","loudness","speechiness","acousticness","instrumentalness","liveness"]


# for feature1 in features:
#     for feature2 in features:
#         if feature1 is not feature2:
#              sns.scatterplot(data=df_k_means,x=feature1,y=feature2,hue='cluster')
             


# %%
