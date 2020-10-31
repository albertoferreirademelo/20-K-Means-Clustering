import pandas as pd
import yfinance as yf
import yahoofinancials
import numpy as np
import matplotlib.pyplot as plt


agg_df3 = pd.read_csv("clean_df_TEST2.csv")

print (agg_df3.head())

ax = agg_df3.set_index('avg_yearly_change')['avg_yearly_variance'].plot(style='o')

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))

label_point(agg_df3.avg_yearly_change, agg_df3.avg_yearly_variance, agg_df3.company, ax)

ax.set_xlabel("Average yearly change")
ax.set_ylabel("Average yearly variation")

#draw()

#agg_df3.plot(kind="scatter", x="avg_yearly_change", y="avg_yearly_variance", figsize = (9,5))

#plt.annotate(label)

plt.show()

'''This was to take a picture for the normalization example

stock = yf.download(("AAK.ST"), start="2015-01-01", end="2015-12-31", progress=False)

#training_years = ["2015", "2016", "2017", "2018", "2019"]

#for year in training_years:
    #stock = yf.download(("AAK.ST"), start="%s-01-01" % year, end="%s-12-31" % year, progress=False)
    #print(stock.info())254

#print (stock.head())

#for tick in companies:

    #easier to understand variables
    #sum_yearly_change = 0 #here is the sum of all years change in percent
    #sum_variance = 0 #this is the sum of the variance of all years

    #for each year
    #for year in training_years:
        #sum_prct_change = 0
list_of_avg_change = []

for index, row in stock.iterrows():
    prct_change = ((row["Open"] - row["Close"]) / row["Open"])  # calculation of the percentage change
    list_of_avg_change.append(prct_change)  # add to the list of average change
    #sum_prct_change = sum_prct_change + prct_change  # sum all the percentage change

print (len(list_of_avg_change))
print (stock.info())

#m = np.asarray(list_of_avg_change)
stock["avg_change"] = np.array(list_of_avg_change)

#stock.reset_index(drop=True)

#print (stock.head())

stock2 = stock["avg_change"]

ax = plt.gca()

stock2.plot(y="avg_change")

plt.show()

'''