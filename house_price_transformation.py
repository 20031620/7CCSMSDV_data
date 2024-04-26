import pandas as pd

df = pd.read_excel('data/hpimonthlyandqtlytables1to19.xls', sheet_name='Table 11', header=None)

# Define the region names as per the GeoJSON labels
regions = ['North East', 'North West', 'Yorkshire and The Humber', 'East Midlands', 'West Midlands',
           'Eastern', 'London', 'South East', 'South West', 'Wales', 'Scotland']

transformed_data = []

for region in regions:
    print(f"Region: {region}")
    # Iterate over each year from 1993 to 2023
    start_row = 536 + regions.index(region) * 131 # 131 lines between each of the regional data tables
    for year in range(1993, 2024):
        year_start_row = start_row + (year - 1993)*4
        print(f"Year: {year}, Start Row: {year_start_row}")

        # Extract the average house prices for the year from Q1 - Q4
        total_house_price = 0
        for i in range(4):
            total_house_price += df.iloc[year_start_row + (i - 1), 8]
        avg_house_price = total_house_price / 4
        print(f"Avg. house price: {avg_house_price}")

        transformed_data.append({'region': region,
                                 'year': year,
                                 'avg. house price': avg_house_price})

    # Skip 7 rows between different regions as per dataset structure 
    for _ in range(7):
        start_row += 1

transformed_df = pd.DataFrame(transformed_data)

transformed_df.to_csv('transformed_data.csv', index=False)
