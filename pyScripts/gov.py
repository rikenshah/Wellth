import pandas as pd

datapath = "../datasets/healthcare.gov/data.csv"
df = pd.read_csv(datapath)

ir = df["Individual Rate"]
n_ir = (ir-ir.mean())/ir.std()


