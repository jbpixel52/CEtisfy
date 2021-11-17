# %%
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix
setpath = '../data/track_features/tf_mini.csv'
targetspath = '../playlists/Top Songs - Global Oct-26-2021.json'


# %%
class k_means_structure(setpath, countrypath):
    def __init__(self):
        self.df_k_means = pd.DataFrame(pd.read_csv(path), columns=['energy', 'valence', 'tempo', 'duration',
                                                                   'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'us_popularity_estimate', 'release_year'])
        self.kmeans = KMeans(n_clusters=2).fit(self.df_k_means)
        self.df_k_means['cluster'] = self.kmeans.labels_
        print(f"LABELS: {self.kmeans.labels_}")
        centroids = pd.DataFrame(self.kmeans.cluster_centers_)

        targetframe = pd.DataFrame(pd.read_json(targetspath), columns=['energy', 'valence', 'tempo', 'duration',
                                                            'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'us_popularity_estimate', 'release_year'])

KMS = k_means_structure()

# %%
