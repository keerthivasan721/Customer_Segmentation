import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import os
import scipy
import warnings 
import datetime as dt
from datetime import datetime as dt2
warnings.filterwarnings("ignore")
from source import *

data = df

# To remove the Invoice no with c on it which was a cancelled order
data['InvoiceNo'] = data['InvoiceNo'].astype('str')
data = data[~data['InvoiceNo'].str.contains('c')]

# To remove the negative values from the quantity which could be cancelled order
data = data[data.Quantity > 0]

# To remove the negative values and cancelled order price from the feature
data = data[data.UnitPrice > 0]

# To remove the missing values since we cannot find the customer id data
data = data.dropna(subset=['CustomerID'])

# To convert the date into correct data type
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

data = data.drop_duplicates(keep='first')

country_transformed = pd.get_dummies(data['Country'])

column_name_country = list(country_transformed.columns)
column_name_country = ['country_'+ col for col in column_name_country]
country_transformed.columns = column_name_country

data_with_dummies = pd.concat([data, country_transformed], axis=1)

numerical = data.select_dtypes(include= ['int64','float64'])

def find_outliers(x):
    q1 = x.quantile(0.25)
    q3 = x.quantile(0.75)
    IQR = q3 -q1
    outliers = x[(x<(q1-1.5*IQR)) | (x>(q3+1.5*IQR))]
    return outliers

outliers = find_outliers(numerical)

outliers = outliers.dropna(how='all')

data = data.drop(index= outliers.index)

data['Revenue'] =  data['Quantity']*data['UnitPrice']

pre_processed_data = data.copy()

#pre_processed_data.to_csv("Dataset/processed_data.csv",index=False)


# print(data.shape)
# print(pre_processed_data.shape)