import pandas as pd

edit_excel_file = "Edit1_stocks_and_prices.xlsx"
raw_excel_file = "RAW_stocks_and_prices.xlsx"

edit_file = pd.read_excel(edit_excel_file)
raw_file = pd.read_excel(raw_excel_file)

raw_file["Date"] = pd.to_datetime(raw_file["Date"]).dt.date
#print (raw_file.head())
#raw_columns = list(raw_file.columns)
#print (raw_file.keys())

#value_to_check = pd.Timestamp()

'''This part is to make a list with all the companies from the raw_file'''
Companies = []
edited_companies = []

for index, row in raw_file.iterrows():
    if row["Source.Name"] not in Companies:
        Companies.append(row["Source.Name"])
for i in Companies:
    edit_file[i]
#    edited_companies.append(i[:-7])

#print (edited_companies)
print (edit_file.head())


'''This part is to try to filter only companies with the data 2015-01-01'''
#print (raw_file.loc["Date"] == ["2015-01-01"])
#print (test)

'''This part is to check all companies that does not have values from 2015'''
#for index, row in raw_file.iterrows():
    #print (row["Date"])
    #if row[raw_columns[1]] == raw_columns.loc["2020-04-24"]:
        #print (raw_columns[0])
    #if row["Date"] == "2015-01-01 00:00:00":
        #print (row["Source.Name"])

#for i in Companies:
    #edit_file[]
#print (Companies)