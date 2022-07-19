import pandas as pd
import matplotlib.pyplot as plt

# dataset overview
df_netflix = pd.read_csv('netflix_titles.csv')
# print(df_netflix.dtypes)
# print(df_netflix.shape)

# identify missing data
print(df_netflix.isnull().sum())

# % of rows missing in each column
for column in df_netflix.columns:
    percentage = df_netflix[column].isnull().mean()
    print(f'{column}: {round(percentage*100, 2)}%')

# use histograms to identify outliers with numeric data
df_movie = df_netflix[df_netflix['type'] == 'Movie']
df_movie = df_movie.assign(minute=df_movie['duration'].str.extract(
    '(\d+)', expand=False))
