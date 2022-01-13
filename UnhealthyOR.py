import pandas as pd
import numpy as np

ui = pd.read_csv("Unhealthy-Ideation.csv",header = None)
up = pd.read_csv("Unhealthy-Planning.csv",header = None)

def UnhealthyOR(csv):
    yes = []
    no = []
    total = []
    for row_index, row in csv.iterrows():
        yes.append(row.loc[0])
        no.append(row.loc[1])
        total.append(row.loc[0] + row.loc[1])
    YesR = yes[0] / total[0]
    NoR = yes[1] / total[1]
    OR = YesR / NoR
    print('Odd Ratio:', OR)

print('Relation between Unhealthy Weight Control and Suicidal Ideation')
UnhealthyOR(ui)
print('Relation between Unhealthy Weight Control and Suicidal Planning')
UnhealthyOR(up)
