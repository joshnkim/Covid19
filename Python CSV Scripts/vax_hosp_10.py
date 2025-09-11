import pandas as pd


df = pd.read_csv('/Users/jush/Desktop/vax_hosp_10.csv')
numeric_df = df[['max_vax_rate', 'relative_hospitalizations']]



print(numeric_df.corr())
