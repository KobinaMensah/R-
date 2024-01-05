
#import pandas as pd
#import numpy as np
#from pyodide.http import pyfetch

#async def download(url, file_name):
    #response = await pyfetch(url)
    #if response.status == 200:
        #with open(file_name, "wb") as f:  # Corrected the variable name here
            #f.write(await response.bytes())

#url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
#file_name = 'auto.csv'

# Download the file
#await download(url, file_name)

# Read the downloaded file into a DataFrame
#df = pd.read_csv(file_name)
#print("The first 5 rows of the dataframe:")
#print(df.head())

# Importing a dataset from n url and saving it as a csv file using pandas package in python
import pandas as pd
import requests
import numpy as np

def download_and_save_csv(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully as '{file_name}'")
    else:
        print("Failed to download the file")

# URL of the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

# File name to save the downloaded dataset
file_name = 'auto.csv'

# Download the file and save it as a CSV
download_and_save_csv(url, file_name)

# Optionally, load the CSV into a Pandas DataFrame
df = pd.read_csv(file_name)

# Print the first few rows of the DataFrame
print("The first 5 rows of the dataframe:")
print(df.head())
print("This are the last 5 rows of the dataframe:")
print(df.tail())

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
print(df.columns)

df1=df.replace('?',np.NaN)
print(df1.head(10))
df=df1.dropna(subset=["price"], axis=0)
print(df.head(20))

#summary statistics
print(df.describe(include = 'all'))
print(df.describe())










