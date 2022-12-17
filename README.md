# ***Customer_Segmentation***

- Used RFM method to calculate Recency, Frequency, Monetary to make a segmentation based on customer habits
- Receny : How recently the customer made a transaction.
- Frequency : How often the customer make transactions.
- Monetary : How many transactions the customer has made.

- Used Quartile statistical method to calculate the Individual RFM score
- we have assigned scores from 1 to 4.
- 4 being the highest and best, while 1 being the lowest.

- Used K-Means Clustering unsupervised Technique to cluster the customers depend on their habits
- K-Means Clustering is an unsupevised machine learning algorithm that uses multiple iterations to segment the unlabeled data points into  k different clusters.
 - For k_means clustering to give best result the followings conditions should be met:
  1. Data distribution must not be skewed.
  2. Data is standardised 
- used Elbow method to find the optimum number of clusters.
- Then used Davies Bouldin and silhouetter score to evaluate the model and optimise the k value.
