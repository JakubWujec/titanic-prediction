# Data Preparation & EDA

##  Dataset description
Data source: [link](https://www.kaggle.com/competitions/titanic/data?select=test.csv)

| Variable   | Definition                                  | Key                          |
|------------|---------------------------------------------|------------------------------|
| survival   | Survival                                    | 0 = No, 1 = Yes             |
| pclass     | Ticket class                                | 1 = Upper, 2 = Middle, 3 = Lower  |
| sex        | Sex                                         |                              |
| Age        | Age in years                                |Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5|
| sibsp      | # of siblings / spouses aboard the Titanic  | brothers / sisters / stepbrothers / stepsisters / husbands / wives       |
| parch      | # of parents / children aboard the Titanic  | mothers / fathers / daughters / sons / stepdaughters / stepsons    |
| ticket     | Ticket number                               |                              |
| fare       | Passenger fare                              |                              |
| cabin      | Cabin number                                |                              |
| embarked   | Port of Embarkation                        | C = Cherbourg, Q = Queenstown, S = Southampton |

Some children travelled only with a nanny, therefore parch=0 for them.

## New features
```python
df['cabin_deck'] = df['cabin'].str[0]
df['solo'] = ((df['sibsp'] == 0) & (df['parch'] == 0)).astype(int)
```
+ solo - binary variabble (1 if person was travelling without children/spouse/sibling etc.)
+ cabin_deck - deck of the ship taken from first letter of cabin name

### Cabin Decks
The bulk of First-Class facilities and accommodation was located on the upper decks within the superstructure of the Titanic, where the vibrations and noise of the engines were at their lowest. The entirety of A-Deck was devoted to First-Class recreation accommodation, along with most of B and C Decks.[source:wiki](https://en.wikipedia.org/wiki/First-class_facilities_of_the_Titanic#location)

## Data size
After data cleaning and preparation size of dataset is 891 rows and 14 columns.

Global survivorship calculated based on given dataset is around 38%.


# Scoring 
## ROC AUC score 
is a metric for evaluating the performance of a classification model. It measures a model's ability to distinguish between two classes, with a score between 0 and 1. A perfect model has a score of 1, while a random model has a score of 0.5. The score represents the probability that the model will rank a randomly chosen positive instance higher than a randomly chosen negative instance.  

    ROC AUC: stands for Receiver Operating Characteristic Area Under the Curve. 

The ROC curve plots the true positive rate (TPR) against the false positive rate (FPR) at various threshold settings. 
The AUC is the area under this curve. 


## How to interpret the score

    Perfect score (1.0): The model can perfectly separate the classes.
    Random model score (0.5): The model is no better than random guessing.
    Score below 0.5: The model is performing worse than random.
    Higher score: Generally indicates better performance. 



# Models

| Model  | AUC Score                              |
|------------|---------------------------------------------|
| Logistic Regression   | 0.839                                  | 
| DecisionTreeClassifier    | 0.882                             | 
| RandomForestClassifier    | 0.836                           | 
| XGB    | 0.828                         | 
