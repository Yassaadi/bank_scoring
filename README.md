# bank_scoring
ASSAADI YASSINE : SCORING PROJECT RECAP

Data source: https://www.kaggle.com/competitions/home-credit-default-risk/data

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/45b0970c-bccd-4b58-a354-a73325509c29)

## Data preprocessing and modeling 

•	Data preparation and preprocessing  

 o Data merging and grouping by
 
 o Encoding categorical features 
 
 o	Handeling missing data by elimination of columns and row containing excessive Nan values

•	Features selection and features engineering : Kaggle kernel

•	Data split : train and test sets and drift data

•	Handeling unbalanced classes.

•	Data transformation : Standard scalering

•	Model training : 

o	Creation of Mlflow experiment tracker

o	1st experiment : Dummy classfier, that helped as resference for other classifiers 

o	2nd experiment : XGBoost classifier

o	3rd experiment LGBM classifier

o	4th experiment Catboost classifier

o	5th experiment Random forest classifier 

o	6th experiment : Stacking model of the XGBoost classfier, LGBM classifier, Catboost classifier and Random Forest classfier .

o	7th experiment Pipeline of data transformation by standard scalering and the stacking model.

•	Model analysis and features importance identification for each of the main models .

•	Registering all the 7th experiments to Mlflow registry.

•	Serving and saving the best model under .pkl format, to be ready for production readiness.

## Unbalanced classes handeling 

Unbalanced data can lead to biased models that perform poorly on the minority class, which is the case in our example. It is important to address unbalanced data by using techniques such as oversampling or undersampling to balance the classes.

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/c022f080-aa50-4f19-b762-d5ffeb40bd15)

In this project, I tried various combinations of oversampling and undersampling techniques. I chose to use SMOTE with a 10% strategy and randomized undersampling with a 10% ratio. This means that the data was oversampled using SMOTE to increase the number of instances in the minority class while also randomly undersampling the majority class to reduce its dominance in the data. This approach helps improve model performance by providing more balanced training data that better represents the underlying distribution of the problem. Additionally, using a 10% strategy ensures that only a portion of the data is affected by the resampling technique, mitigating potential issues related to overfitting or loss of important information.

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/65b40e51-8238-46be-bfae-14556e22078b)


## Metrics 

The manager has highlighted that the financial impact of false negatives is very high, ten times higher than the impact of false positives, which refers to good clients being predicted as bad profiles. Therefore, it is crucial to select appropriate metrics to determine the best model.

In the described context, the chosen metric should prioritize minimizing false negatives due to their significant financial impact. In this regard, ROC AUC (Receiver Operating Characteristic Area Under the Curve) is a more suitable metric than accuracy.

Accuracy measures the percentage of correct predictions made by the model without considering the balance between false positives and false negatives. However, in cases where the cost of false negatives is much higher than that of false positives, accuracy can be misleading as it may favor models that produce more false positives to minimize false negatives. Relying solely on accuracy can lead to a dummy classifier appearing highly effective, as shown below:

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/93e106e7-98d8-48d1-9d12-402c33998fc3)

On the other hand, ROC AUC considers the trade-off between the true positive rate and false positive rate at different classification thresholds, providing a measure of the model's overall predictive power. By examining the entire ROC curve and the area under it, a more comprehensive understanding of the model's ability to accurately classify cases and make reliable predictions is obtained.

Additionally, I have chosen Fcb = F(beta=10) as a metric, which strikes a balance between recall and precision by assigning ten times more importance to the impact of false negatives (FN) compared to false positives (FP). The total importance of FP is represented by F(beta=0), which is equivalent to precision.

## Modeling experiences tracking 

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/e5591b8d-a7ca-41f5-9250-f4573369bd6c)

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/288e41d3-3392-476e-bf9c-4378bea068ed)


The best model correspond to the stacking model :

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/00ece513-ed44-4aba-82b2-0481e734ec2d)


![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/c73c1730-663f-44da-a8e0-19c250ef70a6)


## Important features

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/f11938f2-0710-4a64-a62e-908fc7aa56da)

## Drift monitoring 

Data drift refers to the phenomenon where the statistical properties of data change over time. If models are not adapted to the new data distribution, they can become less accurate. In our case, I performed data drift monitoring using the evidently library, using my current training data as the reference and the application test data provided by the manager as the production data.

To quantify data drift, I calculated the Jensen-Shannon Divergence (JSD) and Wasserstein Distance. Among the set of tested features, only one feature exhibited drift. The calculated drift for this feature was estimated to be 14.29%. Fortunately, this drift has no significant impact on model retraining, indicating that the model can still perform effectively without requiring adjustments due to the observed data drift.

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/d828fb87-c0a7-4574-8860-c90a2a8e436c)


## Model as Streamlit dashboard

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/b87dba9e-bcc3-4c1a-a733-ca42a3f88864)

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/aefbcb39-1dd4-4f78-a5b9-94a42967d0de)

## Streamlit app deployement on Azure services

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/a6a6088b-6962-4283-960a-3d7ae3466398)




 
 
 
 
