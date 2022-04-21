# %%
import pandas as pd
from sklearn.cluster import KMeans
import os
import seaborn as sns
import cufflinks as cf
import matplotlib.pyplot as plt
plt.show()
#%matplotlib inline

datasetpath = 'tf_mini.csv'
directory = os.fsencode('playlists')
global descriptions
descriptions = pd.DataFrame()
global popular_clusters
popular_clusters = {}

cf.go_offline()
cf.set_config_file(world_readable=True,theme='pearl')

# %%


class k_means_structure:
    def __init__(self, setpath, countrypath, countryname):
        """[CONSTRUCTOR of KMA ]

        Args:
            setpath ([string]): [dataset relative path]
            countrypath ([string]): [relative path of country data json]
            countryname ([string]): [name of country less the jargon of filename]
        """
        self.debug = False
        self.sampleframe = pd.DataFrame(pd.read_csv(setpath), columns=[
                                        'energy', 'valence', 'tempo', 'duration', 'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'])  # removed 'us_popularity_estimate', and 'release year'
        self.countryname = countryname
        self.countryframe = pd.DataFrame(pd.read_json(countrypath), columns=[
                                         'energy', 'valence', 'tempo', 'lenght', 'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'])
        self.sampleframe['set'] = 2  # SET 2 -> BIG DATASET
        self.countryframe['set'] = 20  # SET 20-> PER COUNTRY TOP 50
        self.countryframe.rename(columns={'lenght': 'duration'}, inplace=True)
        self.countryframe['duration'] = self.countryframe['duration'].div(
            1000).round(2)

        self.fullframe = pd.concat([self.countryframe, self.sampleframe])

        self.kmeans = KMeans(n_clusters=2).fit(self.fullframe)
        self.fullframe['cluster'] = self.kmeans.labels_
        centroids = pd.DataFrame(self.kmeans.cluster_centers_)
        print(centroids)
        #PLOTTING
        self.fullframe.sample(n=50).iplot(kind='scatter3d', x='energy', y='valence', z='tempo', width=0.5,margin=(0,0,0,0),opacity=1,size=15)
        #sns.pairplot(self.fullframe.sample(n=50), hue="cluster")
        
        
        if self.debug is True:
            # DEBUGGING PRINTS
            print(f"LABELS: {self.kmeans.labels_}")
            print(self.fullframe)
            print('COUNT PER CLUSTER', self.fullframe.groupby('cluster').count())

    def return_desc(self):
        """[returns local copy of global variable country descriptions]

        Returns:
            [dict]: [statistical descriptions of every KMA per country]
        """
        self.desc = self.fullframe.groupby('cluster').describe()
        self.desc['country'] = self.countryname[11:-17]
        global descriptions
        descriptions = pd.concat([descriptions, self.desc])
        print('### DESCRIPTION PER CLUSTER ###')
        return descriptions

    def decide_popular_cluster(self):
        """[FIND THE MORE POPULAR CLUSTER PER COUNTRY]

        Returns:
            [dict]: [{country:popular_cluster}]
        """
        global popular_clusters

        cluster0 = 0
        cluster1 = 0
        for index, row in self.fullframe.iterrows():
            if row['cluster'] == 0 and row['set'] == 20:
                cluster0 += 1
            if row['cluster'] == 1 and row['set'] == 20:
                cluster1 += 1
            if cluster0 > cluster1:
                # CLUSTER 0 ES EL POPULAR
                popular_clusters[self.countryname[11:-17]] = 0
            else:
                # CLUSTER 1 ES EL POPULAR
                popular_clusters[self.countryname[11:-17]] = 1

        print(popular_clusters)

        return popular_clusters


def main(pops):

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            path = 'playlists/'+filename
            print(path)
            KMA = k_means_structure(datasetpath, path, filename)
            KMA.return_desc()
            KMA.decide_popular_cluster()
            #df = pd.read_excel('countries_massive.xlsx')
    # COMMENTED TO NOT STDOUT to EXCEL XML
    descriptions.to_excel('countries_massive.xlsx')
    # popular cluster -> dataframe -> excel
    pop_cluster = pd.DataFrame.from_dict(list(pops.items()))
    pop_cluster.to_excel('pop_clusters_per_country_massive.xlsx')

#%%

main(popular_clusters)

# %%
