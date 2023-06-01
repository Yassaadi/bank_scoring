# bank_scoring
![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/45b0970c-bccd-4b58-a354-a73325509c29)
ASSAADI YASSINE : PROJECT 7 RECAP
1.	Model training 


•	Data preparation and preprocessing : 
•	Data merging and grouping by, Encoding categorical features,, 
•	Handeling missing data by elimination of columns and row containing excessive Nan values.
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
•	Registering all the 7th experiments to Mlflow registry..
•	Serving and saving the best model under pkl format, to be ready for production.
2.	Unbalanced classes treatment 

Unbalanced data can lead to biased models that perform poorly on the minority class which is the case in our example. In fact, a false high performance results of training models on an unbalanced data. Therefore, it is important to treat unbalanced data by using techniques such as oversampling or undersampling to balance the classes.

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/c022f080-aa50-4f19-b762-d5ffeb40bd15)

In my case, I tried many combinaison of oversampling and undersampling, SMOTE with 10% strategy and randomized undersampling with 10% were chosen, this means that the data was oversampled using SMOTE to increase the number of instances in the minority class, while also randomly undersampling the majority class to reduce its dominance in the data. This approach can help to improve model performance by providing more balanced training data that better represents the underlying distribution of the problem. Additionally, the use of a 10% strategy means that only a portion of the data was affected by the resampling technique, which can help to mitigate potential issues related to overfitting or loss of important information.
![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/65b40e51-8238-46be-bfae-14556e22078b)


3.	Metrics

The financial impact of false negative is very hiegh according to the manager. Ten times higher than the impact of false positive which represents good clients predicted as bad profiles. It is then important appropriate metrics to select the best model.
In the context described, the metric of choice should be one that prioritizes minimizing false negatives, as the financial impact of these errors is very high. This is where ROC AUC (Receiver Operating Characteristic Area Under the Curve) can be a more appropriate metric to use than accuracy.
Accuracy simply measures the percentage of correct predictions made by the model, without considering the balance of false positives and false negatives. However, in cases where the cost of false negatives is much higher than that of false positives, accuracy can be a misleading metric to use as it may favor models that produce more false positives in order to minimize false negatives. A dummy classifier can appear very promoting if we only rely on accuracy for examples :
![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/93e106e7-98d8-48d1-9d12-402c33998fc3)


On the other hand, ROC AUC takes into account the trade-off between true positive rate and false positive rate at different classification thresholds, and provides a measure of the overall predictive power of the model. By looking at the entire ROC curve and the area under it, it gives a more complete picture of the model's ability to correctly classify cases and make good predictions.
I chosed also Fcb = F(=10) as a metric which is a way to stand up between recall and precision by giving 10 times importance to FN  impact than FP impact. A total importance. of FP is a F(=0)=Precision.

4.	Sum up of modeling

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/e5591b8d-a7ca-41f5-9250-f4573369bd6c)

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/288e41d3-3392-476e-bf9c-4378bea068ed)


The best model correspond to the stacking model :

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/00ece513-ed44-4aba-82b2-0481e734ec2d)

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/c73c1730-663f-44da-a8e0-19c250ef70a6)


Important features)

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/f11938f2-0710-4a64-a62e-908fc7aa56da)

5.	Drift monitoring 

Data drift is the phenomenon where the statistical properties of data change over time, which can cause models to become less accurate if they are not adapted to the new data distribution. In our case I performed a data drift monitoring using evidently library by taking as reference data my current training data and production data the application test data given by the manager.
The drift is calculated using Jensen-Shannon Divergence (JSD) and Wasserstein Distance. Only one features represents drift in my set of tested features, this drift is estimated to 14,29% which has no impact on model retraining.

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/d828fb87-c0a7-4574-8860-c90a2a8e436c)


6.	Streamlit dashboard

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/b87dba9e-bcc3-4c1a-a733-ca42a3f88864)

![image](https://github.com/Yassaadi/bank_scoring/assets/106546639/aefbcb39-1dd4-4f78-a5b9-94a42967d0de)




 
 
 
 
