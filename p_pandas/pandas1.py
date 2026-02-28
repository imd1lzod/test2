import pandas as pd
df = pd.read_csv("adult.data.csv")
# print(df["sex"].value_counts())
# print(df[df["sex"] == "Female"]["age"].mean())
per = (df['native-country'] == "Germany").mean() * 100
print(per)