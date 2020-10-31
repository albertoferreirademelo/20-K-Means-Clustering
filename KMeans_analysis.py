import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df = pd.read_excel("edited_raw1.xlsx", sheet_name="2015-2018")
df2 = df.set_index("Date")



#print (df.head())

#df2 = pd.DataFrame()

#df2["Date"] = df["Date"]
#df2["AAK"] = df["AAK"]

kmeans = KMeans(n_clusters=15).fit(df2)
centroids = kmeans.cluster_centers_
#print (centroids)
for company in df:
    df.plot.scatter("Date", company)
    #plt.scatter(df["Date"], df[company], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 1], c="red", s=50)
plt.show()

#df = df.set_index("Date")

#df_analysis = df["AAK"]

#print (df_analysis.head())


#for company in df:
    #print (company)

#df.plot.scatter("Date", "AAK")

#plt.show()