import pandas as pd
import yfinance as yf
import yahoofinancials
import numpy as np


companies = pd.read_csv("companies_ticks.csv")

#companies = ["AAK", "ABB"]
#companies = ["AAK"]
#training_years = ["2015"]
training_years = ["2015", "2016", "2017", "2018"]

clean_df = pd.DataFrame(columns=["company", "avg_yearly_change", "avg_yearly_variance"])

number = 1

#iterate each company
for tick in companies:
    total_companies = len(companies)
    print ("%d." % number)
    number += 1

    #easier to understand variables
    sum_yearly_change = 0 #here is the sum of all years change in percent
    sum_variance = 0 #this is the sum of the variance of all years

    #for each year
    for year in training_years:
        sum_prct_change = 0
        list_of_avg_change = []

        #download the stock of the given year
        stock = yf.download(("%s.ST" % tick), start="%s-01-01" % year, end="%s-12-31" % year, progress=False)

        try:
            sum_yearly_change += ((stock["Adj Close"].iloc[-1])-(stock["Adj Close"].iloc[0]))/(stock["Adj Close"].iloc[-1])

            #print (stock.describe())

            #for each row
            for index, row in stock.iterrows():
                prct_change = ((row["Open"]-row["Close"])/row["Open"]) #calculation of the percentage change
                list_of_avg_change.append(prct_change) #add to the list of average change
                #sum_prct_change = sum_prct_change+prct_change #sum all the percentage change

            #try:
                #avg_change = sum_prct_change/len(stock.index) #this will calculate the average change for all the year
            #except ZeroDivisionError:
                #print (tick)
                #avg_change = 0
            #sum_yearly_change += avg_change #this will sum the average change on the variable sum_yearly_change
            yearly_variance = np.var(list_of_avg_change) #this will give a result of the variance of the average change
            sum_variance +=yearly_variance #this will sum the variance of each year to the variable sum_variance

            #print (sum_yearly_change)

        except:
            print ("%s did not work." % tick)

    avg_yearly_change = sum_yearly_change/len(training_years)
    avg_yearly_variance = sum_variance/len(training_years)
    clean_df.loc[len(clean_df)] = ["%s" % tick, "%f" % avg_yearly_change, "%f" % avg_yearly_variance]
    #print (tick)
    #print (avg_yearly_change)
    #print (avg_yearly_variance)
print (clean_df)
clean_df.to_csv("clean_df_TEST2.csv", index=False)

            #print (row["Open"], row["Close"])
        #print (stock.head())
    #test = pd.concat([test, stock["Open"]], axis=1, sort=False)
    #edited_pd = pd.concat([edited_pd, raw_file[Symbol]], axis=1, sort=False)
    #print (stock.head())

#print (test.head())


'''
#Ticker = [AAK, ABB, ACTI, ADDT-B, AF-B, AGRO, ALFA, ALIV-SDB, AM1S, ANOD-B, ANOT, AOI, AQ, ARISE, ARP, ASSA-B, ATCO-A, ATCO-B, ATRE, ATRLJ-B, AXFO, AZA, AZN, BACTI-B, BALD-B, BEGR, BEIA-B, BEIJ-B, BELE, BERG-B, BESQ, BETS-B, BILI-A, BILL, BINV, BIOG-B, BIOT, BMAX, BOL, BONG, BORG, BOUL, BRG-B, BTS-B, BUFAB, BULTEN, BURE, CAST, CAT-A, CAT-B, CATE, CBTT-B, CCC, CCOR-B, CEVI, CLA-B, CLAS-B, COIC, CONS-B, CORE-A, CORE-PREF, CRAD-B, CRED-A, CTT, DEDI, DIOS, DORO, DUNI, DURC-B, EAST, EKTA-B, ELAN-B, ELEC, ELOS-B, ELUX-A, ELUX-B, EMPIR-B, ENDO, ENEA, ENQ, ENRO-PREF, ENRO, EOLU-B, EPIS-B, ERIC-A, ERIC-B, ETX, EWRK, FABG, FAG, FEEL, FING-B, FOI-B, FPAR-A, FPAR-PREF, FPIP, G5EN, GETI-B, GHP, GIGSEK, GRNG, GUNN, HANZA, HAV-B, HEBA-B, HEXA-B, HIQ, HLDX, HM-B, HMS, HNSA, HOLM-A, HOLM-B, HPOL-B, HTRO, HUFV-A, HUSQ-A, HUSQ-B, IAR-B, ICA, ICTA, IMMU, INDT, INDU-A, INDU-C, INTRUM, INVE-A, INVE-B, INWI, IS, ITAB-B, IVSO, JM, JOSE, KABE-B, KARO, KDEV, KIND-SDB, KINV-A, KINV-B, KLED, KLOV-A, KLOV-B, KLOV-PREF, KNOW, LAGR-B, LAMM-B, LATO-B, LIAB, LIFCO-B, LOOM-B, LUC, LUG, LUND-B, MCAP, MEAB-B, MEKO, MIDW-A, MIDW-B, MOB, MOMENT, MSAB-B, MSON-A, MSON-B, MTG-A, MTG-B, MULQ, MVIR-B, MYCR, NAXS, NCC-A, NCC-B, NDA-SE, NET-B, NETI-B, NEWA-B, NGS, NIBE-B, NMAN, NOBI, NOLA-B, NOTE, NP3, NTEK-B, NVP, OASM, ODD, OEM-B, OP-PREF, OP, OPUS, ORES, ORTI-A, ORTI-B, ORX, PACT, PEAB-B, PLAZ-B, PLED, POOL-B, PREC, PREV-B, PRIC-B, PROB, PROF-B, QLRO, RAIL, RATO-A, RATO-B, RAY-B, RECI-B, REJL-B, RNBS, RROS, SAAB-B, SAGA-A, SAGA-B, SAGA-PREF, SAND, SANION, SAS, SBB-B, SCA-A, SCA-B, SCST, SEB-A, SEB-C, SECT-B, SECU-B, SEMC, SENS, SHB-A, SHB-B, SINT, SKA-B, SKF-A, SKF-B, SKIS-B, SMF, SOBI, SOF-B, SPOR, SSAB-A, SSAB-B, STAR-B, STE-A, STE-R, STEF-B, STRAX, STWK, SVED-B, SVIK, SVOL-A, SVOL-B, SWEC-A, SWEC-B, SWED-A, SWMA, SYSR, TEL2-A, TEL2-B, TELIA, TETY, THULE, TIETOS, TIGO-SDB, TRAC-B, TRAD, TREL-B, TRENT, VIT-B, VITR, VOLV-A, VOLV-B, VRG-B, VSSAB-B, WALL-B, WIHL, WISE, XANO-B, XVIVO, ZETA]

#tsla_df = yf.download('AAK.ST', start='2015-01-01', end='2019-12-31', progress=False)

#print (tsla_df.head())
#print (tsla_df.tail())
#print (tsla_df.info())


first_date_2018_df = (tsla_df.query("Date == '2018-01-03'")[['ticker', 'Date', 'Open']]
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .rename(columns={"Open": "open_first_day"})
    .reset_index(drop=True)
    [['ticker', 'year', 'open_first_day']]
    .pivot_table(values='open_first_day', columns='year', index='ticker', aggfunc='sum')
    .rename_axis(None, axis=1)
    .reset_index()
)

print (df_2015_2019)

#df_2015_2019 = (tsla_df.pipe (lambda x: x.assign(yeah=pd.to_datetime(x.date).dt.year)).query("year >= 2015")[["Date", "year", "Open", "Close"]])

'''