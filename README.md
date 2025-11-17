
# Problem statement
Would you survive the Titanic shipwreck?

The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.
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





