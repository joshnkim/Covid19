import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/icu.csv')
numeric_df = df[['max_vax_rate', 'covid_hospitalizations']]

correlation = numeric_df.corr() 

correlation_long = correlation.stack().reset_index()
correlation_long.columns = ['variable_x', 'variable_y', 'correlation']

correlation_long.to_csv('/Users/jush/Desktop/hospitalizations_correlations.csv', index=False)
  




