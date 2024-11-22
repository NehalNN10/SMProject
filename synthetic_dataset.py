import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
data = pd.read_csv("T0002-10.1080_0144929X.2022.2151512 (1).csv")

# Extract the relevant columns
columns = [
    "Subjective measures",
    "Addiction",
    "Short M",
    "Short SD",
    "Medium M",
    "Medium SD",
    "Long M",
    "Long SD",
]
data.columns = columns

# Initialize an empty list to store synthetic data
synthetic_data = []


# Function to generate synthetic data
def generate_synthetic_data(mean, std, size=100):
    return np.random.normal(mean, std, size)


# Iterate over each row in the DataFrame
for index, row in data.iterrows():
    if index == 0:  # Skip the header row
        continue
    measure = row["Subjective measures"]
    addiction = row["Addiction"]

    short_data = generate_synthetic_data(float(row["Short M"]), float(row["Short SD"]))
    medium_data = generate_synthetic_data(
        float(row["Medium M"]), float(row["Medium SD"])
    )
    long_data = generate_synthetic_data(float(row["Long M"]), float(row["Long SD"]))

    for value in short_data:
        synthetic_data.append([measure, addiction, "Short", value])
    for value in medium_data:
        synthetic_data.append([measure, addiction, "Medium", value])
    for value in long_data:
        synthetic_data.append([measure, addiction, "Long", value])

# Create a new DataFrame with the synthetic data
synthetic_df = pd.DataFrame(
    synthetic_data, columns=["Subjective measures", "Addiction", "Duration", "Value"]
)

# Save the synthetic dataset to a new CSV file
synthetic_df.to_csv("synthetic_dataset.csv", index=False)