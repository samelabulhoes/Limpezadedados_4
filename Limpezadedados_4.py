import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, None, 5],
    'C': [1, None, None, 4, None]
})

# Fill null values with the median of each column
df = df.apply(lambda x: x.fillna(x.median()), axis=0)

print(df)
