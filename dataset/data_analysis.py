import os
import zipfile
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tikzplotlib

plt.style.use("paper")


# Path to your zip file
zip_path_sp = "sp.zip"
zip_path_nsp = "no_sp.zip"


# Function to extract the first and second columns from the csvs in a zip file
def extract_columns_from_zip(zip_path):
    data_dict = {}
    max_idx = 0

    with zipfile.ZipFile(zip_path, "r") as z:
        for file_index, file_name in enumerate(z.namelist()):
            if file_name.endswith(".csv"):
                with z.open(file_name) as f:
                    # Read the CSV without headers
                    df = pd.read_csv(f, header=None)
                    # Extract first and second columns
                    col1 = df[0].astype(int).tolist()[:50]
                    max_idx = np.max((max_idx, np.max(col1)))
                    col2 = df[1].tolist()[:50]
                    # Store the columns in the dictionary
                    data_dict[file_index] = (col1, col2)

    return data_dict, max_idx


def find_unique_values(data_dict):
    # Flatten column 1 across all files
    all_values = []
    for col1, col2 in data_dict.values():
        all_values.extend(col1)  # Add all values from column 1

    # Count occurrences of each value
    value_counts = Counter(all_values)

    # Find repeated values (those with a count greater than 1)
    # repeated_values = {val: count for val, count in value_counts.items() if count > 49}

    return np.sort([val for val, _ in value_counts.items()])


# Extract data for both folders
data_SP, max_idx_SP = extract_columns_from_zip(zip_path_sp)
data_NSP, max_idx_NSP = extract_columns_from_zip(zip_path_nsp)
max_idx = np.max((max_idx_SP, max_idx_NSP)) + 1

# Print results
# print("Folder 1 Data:")
# for idx, (col1, col2) in data_SP.items():
#     print(f"File {idx}: Column 1 - {col1[:5]}, Column 2 - {col2[:5]}...")
#
# print("Folder 2 Data:")
# for idx, (col1, col2) in data_NSP.items():
#     print(f"File {idx}: Column 1 - {col1[:5]}, Column 2 - {col2[:5]}...")


unique_SP = find_unique_values(data_SP)
unique_NSP = find_unique_values(data_NSP)
unique_all = np.unique(np.concatenate((unique_SP, unique_NSP)))

map_to_unique = {}
for i in range(unique_all.shape[0]):
    map_to_unique[unique_all[i]] = i

unique_count = unique_all.shape[0]
mat_SP = np.zeros((unique_count, len(data_SP)))
mat_NSP = np.zeros((unique_count, len(data_SP)))
for k, v in data_SP.items():
    idx = []
    for j in range(len(v[0])):
        idx.append(map_to_unique[v[0][j]])
    mat_SP[idx, k - 1] = v[1]
for k, v in data_NSP.items():
    idx = []
    for j in range(len(v[0])):
        idx.append(map_to_unique[v[0][j]])
    mat_NSP[idx, k - 1] = v[1]
mat_full = np.concatenate((mat_NSP, mat_SP), axis=1)


plt.figure()
plt.subplot(211)
plt.imshow(mat_NSP.T)
plt.ylabel("Files")
xticks = np.arange(0, 450, 50)
plt.xticks(xticks, ["\empty" for x in xticks])
plt.ylabel("Files")
plt.subplot(212)
plt.imshow(mat_SP.T)
plt.xticks(xticks, [f"{x}" for x in xticks])
# plt.subplot(133)
# plt.imshow(mat_full.T)
# xticks = np.concatenate((range(50), range(50)))
# yticks = [0, 50, 51, 100]
# ynames = [0, 50, 0, 50]
# plt.yticks(yticks, [f"{x}" for x in ynames])
plt.ylabel("Files")
plt.xlabel("Features")
tikzplotlib.save("feature_matrix.tikz")

plt.figure()
mean_SP = np.mean(mat_SP, axis=1)
mean_NSP = np.mean(mat_NSP, axis=1)
idx = np.flip(mean_NSP.argsort())
mean_SP = mean_SP[idx]
mean_NSP = mean_NSP[idx]
plt.bar(range(unique_count), mean_NSP, label="NSP")
plt.bar(range(unique_count), mean_SP, label="SP")
plt.ylabel("Activation Strength")
plt.xlabel("Sorted Features")
tikzplotlib.save("mean_features.tikz")

plt.show()
