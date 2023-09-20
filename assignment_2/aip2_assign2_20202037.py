import pandas as pd


# Define column names
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Load the data into a DataFrame
df = pd.read_csv('actual_file_path_here.csv', header=None, delimiter=r"\s+", names=column_names)
