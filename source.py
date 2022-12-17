import pandas as pd
import numpy as np


def read_dataset(x):
    df = pd.read_csv(x)
    return df

df = read_dataset(r'Dataset\train.csv')
