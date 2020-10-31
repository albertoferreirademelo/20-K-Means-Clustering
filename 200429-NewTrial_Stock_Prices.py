import pandas as pd
import glob, os


def list_of_name_of_files(path, type):
    all_files = glob.glob(path+"\\*."+type)
    return (all_files)

all_files = list_of_name_of_files("G:\Programming\Projects\MasterThesis\Stockprices", "csv")

edited_pd = pd.DataFrame()
last_df = pd.DataFrame()


#Loop for each file
for file in all_files:
    raw_file = pd.read_csv(file)
    #print (raw_file.head(1))
    if raw_file["Date"].iloc[0] == "2015-01-01":
        Symbol = file[49:-7] #Symbols of each company
        number_date = len(raw_file["Date"])
        if number_date != 279: #We remove the company VRG-B in this case since I got a lot of bug from this one
            #print (raw_file)
            #print ("%s have %d dates." % (Symbol, number_date))
            print ("PASS")
            #print (raw_file.head())
        else:
            raw_file.rename(columns={"Adj Close" : Symbol}, inplace = True)
            #print (raw_file["Date"])
            #edited_pd = raw_file.filter()
            #edited_pd.join(raw_file[Symbol])
            #print (Symbol)
            edited_pd = pd.concat([edited_pd, raw_file[Symbol]], axis=1, sort=False)
            last_df = raw_file
            #edited_pd.set_index(raw_file["Date"])

print (edited_pd.head())
print (edited_pd.info())
print ("------------------")
last_df["Date"] = pd.to_datetime(last_df["Date"]).dt.date
edited_pd = edited_pd.set_index(last_df["Date"])
print (edited_pd.head())
print (edited_pd.info())
print ("------------------")

edited_pd.to_csv("edited_file.csv")

