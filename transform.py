import pandas
import numpy as np
import pandas as pd

def transform(df):
    PIB_list = df["PIB_FMI"].tolist()
    PIB_list = [float("".join(x.split(','))) for x in PIB_list]
    PIB_list = [np.round(x/1000,2) for x in PIB_list]
    df["PIB_FMI"] = PIB_list
    df=df.rename(columns = {"PIB_FMI":" PIB_FMI_billions"})
    return df   