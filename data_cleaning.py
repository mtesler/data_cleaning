import pandas as pd

# dataset overview
df_netflix = pd.read_csv('netflix_titles.csv')
print(df_netflix.dtypes)
print(df_netflix.shape)

# identify missing data

print(df_netflix.isnull().sum())
