import csv
import pandas as pd

input_file = '/Users/jush/Downloads/populations.csv'
output_file = '/Users/jush/Downloads/populations_cleaned.csv'
df = pd.read_csv('/Users/jush/Downloads/populations.csv')

desired_columns = [
    'NAME',
    'POPESTIMATE2021',
    'DEATHS2021'
]

rows_to_skip = ['District of Columbia', 'United States', 
                'Northeast Region', 'Midwest Region', 
                'South Region', 'West Region', 'Puerto Rico']

with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=desired_columns)
    writer.writeheader()

    for row in reader:
        if row['NAME'].strip() in rows_to_skip:
            continue 

        new_row = {}
        for col in desired_columns:

            val = row[col]
            if val is None:
                new_row[col] = ''
        
            elif col in {
                'NAME',
                'POPESTIMATE2021',
                'DEATHS2021'
                }:
                cleaned_value = val.replace(',', '')

                
                state_to_code = {
                    "ALABAMA":"AL", "ALASKA":"AK", "ARIZONA":"AZ", "ARKANSAS":"AR", "CALIFORNIA":"CA",
                    "COLORADO":"CO", "CONNECTICUT":"CT", "DELAWARE":"DE", "FLORIDA":"FL", "GEORGIA":"GA",
                    "HAWAII":"HI", "IDAHO":"ID", "ILLINOIS":"IL", "INDIANA":"IN", "IOWA":"IA",
                    "KANSAS":"KS", "KENTUCKY":"KY", "LOUISIANA":"LA", "MAINE":"ME", "MARYLAND":"MD",
                    "MASSACHUSETTS":"MA", "MICHIGAN":"MI", "MINNESOTA":"MN", "MISSISSIPPI":"MS", "MISSOURI":"MO",
                    "MONTANA":"MT", "NEBRASKA":"NE", "NEVADA":"NV", "NEW HAMPSHIRE":"NH", "NEW JERSEY":"NJ",
                    "NEW MEXICO":"NM", "NEW YORK":"NY", "NORTH CAROLINA":"NC", "NORTH DAKOTA":"ND", "OHIO":"OH",
                    "OKLAHOMA":"OK", "OREGON":"OR", "PENNSYLVANIA":"PA", "RHODE ISLAND":"RI", "SOUTH CAROLINA":"SC",
                    "SOUTH DAKOTA":"SD", "TENNESSEE":"TN", "TEXAS":"TX", "UTAH":"UT", "VERMONT":"VT",
                    "VIRGINIA":"VA", "WASHINGTON":"WA", "WEST VIRGINIA":"WV", "WISCONSIN":"WI", "WYOMING":"WY"
                }

                if col == 'NAME':
                    cleaned_value = state_to_code.get(cleaned_value.upper(), cleaned_value)
                
                new_row[col] = cleaned_value



            else:
                new_row[col] = val.replace(',', '') if val else val
        writer.writerow(new_row)

print(f"Cleaned CSV saved to {output_file}")