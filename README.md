
# Problem statement
Would you survive the Titanic shipwreck
A model that predicts which passengers survived the Titanic shipwreck.
[more info](https://www.kaggle.com/competitions/titanic)

# Data / EDA / Models
[notebooks folder](./notebooks/README.md)

# How to run 
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





