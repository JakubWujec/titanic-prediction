
# Problem statement
Would you survive the Titanic shipwreck
A model that predicts which passengers survived the Titanic shipwreck.
[more info](https://www.kaggle.com/competitions/titanic)

# Dataset description
Data source: [link](https://www.kaggle.com/competitions/titanic/data?select=test.csv)

| Variable   | Definition                                  | Key                          |
|------------|---------------------------------------------|------------------------------|
| survival   | Survival                                    | 0 = No, 1 = Yes             |
| pclass     | Ticket class                                | 1 = 1st, 2 = 2nd, 3 = 3rd  |
| sex        | Sex                                         |                              |
| Age        | Age in years                               |                              |
| sibsp      | # of siblings / spouses aboard the Titanic |                              |
| parch      | # of parents / children aboard the Titanic |                              |
| ticket     | Ticket number                               |                              |
| fare       | Passenger fare                              |                              |
| cabin      | Cabin number                                |                              |
| embarked   | Port of Embarkation                        | C = Cherbourg, Q = Queenstown, S = Southampton |

## Variable Notes

### pclass: A proxy for socio-economic status (SES)
+ 1st = Upper
+ 2nd = Middle
+ 3rd = Lower

### age 
Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

### sibsp
The dataset defines family relations in this way...
+ Sibling = brother, sister, stepbrother, stepsister
+ Spouse = husband, wife (mistresses and fiancés were ignored)

### parch
The dataset defines family relations in this way...
+ Parent = mother, father
+ Child = daughter, son, stepdaughter, stepson

Some children travelled only with a nanny, therefore parch=0 for them.


# Modeling approach & metrics

# How to run locally and via Docker
## Locally
You need to have uv installed
```bash
uv sync
```
And then
```
py predict.py
```

## Via Docker
```bash
docker build -t titanic-model . 
```
and then
```bash
docker run -p 9696:9696 -it titanic-model
```


# API usage example
```bash
curl -X POST http://localhost:9696/api/predict \
     -H "Content-Type: application/json" \
     -d '{"age": 27, "pclass": "middle", "sex": "male", "solo": 1}'
```
or on windows
```bash
curl -X POST http://localhost:9696/api/predict ^
     -H "Content-Type: application/json" ^
     -d "{\"age\": 27, \"pclass\": \"middle\", \"sex\": \"male\", \"solo\": 1}"
```
or use make_request.py file

# Known limitations / next steps




