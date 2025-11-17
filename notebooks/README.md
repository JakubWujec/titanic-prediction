# Data prep & EDA

## New features
```python
df['child'] = (df['age'] < 13).astype(int)
df['cabin_deck'] = df['cabin'].str[0]
df['solo'] = ((df['sibsp'] == 0) & (df['parch'] == 0)).astype(int)
```
+ child - binary variable (1 if age < 13 else 0)
+ solo - binary variabble (1 if person was travelling without children/spouse/sibling etc.)
+ cabin_deck - deck of the ship taken from first letter of cabin name

### Cabin Decks
The bulk of First-Class facilities and accommodation was located on the upper decks within the superstructure of the Titanic, where the vibrations and noise of the engines were at their lowest. The entirety of A-Deck was devoted to First-Class recreation accommodation, along with most of B and C Decks.[source:wiki](https://en.wikipedia.org/wiki/First-class_facilities_of_the_Titanic#location)

## Data size
After data cleaning and preparation size of dataset is 891 rows and 14 columns.

Global survivorship calculated based on given dataset is around 38%.


# Models

| Model  | AUC Score                              |
|------------|---------------------------------------------|
| Logistic Regression   | 0.83                                   | 
| DecisionTreeClassifier    | 0.850                             | 
| XGB    | 0.850                             | 
