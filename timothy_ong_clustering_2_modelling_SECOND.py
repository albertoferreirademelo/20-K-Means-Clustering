from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from dateutil.relativedelta import relativedelta

agg_df3 = pd.read_csv("clean_df_TEST2.csv")
avg_risk_free_rate = [0.011, 0.017, 0.018, 0.013, 0.01]


def plot_cluster(df, max_loop=50):
    """
    Looking at the performance of various number of clusters using K-Means.
    Performance is evaluated by within cluster SSE and silhouette score.
    """
    try:
        df.drop('cluster', axis=1, inplace=True)
    except:
        next
    X = df.iloc[:, 1:]

    # robust scaling is used so that the centering and scaling statistics are therefore not influenced by a few number of very large marginal outliers as they are based on percentiles
    rb = RobustScaler()
    X_rb = rb.fit_transform(X)

    sse_within_cluster = {}
    silhouette_score = {}

    for k in range(2, max_loop):
        kmeans = KMeans(n_clusters=k, random_state=10, n_init=10, n_jobs=-1)
        kmeans.fit(X_rb)
        sse_within_cluster[k] = kmeans.inertia_
        silhouette_score[k] = metrics.silhouette_score(X_rb, kmeans.labels_, random_state=10)

    _ = plt.figure(figsize=(10, 6))
    ax1 = plt.subplot(211)
    _ = plt.plot(list(sse_within_cluster.keys()), list(sse_within_cluster.values()))
    _ = plt.xlabel("Number of Clusters")
    _ = plt.ylabel("SSE Within Cluster")
    _ = plt.title("Within Cluster SSE After K-Means Clustering")
    _ = plt.xticks([i for i in range(2, max_loop)], rotation=75)

    ax2 = plt.subplot(212)
    _ = plt.plot(list(silhouette_score.keys()), list(silhouette_score.values()))
    _ = plt.xlabel("Number of Clusters")
    _ = plt.ylabel("Silhouette Score")
    _ = plt.title("Silhouette Score After K-Means Clustering")
    _ = plt.xticks([i for i in range(2, max_loop)], rotation=75)

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
    plt.show()


def apply_cluster(df, clusters=2):
    """
    Applying K-Means with the optimal number of clusters identified
    """
    try:
        df.drop('cluster', axis=1, inplace=True)
    except:
        next
    X = df.iloc[:, 1:]
    rb = RobustScaler()
    X_rb = rb.fit_transform(X)
    kmeans = KMeans(n_clusters=clusters, random_state=10, n_init=10, n_jobs=-1)
    kmeans.fit(X_rb)
    score = metrics.silhouette_score(X_rb, kmeans.labels_, random_state=10)
    df['cluster'] = kmeans.labels_
    sse_within_cluster = kmeans.inertia_

    print("clustering performance")
    print("-----------------------------------")
    print("silhouette score: " + str(score.round(2)))
    print("sse withing cluster: " + str(sse_within_cluster.round()))

    return df


#plot_cluster(agg_df3, max_loop=25)


first_trial = apply_cluster(agg_df3, clusters=5)
#print (first_trial)
#first_trial = first_trial.groupby(["cluster"])
#first_trial = first_trial.agg(["mean", "mean", "count"])



cluster_perf_df = (
    first_trial
    .groupby('cluster')
    .agg({"avg_yearly_change" : "mean", "avg_yearly_variance" : "mean", "company" : "count"})
    .sort_values('avg_yearly_change')
    .reset_index()
)

#print (cluster_perf_df)


agg_df3_sub = agg_df3.query("cluster == 3").reset_index(drop=True)
#plot_cluster(agg_df3_sub, max_loop=20)
#plt.show()

#print (agg_df3_sub)

#print (agg_df3.query("cluster == 2").company.unique())

second_trial= apply_cluster(agg_df3_sub, clusters=4)


sub_cluster_perf_df = (
    second_trial
    .groupby('cluster')
    .agg({"avg_yearly_change" : "mean", "avg_yearly_variance" : "mean", "company" : "count"})
    .sort_values('avg_yearly_change')
    .reset_index()
)


#print (sub_cluster_perf_df)


agg_df3_sub_sub = agg_df3_sub.query("cluster == 1").reset_index(drop=True)

third_trial= apply_cluster(agg_df3_sub_sub, clusters=3)

#print (agg_df3_sub_sub)

#plot_cluster(agg_df3_sub_sub, max_loop=20)
#plt.show()


sub_sub_cluster_perf_df = (
    third_trial
    .groupby('cluster')
    .agg({"avg_yearly_change" : "mean", "avg_yearly_variance" : "mean", "company" : "count"})
    .sort_values('avg_yearly_change')
    .reset_index()
)

#print (sub_sub_cluster_perf_df)
#print (agg_df3_sub.query("cluster == 3").company.unique())
#print (agg_df3_sub.query("cluster == 0").company.unique())

#sub_sub_cluster = apply_cluster(agg_df3_sub, clusters=3)
#plot_cluster(agg_df3_sub, max_loop=25)

print (agg_df3_sub_sub.query("cluster == 1").company.unique())
