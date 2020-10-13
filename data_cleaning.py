import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

# setting up pandas for a better data visualization in terminal
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# importing data and read them
data_path = "data /heart_failure_clinical_records_dataset.csv"
data = pd.read_csv(data_path)
print(data.head())

