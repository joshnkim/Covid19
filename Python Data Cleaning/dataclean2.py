import csv
import pandas as pd

input_file = '/Users/jush/Downloads/Vaccine_Hesitancy_for_COVID-19__County_and_local_estimates_20250903.csv'
output_file = '/Users/jush/Downloads/antivax_cleaned.csv'
df = pd.read_csv('/Users/jush/Downloads/Vaccine_Hesitancy_for_COVID-19__County_and_local_estimates_20250903.csv')

desired_columns = [
    'County Name',
    'State',
    'Estimated hesitant',
    'Estimated hesitant or unsure',
    'Estimated strongly hesitant',
    'Percent adults fully vaccinated against COVID-19 (as of 6/10/21)'
]

with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=desired_columns)
    writer.writeheader()

    for row in reader:
        new_row = {}
        for col in desired_columns:

            val = row[col]
            if val is None:
                new_row[col] = ''

            elif col in {
                'County Name',
                'State',
                'Estimated hesitant',
                'Estimated hesitant or unsure',
                'Estimated strongly hesitant',
                'Percent adults fully vaccinated against COVID-19 (as of 6/10/21)'
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

                if col == 'State':
                    cleaned_value = state_to_code.get(cleaned_value, cleaned_value)
                
                
                if cleaned_value.endswith('%'):
                    try:
                        cleaned_value = str(float(cleaned_value.strip('%')))
                    except ValueError:
                        pass
                new_row[col] = cleaned_value



            else:
                new_row[col] = val.replace(',', '') if val else val
        writer.writerow(new_row)

print(f"Cleaned CSV saved to {output_file}")