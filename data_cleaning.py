import pandas as pd

# setting up pandas for a better data visualization
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# importing data and read them
data_path = "data /heart_failure_clinical_records_dataset.csv"
data = pd.read_csv(data_path)
print(data['age'])
print(type(data['age']))


