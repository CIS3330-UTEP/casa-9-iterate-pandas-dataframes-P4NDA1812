

import pandas as pd 

df = pd.read_csv('big-mac-full-index.csv')

# Iterate over rows using .iloc[] (index-based)
print("Using iloc[] for index-based iteration:")
for i in range(len(df)):
    print(f"Row {i}: {df.iloc[i]}")

# Iterate over rows using .loc[] (label-based)
print("\nUsing loc[] for label-based iteration:")
for i in df.index:  # Here, index defaults to 0, 1, 2
    print(f"Row {i}: {df.loc[i]}")