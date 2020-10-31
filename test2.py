import pandas as pd
import yfinance as yf
import yahoofinancials
import numpy as np

'''working program

#companies = ["AGRO", "AOI", "ARISE", "BACTI-B", "BINV", "CORE-A", "ENQ", "EPIS-B", "ETX", "HNSA", "HTRO", "IMMU", "IS", "ITAB-B", "JOSE", "KARO", "KDEV", "MOB", "MULQ", "OASM", "OP", "OPUS", "ORX", "PLED", "QLRO", "RATO-A", "SANION", "SENS", "SMF", "SSAB-A", "SSAB-B", "VRG-B"]


#companies = ["AGRO"]

companies = ['BIOT','CEVI','CORE-A','CTT','HMS','MYCR','PROF-B','SAGA-A','SAGA-B','VITR','XANO-B','XVIVO']
#years = ["2015", "2016", "2017", "2018", "2019"]

clean_df = pd.DataFrame(columns=["company", "1 Jan 2019", "31 Dec 2019", "perc change"])


for company in companies:
    stock = yf.download(("%s.ST" % company), start="2019-01-01", end="2019-12-31", progress=False)
    #print (company)
    #print (stock.head())
    January = stock["Adj Close"].iloc[0]
    #print (stock.tail())
    #print(stock["Adj Close"].iloc[-1])
    December = stock["Adj Close"].iloc[-1]
    avg_change = (December-January)/January
    #avg_change = stock.loc[:,"Adj Close"].var()
    clean_df.loc[len(clean_df)] = ["%s" % company, January, December, avg_change]

#clean_df.to_csv("result_second_analysis_2019.csv", index=False)

#print (clean_df.head())

'''

#Testing statistics

#companies = ['BIOT','CEVI','CORE-A','CTT','HMS','MYCR','PROF-B','SAGA-A','SAGA-B','VITR','XANO-B','XVIVO']
#companies = ["BIOT"]
companies = ["OMX"]
years = ["2015", "2016", "2017", "2018", "2019"]
#years = ["2015"]

clean_df = pd.DataFrame(columns=["year", "company", "perc change"])


for year in years:
    perc_change = 0
    start_date = ("%s-01-01" % year)
    end_date = ("%s-12-31" % year)
    #print (start_date)
    #print (year)
    for company in companies:
        #stock = yf.download(("%s.ST" % company), start_date, end_date, progress=False)
        stock = yf.download(("^OMX"), start_date, end_date, progress=False)
        #print (company)
        #print (stock.head())
        #print(stock.tail())
        January = stock["Adj Close"].iloc[0]
        #print (January)
        #print(stock["Adj Close"].iloc[-1])
        December = stock["Adj Close"].iloc[-1]
        #print (December)
        temp_perc_change = perc_change+((December-January)/January)
        #print (temp_perc_change)
        #perc_change = perc_change+temp_perc_change
        #print (perc_change)
        #avg_change = stock.loc[:,"Adj Close"].var()
        clean_df.loc[len(clean_df)] = ["%s" % year, "%s" % company, "%s" % temp_perc_change]


    '''
    perc_change = perc_change/(len(companies))
    print (perc_change)
    clean_df.loc[len(clean_df)] = ["%s" % year, "%s" % perc_change]
    '''

#clean_df.to_csv("test_yearly_change.csv", index=False)

print (clean_df.head())