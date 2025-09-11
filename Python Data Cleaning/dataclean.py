import csv

input_file = '/Users/jush/Downloads/COVID-19_Vaccinations_in_the_United_States,Jurisdiction_20250828(in).csv'
output_file = '/Users/jush/Downloads/vax_data_cleaned.csv'


desired_columns = [
    'Date',
    'MMWR_week',
    'Location',
    'Administered_Dose1_Recip',
    'Administered_Dose1_Pop_Pct',
    'Series_Complete_Yes',
    'Series_Complete_Pop_Pct',
    'Additional_Doses',
    'Additional_Doses_Vax_Pct'
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
            elif col in {'Administered_Dose1_Pop_Pct', 'Series_Complete_Pop_Pct', 'Additional_Doses_Vax_Pct'}:
                new_row[col] = val.replace(',', '') 
            else:
                new_row[col] = val.replace(',', '') if val else val
        writer.writerow(new_row)

print(f"Cleaned CSV saved to {output_file}")