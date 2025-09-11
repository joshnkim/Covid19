import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/hesitancy_vs_death.csv')
numeric_df = df[['avg_hesitant', 'percent_population_dead_post_vax']]

correlation = numeric_df.corr() 

correlation_long = correlation.stack().reset_index()
correlation_long.columns = ['variable_x', 'variable_y', 'correlation']

correlation_long.to_csv('/Users/jush/Desktop/hesitancy_death_corr.csv', index=False)





