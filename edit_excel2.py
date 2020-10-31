import pandas as pd

raw_excel_file = "RAW_stocks_and_prices.xlsx"

raw_file = pd.read_excel(raw_excel_file)


#raw_file["Date"] = pd.to_datetime(raw_file["Date"]).dt.date

#raw_file.set_index(["Source.Name"])

#raw_file.set_index('Date', inplace=True)

print (raw_file.head())