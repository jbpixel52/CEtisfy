# %%
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
setpath = 'tf_mini.csv'
countrypath ='playlists/Top Songs - Global Oct-26-2021.json'

# %%


class k_means_structure:
    def __init__(self, setpath, countrypath):
        self.sampleframe = pd.DataFrame(pd.read_csv(setpath).sample(n=500), columns=['energy', 'valence', 'tempo', 'duration',
                                                                                    'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'])  # removed 'us_popularity_estimate', and 'release year'

        self.countryframe = pd.DataFrame(pd.read_json(countrypath), columns=[
                                         'energy', 'valence', 'tempo', 'lenght', 'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'])
        self.sampleframe['set'] = 2 # SET 2 -> BIG DATASET
        self.countryframe['set'] = 20  # SET 20-> PER COUNTRY TOP 50
        self.countryframe.rename(columns={'lenght': 'duration'}, inplace=True)
        self.countryframe['duration'] = self.countryframe['duration'].div(1000).round(2)
        
        self.countryframe.info()
        self.fullframe = pd.concat([self.countryframe, self.sampleframe])

        self.fullframe.info()

        self.kmeans = KMeans(n_clusters=2).fit(self.fullframe)
        self.fullframe['cluster'] = self.kmeans.labels_
        print(f"LABELS: {self.kmeans.labels_}")
        centroids = pd.DataFrame(self.kmeans.cluster_centers_)
        print(self.fullframe)
        print('COUNT PER CLUSTER', self.fullframe.groupby('cluster').count())
        
        
        
        
        self.desc =self.fullframe.groupby('cluster').describe()
        print ('### DESCRIPTION PER CLUSTER ###')
        print ( self.desc)
        self.desc.to_excel('description.xlsx')


# %%
