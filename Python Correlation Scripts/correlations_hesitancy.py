import pandas as pd

df = pd.read_csv('/Users/jush/Desktop/vaccine_hesitancy_and_deaths.csv')
numeric_df = df[['avg_hesitant', 'avg_strongly_hesitant', 'percent_population_dead']]
print(numeric_df.corr())

# avg_hesitant vs avg_strongly_hesitant → 0.976

# Very strong positive correlation. States with higher general hesitancy also tend to have more strongly hesitant people.

# avg_hesitant or avg_strongly_hesitant vs percent_population_dead → -0.0647 / -0.0304

# Essentially no correlation. Vaccine hesitancy in a state doesn’t strongly line up with deaths per population in your dataset.