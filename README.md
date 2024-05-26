 **Author:** Charles Barnes
  
**Institution:** QuickStart Inc
  
**Active Project Dates:** May 6th, 2024 - May 20th, 2024
## Summary

A bank will start a campaign soon to contact clients about opening a term account. The bank has data about previous campaigns and management wants to use the data to design a strategy around contacting clients. To address this problem, I used supervised machine learning algorithms to predict whether a client would subscribe to a term account based on available data. I tested modifications to stages in the model building process and used three model types including logistic regression, decision tree, and random forest models. I found that a random forest model achieved the best accuracy, about 70%, for predicting term subscriptions. This model could be used by the bank during their next campaign to inform the outreach strategy when contacting current and prospective clients.

## Business Problem

A bank in Portugal has been collecting data on their clientele. They have archived the data but now think that this data could be useful to identify customers who are more likely to subscribe to a term account. The information would then be used to prioritize contacting clients during the next campaign.

## Data

The data in this scenario is the [bank marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) dataset. The data includes banking, life, career, previous campaign information, and whether or not a client subscribed to a term account.

## Methods

### 1. Exploratory data analysis (EDA)
EDA included descriptive statistics of features, histograms for numeric features, bar charts for categorical features, and analysis of missing values.

### 2. Data cleaning and preprocessing
Based on EDA and documentation, I removed columns and then rows with multiple missing values. I scaled numeric features and one-hot-encoded categorical features. I used KNN to impute remaining `Null` values.

### 3. Model building and assessment
Base models always had class weight balanced due to an imbalance in the target variable (more 'No' than 'Yes' values). I tested sampling methods for imbalanced learning. To assess model performance, I used a train/test/validation split of 70/15/15% for classification reports. I combined the train/test splits and used 5- or 3-fold cross-validation (cv) for ROC-AUC and precision metrics. 

### 4. Hyperparameter selection
I used ROC-AUC to select logistic regression parameters and I used log-loss to select parameters for the tree models.

### 5. Threshold tuning
Depending on the classification problem, I used a logistic-regression model to demonstrate how tuning the decision threshold biases predictions for precision (accurate predictions but missed true cases) versus recall (less accurate predictions but no missed true cases).

## Results
(2.) I dropped `duration` and `poutcome` from the dataset and imputed `contact`. The dataset creators suggest removing `duration`. `poutcome` was mostly null values. Imputing `contact` preserved the existing imbalance that most clients use `cellular` devices compared to `telephone`.

(3.) I chose to focus model building on true positive precision (predicting those clients that did subscribe to term accounts). Precision improved moving from logistic regression, decision tree, and then to random forest models. Progression along base models resulted in a precision score of ~50%. The models progressively lost recall. The tree models had variance in the precision score indicating that the base model was overfit. 

(4.) The final random forest model had ~70% accuracy accross all scoring metrics. There was no bias predicting 'No' versus 'Yes'. Precision and recall were similar, too. This model had log-loss scoring in the hyperparameter search and random under sampling to unbias predictions.

## Conclusions
The final random forest model had a prediction accuracy better than random guessing. This model could be used as a tool to aid the outreach strategy for the next campaign.

## Considerations
With more time and resources, I would:
- use feature selection, dimension reduction for logistic regression models
- include other classifiers
- extend the hyperparameter search
- use oversampling to balance classes, not just under sampling.

Even over a short timeframe, like going from campaign to campaign, there can be changes to the economy that supercede prediction accuracy. More expensive training capacities could include this information in the model. With increased computing power, we could also consider information about the term account (length of the term, interest rate, penalties) and whether the client negotiated the conditions.
