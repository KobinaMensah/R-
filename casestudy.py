import pandas as pd
import zipfile
import io

# Path to the zip file
zip_file_path = '/home/Emmanuel Kobina Mensah/Downloads/archive (1).zip'

# Path to the CSV file inside the zip archive
csv_file_path_inside_zip = 'Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv'

# Extract the CSV file from the zip archive
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Read the CSV file from the zip archive
    with zip_ref.open(csv_file_path_inside_zip) as file:
        # Read the CSV file directly into a Pandas DataFrame
        df = pd.read_csv(io.TextIOWrapper(file))

# Display the first few rows of the DataFrame
print(df.head())

