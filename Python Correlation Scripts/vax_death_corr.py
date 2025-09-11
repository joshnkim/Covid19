import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/vax_vs_death2.csv')
numeric_df = df[['vax_rate_at_cutoff', 'percent_population_dead_after_cutoff']]

correlation = numeric_df.corr() 

correlation_long = correlation.stack().reset_index()
correlation_long.columns = ['variable_x', 'variable_y', 'correlation']

correlation_long.to_csv('/Users/jush/Desktop/vax_death_corr.csv', index=False)



