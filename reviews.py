import pandas as pd

# Read the CSV file
file_path = 'CLCK-Data-Aug2023/wine-reviews-exercise-gainfal/data/winemag-data-130k-v2.csv.zip'
df = pd.read_csv(file_path, compression='zip')

# Group data by country and calculate count and mean
summary_data = df.groupby('country').agg({'points': ['count', 'mean']}).reset_index()

# Rename columns for better clarity
summary_data.columns = ['country', 'count', 'points']

# Sort the data by count in descending order
summary_data = summary_data.sort_values(by='count', ascending=False)

# Write the summary data to a new CSV file
output_file_path = 'data/reviews-per-country.csv'
summary_data.to_csv(output_file_path, index=False)

print(f"Summary data written to {output_file_path}")


