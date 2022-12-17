from main import *
import sklearn.cluster as cluster
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import davies_bouldin_score, silhouette_score



# K-Means Clustering

new_rfm1 = rfm_table1.drop('CustomerID', axis=1)

df_rfm_log = new_rfm1.copy()

scaler = StandardScaler()
scaler.fit(df_rfm_log)
RFM_scaled1 = scaler.transform(df_rfm_log)
RFM_scaled1 = pd.DataFrame(RFM_scaled1, columns=df_rfm_log.columns)

# To find optimal number of clusters
X = np.asarray(RFM_scaled1)

from scipy.spatial.distance import cdist
distortions = [] 
inertias = [] 
mapping1 = {} 
mapping2 = {} 
K = range(1,10) 
for k in K: 
    #Building and fitting the model 
    kmeanModel = KMeans(n_clusters=k).fit(RFM_scaled1) 
    kmeanModel.fit(RFM_scaled1)     
    distortions.append(sum(np.min(cdist(RFM_scaled1, kmeanModel.cluster_centers_, 
                      'euclidean'),axis=1)) / RFM_scaled1.shape[0]) 
    inertias.append(kmeanModel.inertia_) 

    mapping1[k] = sum(np.min(cdist(RFM_scaled1, kmeanModel.cluster_centers_, 
                 'euclidean'),axis=1)) / RFM_scaled1.shape[0] 
    mapping2[k] = kmeanModel.inertia_

def kmeans(normalised_df_rfm, clusters_number, original_df_rfm):
    kmeans = KMeans(n_clusters = clusters_number, random_state = 1)
    kmeans.fit(normalised_df_rfm)
    # Extract cluster labels
    cluster_labels = kmeans.labels_
    # Create a cluster label column in original dataset
    df_new = original_df_rfm.assign(Cluster = cluster_labels)
    # Initialise TSNE
    model = TSNE(random_state=1)
    transformed = model.fit_transform(df_new)
    # Plot t-SNE
    plt.title('Flattened Graph of {} Clusters'.format(clusters_number))
    sns.scatterplot(x=transformed[:,0], y=transformed[:,1], hue=cluster_labels, style=cluster_labels, palette="Set1")
    return df_new

# Model Evaluation

# Davies Boulding score
def optimal_cluster(n):
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(X)
    print(f"Number of cluster {n}, Davies Boulding Score {davies_bouldin_score(X, kmeans.labels_)}")

optimal_cluster(3)
optimal_cluster(4)
optimal_cluster(5)
optimal_cluster(6)

# we will pick the cluster with lowest davies boulding score
print('\n')
# Silhouetter Score
def optimal_sil_Score(n):
    km = KMeans(n_clusters=n)
# Fit the KMeans model
    km.fit_predict(X)
# Calculate Silhoutte Score
    score = silhouette_score(X, km.labels_, metric='euclidean')
    print('Silhouetter Score: %.3f' % score)

optimal_sil_Score(3)
optimal_sil_Score(4)
optimal_sil_Score(5)
optimal_sil_Score(6)