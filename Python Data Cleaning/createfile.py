import csv 


output_file = '/Users/jush/Downloads/state_politics.csv'

desired_columns = ['State', 'Dem_or_rep']
state_colors = {
    "AL": "Red", "AK": "Red", "AZ": "Blue", "AR": "Red",
    "CA": "Blue", "CO": "Blue", "CT": "Blue", "DE": "Blue",
    "FL": "Red", "GA": "Blue", "HI": "Blue", "ID": "Red",
    "IL": "Blue", "IN": "Red", "IA": "Red", "KS": "Red",
    "KY": "Red", "LA": "Red", "ME": "Blue", "MD": "Blue",
    "MA": "Blue", "MI": "Blue", "MN": "Blue", "MS": "Red",
    "MO": "Red", "MT": "Red", "NE": "Red", "NV": "Blue",
    "NH": "Blue", "NJ": "Blue", "NM": "Blue", "NY": "Blue",
    "NC": "Red", "ND": "Red", "OH": "Red", "OK": "Red",
    "OR": "Blue", "PA": "Blue", "RI": "Blue", "SC": "Red",
    "SD": "Red", "TN": "Red", "TX": "Red", "UT": "Red",
    "VT": "Blue", "VA": "Blue", "WA": "Blue", "WV": "Red",
    "WI": "Blue", "WY": "Red"
}

with open(output_file, 'w', newline='', encoding='utf-8') as outfile: 
    writer = csv.DictWriter(outfile, fieldnames=desired_columns)
    writer.writeheader()
    for state, color in state_colors.items():
            writer.writerow({'State':state, 'Dem_or_rep':color})
        
print(f"Created CSV file {output_file}")

