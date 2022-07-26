import pandas as pd
import numpy as np
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

# use histogram to identify outliers with numeric data
df_movie = df_netflix[df_netflix['type'] == 'Movie']
df_movie = df_movie.assign(minutes=df_movie['duration'].str.extract(
    '(\d+)', expand=False))

# drop all rows with any Null/NaN/NaT value
df_movie_clean = df_movie.dropna()
df_movie_clean_number = df_movie_clean['minutes'].astype(str).astype(int)

# create histogram
plt.hist(df_movie_clean_number)
plt.show()
