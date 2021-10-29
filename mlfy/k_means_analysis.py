# %%
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix
path = '../data/track_features/tf_mini.csv'



# %%
class k_means_structure():
    def __init__(self):
        self.df_k_means = pd.DataFrame(pd.read_csv(path), columns=['energy', 'valence', 'tempo', 'duration',
                                'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness','us_popularity_estimate','release_year'])
        self.kmeans = KMeans(n_clusters=2).fit(self.df_k_means)
        self.df_k_means['cluster'] = self.kmeans.labels_
        print(f"LABELS: {self.kmeans.labels_}")
        centroids = pd.DataFrame(self.kmeans.cluster_centers_)
