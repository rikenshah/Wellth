# This is a magic script that transforms two datasets into one smartly by comparison of resonse parameters

import pandas as pd

datapath = "data.csv"
datapath2 = "../datasets/prudentialLifeInsurance/train.csv"
savepath1 = "../datasets/merged.csv"

df = pd.read_csv(datapath)

df2 = df[df["Individual Tobacco Rate"].notnull()]

individual_rate = df2["Individual Rate"]
# normalized_individual_rate = ((individual_rate-individual_rate.mean())/individual_rate.std())*4+4
# normalized_individual_rate = (individual_rate-individual_rate.min())/(individual_rate.max()-individual_rate.min())

individual_tobacco_rate =  df2["Individual Tobacco Rate"]
# normalized_individual_tobacco_rate = ((individual_tobacco_rate-individual_tobacco_rate.mean())/individual_tobacco_rate.std())*4+4

# here multiplying by 8 does not give a good range
rate_diff = (individual_tobacco_rate-individual_rate)*16/individual_rate
df2["rate_diff"] = pd.Series(rate_diff)

response = 1

mapping_dict = {}

def init_map(df2,i):
	if i == 0:
		mapping_dict[0] = df2.loc[(df2.rate_diff < 0.5)].iterrows()
	elif i == 1:
		mapping_dict[1] = df2.loc[(df2.rate_diff < 1) & (df2.rate_diff >0.5)].iterrows()
	elif i in range(2,8):
		mapping_dict[i] = df2.loc[(df2.rate_diff < i) & (df2.rate_diff >(i-1))].iterrows()
	elif i == 8:
		mapping_dict[8] = df2.loc[(df2.rate_diff >7)].iterrows()
	else:
		return

for i in range(9):
	init_map(df2,i)

## Loading second dataset
df3 = pd.read_csv(datapath2)
df3 = df3[df3.Response.notnull()]

for i, row in df3.iterrows():
	try:
		new_tuple = next(mapping_dict[row.Response])
	except:
		init_map(df2,row.Response)
	for key,value in new_tuple[1].iteritems():
		df3.set_value(i,key,value)

df3.to_csv(savepath1)
