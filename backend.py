import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def load_data():
    data = {
        'price': [550000, 720000, 330000, 875000, 450000, 990000, 625000],
        'bedrooms': [3, 4, 2, 5, 3, 6, 4],
        'bathrooms': [2, 3, 1, 4, 2.5, 5, 2.5],
        'sqft_living': [1800, 2400, 1200, 3200, 2000, 4000, 2600],
        'sqft_lot': [5000, 6000, 3000, 7500, 5500, 10000, 7200],
        'floors': [1, 2, 1, 2, 2, 3, 2],
        'condition': [3, 4, 3, 5, 4, 5, 4],
        'yr_built': [1995, 2005, 1980, 2015, 1998, 2020, 2008],
        'yr_renovated': [0, 2010, 0, 2018, 2005, 0, 2012]
    }
    return pd.DataFrame(data)

def train_and_save_model(path='model.pkl'):
    df = load_data()
    x = df.drop('price', axis=1)
    y = df['price']
    model = LinearRegression()
    model.fit(x, y)
    joblib.dump((model, x.columns.tolist()), path)

def load_model(path='model.pkl'):
    if not os.path.exists(path):
        train_and_save_model(path)
    return joblib.load(path)

def predict_price(features, path='model.pkl'):
    model, columns = load_model(path)
    input_df = pd.DataFrame([features], columns=columns)
    return int(model.predict(input_df)[0])
