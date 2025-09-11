import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/vax_vs_hospitalizations.csv')
numeric_df = df[['max_vax_rate', 'relative_hospitalizations']]
print(numeric_df.corr())


#more vaccinations, less hospitalizations.