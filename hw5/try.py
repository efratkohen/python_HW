import numpy as np
import pandas as pd
import pathlib
from hw5 import *
import matplotlib.pyplot as plt

fname = 'data.json'
q = QuestionnaireAnalysis(fname)
q.read_data()
q.data['age']=q.data['age'].fillna(q.data['age'].mean())
i=0
for row in q.data['age']:
    if row>=40:
        q.data['age'].iloc[i]=True
    else:
        q.data['age'].iloc[i]=False
    i=i+1
print(q.data)
df=q.data.set_index(['gender', 'age'], append=True)
grouped = df.groupby(level=[1,2]).mean().drop(columns=['id'])
print(grouped)

