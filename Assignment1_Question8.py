#Imports pandas package calling it pd.
import pandas as pd

#Initial data dictionary.
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

#Creates a DataFrame from the dictionary.
df = pd.DataFrame(data)

#Adds a new computed column using existing columns.
df["Sum"] = df["A"] + df["B"] + df["C"]

#Prints the final DataFrame.
print(df)