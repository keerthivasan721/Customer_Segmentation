from preprocess import *

# Recency value
rfm_table1 = pd.DataFrame(pre_processed_data['CustomerID'].unique())
rfm_table1.columns = ['CustomerID']

latest_purchase = pre_processed_data.groupby('CustomerID').InvoiceDate.max().reset_index()
latest_purchase.columns = ['CustomerID','LatestPurchaseDate']
latest_purchase['LatestPurchaseDate'] = pd.to_datetime(latest_purchase['LatestPurchaseDate'])
# Recency = point in time of observation - number of days last purchase
latest_purchase['Recency'] = (latest_purchase['LatestPurchaseDate'].max() - latest_purchase['LatestPurchaseDate']).dt.days


rfm_table1 = pd.merge(rfm_table1, latest_purchase[['CustomerID','Recency']], on='CustomerID')

# Frequency

frequency = data.groupby('CustomerID').InvoiceDate.count().reset_index()
frequency.columns = ['CustomerID','frequency']
rfm_table1 = pd.merge(rfm_table1,frequency, on='CustomerID')

# Monetary

monetary = pre_processed_data.groupby('CustomerID').Revenue.sum().reset_index()
monetary.columns = ['CustomerID','monetary']

rfm_table1 = pd.merge(rfm_table1, monetary, on='CustomerID')

# RFM Scores
quartiles = rfm_table1.quantile(q=[0.25, 0.5, 0.75])

segmented_rfm1 = rfm_table1.copy()

def recency_score (data):
    if data <= 15:
        return 4
    elif data <= 47:
        return 3
    elif data <= 135:
        return 2
    else:
        return 1

def frequency_score (data):
    if data <= 16:
        return 1
    elif data <= 38:
        return 2
    elif data <= 87:
        return 3
    else:
        return 4
def monetary_value_score (data):
    if data <= 219.9525:
        return 1
    elif data <= 489.5500:
        return 2
    elif data <= 1183.5400:
        return 3
    else:
        return 4

segmented_rfm1['R'] = segmented_rfm1['Recency'].apply(recency_score )
segmented_rfm1['F'] = segmented_rfm1['frequency'].apply(frequency_score)
segmented_rfm1['M'] = segmented_rfm1['monetary'].apply(monetary_value_score)

# Total RFM Score

segmented_rfm1['RFM_score'] =segmented_rfm1[['R', 'F', 'M']].sum(axis=1)
segmented_rfm1['RFM_Segment'] = segmented_rfm1.R.map(str)+segmented_rfm1.F.map(str)+segmented_rfm1.M.map(str)

# Labelling the customers

label = [0] * len(segmented_rfm1)

for i in range(0,len(segmented_rfm1)):

    if segmented_rfm1['RFM_Segment'][i] == '444':
        label[i] = "Best Customers"
        
    elif segmented_rfm1['RFM_Segment'][i] == '334'or segmented_rfm1['RFM_Segment'][i] == '441'or segmented_rfm1['RFM_Segment'][i] == '442'or segmented_rfm1['RFM_Segment'][i] == '244'or segmented_rfm1['RFM_Segment'][i] == '343'or segmented_rfm1['RFM_Segment'][i] == '344'or segmented_rfm1['RFM_Segment'][i] == '433'or segmented_rfm1['RFM_Segment'][i] == '434'or segmented_rfm1['RFM_Segment'][i] == '443':
        label[i] = "Loyal Custumers"
        
    elif segmented_rfm1['RFM_Segment'][i] == '311'or segmented_rfm1['RFM_Segment'][i] == '324'or segmented_rfm1['RFM_Segment'][i] == '341'or segmented_rfm1['RFM_Segment'][i] == '342'or segmented_rfm1['RFM_Segment'][i] == '314'or segmented_rfm1['RFM_Segment'][i] == '414'or segmented_rfm1['RFM_Segment'][i] == '424'or segmented_rfm1['RFM_Segment'][i] == '312' or segmented_rfm1['RFM_Segment'][i] == '313' or segmented_rfm1['RFM_Segment'][i] == '321'or segmented_rfm1['RFM_Segment'][i] == '322'or segmented_rfm1['RFM_Segment'][i] == '323'or segmented_rfm1['RFM_Segment'][i] == '331'or segmented_rfm1['RFM_Segment'][i] == '332'or segmented_rfm1['RFM_Segment'][i] == '333'or segmented_rfm1['RFM_Segment'][i] == '411'or segmented_rfm1['RFM_Segment'][i] == '412'or segmented_rfm1['RFM_Segment'][i] == '413'or segmented_rfm1['RFM_Segment'][i] == '421'or segmented_rfm1['RFM_Segment'][i] == '422'or segmented_rfm1['RFM_Segment'][i] == '423'or segmented_rfm1['RFM_Segment'][i] == '431'or segmented_rfm1['RFM_Segment'][i] == '432':
        label[i] = "Potential Costumers"

    elif segmented_rfm1['RFM_Segment'][i] == '222'or segmented_rfm1['RFM_Segment'][i] == '223'or segmented_rfm1['RFM_Segment'][i] == '232'or segmented_rfm1['RFM_Segment'][i] == '233'or segmented_rfm1['RFM_Segment'][i] == '113'or segmented_rfm1['RFM_Segment'][i] == '114'or segmented_rfm1['RFM_Segment'][i] == '131'or segmented_rfm1['RFM_Segment'][i] == '141'or segmented_rfm1['RFM_Segment'][i] == '213'or segmented_rfm1['RFM_Segment'][i] == '214'or segmented_rfm1['RFM_Segment'][i] == '231'or segmented_rfm1['RFM_Segment'][i] == '214'or segmented_rfm1['RFM_Segment'][i] == '231'or segmented_rfm1['RFM_Segment'][i] == '241'or segmented_rfm1['RFM_Segment'][i] == '243':
        label[i] = "Customers Needing Attention"
    
    elif segmented_rfm1['RFM_Segment'][i] == '144'or segmented_rfm1['RFM_Segment'][i] == '244'or segmented_rfm1['RFM_Segment'][i] == '143'or segmented_rfm1['RFM_Segment'][i] == '134':
        label[i] = "Cant' Lose Them"

    elif segmented_rfm1['RFM_Segment'][i] == '121'or segmented_rfm1['RFM_Segment'][i] == '122'or segmented_rfm1['RFM_Segment'][i] == '112'or segmented_rfm1['RFM_Segment'][i] == '212'or segmented_rfm1['RFM_Segment'][i] == '211'or segmented_rfm1['RFM_Segment'][i] == '221'or segmented_rfm1['RFM_Segment'][i] == '222'or segmented_rfm1['RFM_Segment'][i] == '123'or segmented_rfm1['RFM_Segment'][i] == '124'or segmented_rfm1['RFM_Segment'][i] == '132'or segmented_rfm1['RFM_Segment'][i] == '133'or segmented_rfm1['RFM_Segment'][i] == '134'or segmented_rfm1['RFM_Segment'][i] == '142'or segmented_rfm1['RFM_Segment'][i] == '224'or segmented_rfm1['RFM_Segment'][i] == '242':
        label[i] = "At Risk Customers"

    elif segmented_rfm1['RFM_Segment'][i] == '111':
        label[i] = "Lost Customers"
        
    else:
        label[i] = "Others"

segmented_rfm1['label'] = label
print(segmented_rfm1)