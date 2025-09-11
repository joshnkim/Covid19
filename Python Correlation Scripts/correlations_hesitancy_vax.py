import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/hesitancy_vs_vaccinations.csv')
df['party_numeric'] = df['Dem_or_rep'].str.strip().map({'Blue': 0, 'Red': 1})
numeric_df = df[['party_numeric', 'avg_hesitant', 'avg_strongly_hesitant', 'avg_dose1_received']]
print(numeric_df.corr())



# party_numeric vs avg_hesitant / avg_strongly_hesitant (~0.66–0.68) → Republican-leaning states (1) tend to have higher vaccine hesitancy.

# party_numeric vs avg_dose1_received (-0.62) → Republican-leaning states tend to have lower vaccination rates.

# avg_hesitant vs avg_dose1_received (-0.64) → Higher hesitancy is associated with lower vaccination coverage.

# avg_hesitant vs avg_strongly_hesitant (0.97) → Strong hesitancy is strongly correlated with general hesitancy, as expected.