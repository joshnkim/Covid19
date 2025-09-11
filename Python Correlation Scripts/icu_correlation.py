import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/icu.csv')
numeric_df = df[['max_vax_rate', 'icu_utilization']]

correlation = numeric_df.corr() 

correlation_long = correlation.stack().reset_index()
correlation_long.columns = ['variable_x', 'variable_y', 'correlation']

correlation_long.to_csv('/Users/jush/Desktop/icu.csv', index=False)
  




