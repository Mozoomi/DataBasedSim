import pandas as pd
import csv

df = pd.read_csv('data/age/nycAge.csv', index_col=0)

df = df[df.index != 'Total']

def calculatePercent(df):
   total_pop = df.sum()
   percentage_data = (df.div(total_pop)) * 100

   return percentage_data


percentage_data = calculatePercent(df)

average_percentage = percentage_data.mean(axis=1)
average_percentage = average_percentage.rename('percent')

result_df = pd.DataFrame(average_percentage)

result_df.to_csv('data/age/nycAgeData.csv')