import numpy as np
import pandas as pd
import pathlib


def common_complaint(fname: pathlib.Path):

    """Finds and returns the most common complaint as (complaint_name, num)."""
    df = pd.read_csv(fname)
    most_common_complaint=df['Complaint Type'].value_counts().idxmax() 
    number_of_occasions=df['Complaint Type'].value_counts().max()
    ans=(most_common_complaint,number_of_occasions)
    return ans

def parking_borough(fname: pathlib.Path) -> str:
    """Finds and returns the name of the NYC borough that has the
    most complaints of type 'Illegal Parking'."""
    df = pd.read_csv(fname)
    df_Illegal_Parking=df.loc[df['Complaint Type']=="Illegal Parking"]
    NYC_borough=df_Illegal_Parking['Borough'].value_counts().idxmax()
    return NYC_borough
