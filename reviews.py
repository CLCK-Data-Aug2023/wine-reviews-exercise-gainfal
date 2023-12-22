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


