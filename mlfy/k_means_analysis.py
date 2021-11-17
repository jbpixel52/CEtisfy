# %%
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix
setpath = '../data/track_features/tf_mini.csv'
countrypath = '../playlists/Top Songs - Global Oct-26-2021.json'

# %%
class k_means_structure:
    def __init__(self,setpath,countrypath):
        self.sampleframe = pd.DataFrame(pd.read_csv(setpath).sample(n=50), columns=['energy', 'valence', 'tempo', 'duration',
                                                                   'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness']) #removed 'us_popularity_estimate', and 'release year'
        
        self.countryframe = pd.DataFrame(pd.read_json(countrypath), columns=['energy', 'valence', 'tempo', 'lenght',
                                                            'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'])
        self.sampleframe['set']=1 #SET 1 -> BIG DATASET
        self.countryframe['set']=2 #SET 2-> PER COUNTRY TOP 50
        self.countryframe.rename(columns={'lenght':'duration'},inplace=True)
        self.countryframe.info()
        self.fullframe = pd.concat([self.countryframe, self.sampleframe])
        
        self.fullframe.info()



        self.kmeans = KMeans(init='random').fit(self.fullframe)
        self.fullframe['cluster'] = self.kmeans.labels_
        print(f"LABELS: {self.kmeans.labels_}")
        centroids = pd.DataFrame(self.kmeans.cluster_centers_)
        print(self.fullframe)




KMS = k_means_structure(setpath = setpath, countrypath=countrypath)

# %%
