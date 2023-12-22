import os
import pandas as pd

def create_summary(input_file_path, output_file_path):
    # Read the CSV file
    df = pd.read_csv(input_file_path, compression='zip')

    # Group data by country and calculate count and mean
    summary_data = df.groupby('country').agg({'points': ['count', 'mean']}).reset_index()

    # Rename columns for better clarity
    summary_data.columns = ['country', 'count', 'points']

    # Sort the data by count in descending order
    summary_data = summary_data.sort_values(by='count', ascending=False)

    # Write the summary data to a new CSV file
    summary_data.to_csv(output_file_path, index=False)

    print(f"Summary data written to {output_file_path}")

def test_file_exists():
    assert os.path.isfile('data/winemag-data-130k-v2.csv.zip'), "csv file does not exist"

def test_output_file_exists():
    create_summary('data/winemag-data-130k-v2.csv.zip', 'data/reviews-per-country.csv')
    assert os.path.isfile('data/reviews-per-country.csv'), "output csv file does not exist"

def test_columns_exist():
    create_summary('data/winemag-data-130k-v2.csv.zip', 'data/reviews-per-country.csv')
    expected_columns = ['country', 'count', 'points']
    df = pd.read_csv('data/reviews-per-country.csv')
    assert all(col in df.columns for col in expected_columns), "Columns do not match"

def test_values_exist():
    create_summary('data/winemag-data-130k-v2.csv.zip', 'data/reviews-per-country.csv')
    test_cases = [('US', 54504, 88.6), ('France', 22093, 88.8), ('Italy', 19540, 88.6),
                  ('Spain', 6645, 87.3), ('Israel', 505, 88.5), ('Egypt', 1, 84.0)]

    for country, count, points in test_cases:
        df = pd.read_csv('data/reviews-per-country.csv')
        row = df[df['country'] == country].iloc[0]
        assert row['count'] == count, f"Count for {country} does not match"
        assert row['points'] == points, f"Points for {country} does not match"

if __name__ == "__main__":
    test_file_exists()
    test_output_file_exists()
    test_columns_exist()
    test_values_exist()



