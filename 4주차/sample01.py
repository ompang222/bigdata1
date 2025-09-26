import pandas as pd

covid_file_path = './data/owid-covid-data.csv'
#covid_file_path = './data/data_bar.csv'
df = pd.read_csv(covid_file_path, sep=',', encoding='euc_kr')
#print(df)
#print(type(df))
#print(id(df))

print('-'*50)
print(df.info())

print('-'*50)
print(df.head())