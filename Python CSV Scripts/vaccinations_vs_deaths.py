import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/vaccinations_vs_deaths.csv')
numeric_df = df[['max_vax_rate', 'percent_population_dead_post_vax']]
print(numeric_df.corr())
