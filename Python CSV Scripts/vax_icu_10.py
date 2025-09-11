import pandas as pd


df = pd.read_csv('/Users/jush/Desktop/vax_icu_10.csv')
numeric_df = df[['max_vax_rate', 'relative_icu_utilization']]



print(numeric_df.corr())
