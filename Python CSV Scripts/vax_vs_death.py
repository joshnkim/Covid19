import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/vax_vs_death2.csv')
numeric_df = df[['vax_rate_at_cutoff', 'percent_population_dead_after_cutoff']]
print(numeric_df.corr())


# cutoff date at 6/30/21.

# The correlation of -0.097882 means there’s a slight negative correlation,
#  i.e., higher vaccination rates before the cutoff are weakly associated with fewer subsequent deaths.f