import pandas as pd
import requests
import matplotlib.pylab as plt
import numpy as np

# downloading a dataset from a using a url and saving as a csv file
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
file_name = 'usedcars.csv'

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
df = pd.read_csv(file_name, names = headers)
print(df.head())
# replacing blanks and missing values with NAN
df.replace("?", np.nan, inplace = True)

missing_data = df.isnull() # creates a table with boolean with true inducating there is a value in the row and false indicating a missing value
print(missing_data.head(5))

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts()) # returns a count of the number of missing values in all the columns
    print("") 

# replacing the missing values with the mean of each of the columns
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print(" The Average of normalized-losses is:", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True) # this code replaces the nan with the mean ofthe normalized losses
avg_bore=df['bore'].astype('float').mean(axis=0)
print(" The Average of bore is :", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True) # this code replaces the nan with the mean ofthe bore column
avg_stroke=df['stroke'].astype('float').mean(axis=0)
df["stroke"].replace(np.nan,avg_stroke,inplace = True) # this code replaces the missing values in the stroke column with the mean

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

freq_num_of_doors = df['num-of-doors'].value_counts().idxmax() # returns the most frequent value in the num of doors column
df["num-of-doors"].replace(np.nan, freq_num_of_doors, inplace=True) # replaces the nan values with the mode of the number of doors
print(df["num-of-doors"].head(15))
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)
print(df.head(15))
#changing the data types from objects to floats or int
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
print(df.dtypes)

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]
df.head() # check your transformed data 

#change of column name from highway mpg to highway L/100km
df["highway-L/100km"] = 235/df["highway-mpg"]
df.rename(columns={"highway-mpg": "highway-L/100km”"}, inplace = True)

# DATA NORMALIZATION
df["height"] = df["height"]/df["height"].max()
df["length"] = df["length"]/df["length"].max()
df["width"] = df["width"]/df["width"].max()
print(df["length"].head())
print(df["width"].head())
print(df["height"].head())