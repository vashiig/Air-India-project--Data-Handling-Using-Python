import pandas as pd

nof = input("Enter the name of file ", )
yr = input("Enter the yr(only last 2 digits) ", )

df = pd.read_csv("Tap_"+nof+yr+".csv")
df = df[~df.RMK.str.contains("XXD")]
df.to_csv("Tap_"+nof+yr+".csv", index=False)

