import pandas as pd


df = pd.read_csv('/Users/jush/Desktop/weekly_vax_vs_deaths.csv')
numeric_df = df[['vax_rate', 'percent_population_dead_week']]



print(numeric_df.corr())