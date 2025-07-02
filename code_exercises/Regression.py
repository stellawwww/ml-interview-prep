import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This tells Python to go up one directory and then into the datasets folder
df = pd.read_csv("../datasets/College.csv")

# display the column names
df.columns

# the first column is the name of the university
df3 = df.rename(columns={"Unnamed: 0": "University"})

# since we don't use it in analysis, set it as index
df3.set_index("University", inplace=True)

df3.describe()

# produce scatterplot matrix
pd.plotting.scatter_matrix(df3[["Top10perc", "Apps", "Enroll"]], figsize=(10, 10))
