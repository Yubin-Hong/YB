import pandas as pd
pu = pd.read_csv("Perception-Unhealthy.csv",header = None)
pi = pd.read_csv("Perception-Ideation.csv",header = None)
pp = pd.read_csv("Perception-Planning.csv",header = None)
def PerceptionOR(csv):
    yes =[]
    no =[]
    total =[]
    for row_index, row in csv.iterrows():
        yes.append(row.loc[0])
        no.append(row.loc[1])
        total.append(row.loc[0]+row.loc[1])
    UnderR= yes[0]/total[0]
    NormalR= yes[1]/total[1]
    OverR= yes[2]/total[2]
    UnderOR= UnderR/NormalR
    OverOR= OverR/NormalR
    print('Odd Ratio of Underweight:',UnderOR)
    print('Odd Ratio of Overweight:',OverOR)

print('Relation between Perception of Weight and Unhealthy Weight Control')
PerceptionOR(pu)
print('Relation between Perception of Weight and Suicidal Ideation')
PerceptionOR(pi)
print('Relation between Perception of Weight and Suicidal Planning')
PerceptionOR(pp)


