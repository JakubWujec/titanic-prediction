# Data prep & EDA

## New features
```python
df['child'] = (df['age'] < 13).astype(int)
df['cabin_deck'] = df['cabin'].str[0]
df['solo'] = ((df['sibsp'] == 0) & (df['parch'] == 0)).astype(int)
```
+ child - binary variable (1 if age < 13 else 0)
+ cabin_deck - deck of the ship taken from first letter of cabin name
+ solo - binary variabble (1 if person was travelling without children/spouse/sibling etc.)

## Data size
After data cleaning and preparation size of dataset is 891 rows and 14 columns.

Global survivorship calculated based on given dataset is around 38%.


# Models

| Model  | AUC Score                              |
|------------|---------------------------------------------|
| Logistic Regression   | 0.83                                   | 
| DecisionTreeClassifier    | 0.850                             | 
| XGB    | 0.850                             | 
