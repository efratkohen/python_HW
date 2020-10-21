import numpy as np
import pandas as pd
import pathlib

def txt_to_df (fname):
    df = pd.read_csv(fname,delimiter='\t')
    return df

def largest_species(fname: pathlib.Path) -> pd.Series:
    df = txt_to_df (fname)
    df_t=df.transpose()
    max_col=list(df_t.idxmax())
    data = pd.Series(max_col, index=df['# year'])
    return data

def lynxes_when_hares(fname: pathlib.Path) -> pd.Series:
    df = txt_to_df (fname)
    data=(df.loc[df['hare']>df['fox']])
    col=list(data['lynx'])
    data_s = pd.Series(col, index=data['# year'])
    return(data_s)

def mean_animals(fname: pathlib.Path) -> pd.DataFrame:
    df=txt_to_df(fname)
    df['total'] = df['hare']+df['lynx']+df['fox']
    df['mean_animals']=(df['total'])/(df['total'].max())
    df=df.drop(columns=['total'])
    df=df.drop(columns=['# year'])
    return(df)
