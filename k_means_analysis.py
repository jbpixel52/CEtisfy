# %%
import pandas as pd
from sklearn.cluster import KMeans
import os
from sklearn.metrics import accuracy_score
import numpy as np
datasetpath = 'tf_mini.csv'
countrypath = 'playlists/Top Songs - Global Oct-26-2021.json'
directory = os.fsencode('playlists')
global descriptions
descriptions = pd.DataFrame()
global popular_clusters
popular_clusters = {}
# %%


class k_means_structure:
    def __init__(self, setpath, countrypath, countryname):
        self.debug = False
        self.sampleframe = pd.DataFrame(pd.read_csv(setpath).sample(n=500), columns=[
                                        'energy', 'valence', 'tempo', 'duration', 'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'])  # removed 'us_popularity_estimate', and 'release year'
        self.countryname = countryname
        self.countryframe = pd.DataFrame(pd.read_json(countrypath), columns=[
                                         'energy', 'valence', 'tempo', 'lenght', 'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'])
        self.sampleframe['set'] = 2  # SET 2 -> BIG DATASET
        self.countryframe['set'] = 20  # SET 20-> PER COUNTRY TOP 50
        self.countryframe.rename(columns={'lenght': 'duration'}, inplace=True)
        self.countryframe['duration'] = self.countryframe['duration'].div(
            1000).round(2)

        # self.countryframe.info()
        self.fullframe = pd.concat([self.countryframe, self.sampleframe])

        # self.fullframe.info()

        self.kmeans = KMeans(n_clusters=2).fit(self.fullframe)
        self.fullframe['cluster'] = self.kmeans.labels_
        centroids = pd.DataFrame(self.kmeans.cluster_centers_)

        if self.debug is True:
            # DEBUGGING PRINTS
            print(f"LABELS: {self.kmeans.labels_}")
            print(self.fullframe)
            print('COUNT PER CLUSTER', self.fullframe.groupby('cluster').count())

        # FIND POPULAR CLUSTER

    def return_desc(self):
        self.desc = self.fullframe.groupby('cluster').describe()
        self.desc['country'] = self.countryname[11:-17]
        global descriptions
        descriptions = pd.concat([descriptions, self.desc])
        print('### DESCRIPTION PER CLUSTER ###')
        return descriptions

    def decide_popular_cluster(self):
        global popular_clusters
        
        cluster0 = 0
        cluster1 = 0
        for index, row in self.fullframe.iterrows():
            if row['cluster'] == 0 and row['set'] == 20:
                cluster0+=1
            if row['cluster'] == 1 and row['set'] == 20:
                cluster1+=1
            if cluster0 > cluster1:
                popular_clusters[self.countryname[11:-17]] = 0 #CLUSTER 0 ES EL POPULAR
            else:
                popular_clusters[self.countryname[11:-17]] = 1 #CLUSTER 1 ES EL POPULAR

        
        print(popular_clusters)

        return popular_clusters


def main(desc,pops):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            path = 'playlists/'+filename
            print(path)
            KMA = k_means_structure(datasetpath, path, filename)
            KMA.return_desc()
            KMA.decide_popular_cluster()
    # COMMENTED TO NOT STDOUT to EXCEL XML
    # descriptions.to_excel('countries.xlsx')
    
    #popular cluster -> dataframe -> excel
    pop_cluster = pd.DataFrame.from_dict(list(pops.items()))
    pop_cluster.to_excel('pop_clusters_per_country.xlsx')


main(descriptions,popular_clusters)

# %%
