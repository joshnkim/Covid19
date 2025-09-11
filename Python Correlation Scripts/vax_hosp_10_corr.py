import pandas as pd


df = pd.read_csv('/Users/jush/Desktop/vax_hosp_10.csv')
numeric_df = df[['max_vax_rate', 'relative_hospitalizations']]
correlation = numeric_df.corr() 

correlation_long = correlation.stack().reset_index()
correlation_long.columns = ['variable_x', 'variable_y', 'correlation']

correlation_long.to_csv('/Users/jush/Desktop/vax_hosp_10_corr.csv', index=False)