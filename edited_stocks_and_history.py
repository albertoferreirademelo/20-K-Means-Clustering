import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

''' This is only to plot the original file, before been normalized
df = pd.read_csv("edited_file2.csv")
df = df.set_index("Date")

AAK = df["AAK"]

AAK.plot(label="AAK")
plt.legend(loc="upper left")
plt.show()

'''



df = pd.read_excel("edited_raw1.xlsx", sheet_name="2015-2018")

df.plot.scatter("Date", "AAK")

plt.show()

#print (df.head())

#select_data = df.loc[df["Date"] == "2015-01-08"]
#transposed_data = transposed_data.set_index("Date")

#print (select_data.head())

#select_data.set_index("Date", inplace=True)

#transposed_data = select_data.T

#print (transposed_data.head())


#transposed_data.plot.scatter(x="a", y="b")
#plt.show()


'''
#df = df.set_index("Date")

#for company in df:
    #print (company)
    #print (df[company].describe())
    #print ("-------------------------------------------------")
    #print (company.describe())

AAK = df["AAK"]
print (df.info())

AAK.plot(label="AAK")
plt.legend(loc="upper left")
plt.show()

#A = AAK.describe()

#for i in A:
    #print (i)


#df.plot(y="AAK")

#plt.show()

'''