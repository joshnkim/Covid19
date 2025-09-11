import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/hesitancy_vs_death.csv')
numeric_df = df[['avg_hesitant', 'percent_population_dead_post_vax']]
print(numeric_df.corr())
