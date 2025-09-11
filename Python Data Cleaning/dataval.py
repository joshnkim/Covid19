import csv

file = '/Users/jush/Downloads/vax_data_cleaned.csv'

with open(file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, 1):
        if len(row) == 9:
            print(f"Row {i} has {len(row)} columns")


