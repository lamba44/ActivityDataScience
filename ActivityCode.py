import numpy as np
import pandas as pd

# Read the CSV file into a pandas DataFrame.
df = pd.read_csv("data.csv")

print("Collected Data as a DataFrame:\n")
print(df)

data_array = df.to_numpy()  # or use df.values
print("\nNumPy Array:")
print(data_array)

year_counts = df["What is your year of study?"].value_counts()
print("\nStudent counts by Year:")
print(year_counts)

extremely_dissatisfied_count = df[
    df["How would you rate the overall quality of your current courses?  "] == 1
].shape[0]
print("\nNumber of extremely dissatisfied responses for Q1:")
print(extremely_dissatisfied_count)
