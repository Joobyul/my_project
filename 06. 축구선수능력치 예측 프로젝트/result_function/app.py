import pandas as pd 
import numpy as np 
player=[]
def find_team(gk, df1, df2, df3, df4, mid1, mid2, mid3, fw1, fw2, fw3):

    filename = './data/players_23.csv'
    filename1='./data/footballclub_2023_top180.csv'

    playDF=pd.read_csv(filename)
    teamDF=pd.read_csv(filename1)

    teamDF = teamDF.drop(columns=['FW','MID','DF'])
    teamDF['rank'] = (teamDF['TOTAL_MEAN'].rank(method='min', ascending=False)).astype('int64')

    overDF=playDF[(playDF['overall']>=70) & (playDF['overall']<=85)]
    gkDF=overDF[overDF['position']=='GK']
    dfDF=overDF[overDF['position']=='DF']
    midDF=overDF[overDF['position']=='MID']
    fwDF=overDF[overDF['position']=='FW']

    elveDF = pd.DataFrame(overDF)
    elveDF = elveDF.drop(elveDF.index)

    elveDF = elveDF.append(gkDF.iloc[1], ignore_index=True)
    elveDF = elveDF.append(dfDF.iloc[:4], ignore_index=True)
    elveDF = elveDF.append(midDF.iloc[:3], ignore_index=True)
    elveDF = elveDF.append(fwDF.iloc[:3], ignore_index=True)

    same_mean=teamDF[teamDF['TOTAL_MEAN']==elveDF['overall'].mean()]
    print(same_mean)

find_team()