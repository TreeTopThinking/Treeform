import pandas as pd

df = pd.read_csv("syllables.csv")

seen = []

for i in range(df.shape[0]):
    value = df.iloc[i, 1]
    if value in seen:
        print(value)
        continue
    seen.append(value)
