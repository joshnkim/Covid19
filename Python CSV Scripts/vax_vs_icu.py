import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/vax_vs_icu.csv')
numeric_df = df[['max_vax_rate', 'relative_icu_utilization']]
print(numeric_df.corr())


#more vaccinations, less ICU, not as much as with vax vs hospitalizations though.